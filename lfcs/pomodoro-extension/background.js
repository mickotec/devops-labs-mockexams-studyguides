// background.js - Pomodoro timer with Marinara-style left-click controls, stop timer, and audio chimes
const ALARM_NAME = "pomodoro_tick";

const WORK_MIN = 25;
const SHORT_BREAK_MIN = 5;
const LONG_BREAK_MIN = 15;
const WEBAPP_URL = "http://127.0.0.1:5050";

// Module-level cache of user options (loaded at startup, refreshed on settingsChanged)
let cachedOptions = { workMin: WORK_MIN, shortBreakMin: SHORT_BREAK_MIN, longBreakMin: LONG_BREAK_MIN };

async function refreshOptions() {
  const opts = await getOptions();
  cachedOptions = opts;
  return opts;
}

function getPhaseTotalSec(mode) {
  const w = (cachedOptions.workMin || WORK_MIN) * 60;
  const s = (cachedOptions.shortBreakMin || SHORT_BREAK_MIN) * 60;
  const l = (cachedOptions.longBreakMin || LONG_BREAK_MIN) * 60;
  if (mode === "work") return w;
  if (mode === "longBreak") return l;
  return s;
}

// Suggest study track based on the daily study schedule (Mon–Sat; Sun rest):
//   08:00–12:00 CKA, 12:00–15:00 Recovery, 15:00–18:00 LFCS
function suggestTrack(d = new Date()) {
  const day = d.getDay(); // 0=Sun … 6=Sat
  if (day === 0) return null; // Sunday: no scheduled study
  const h = d.getHours();
  if (h >= 8 && h < 12) return "CKA";
  if (h >= 15 && h < 18) return "LFCS";
  return null; // recovery or off-schedule → leave as-is
}

const DEFAULT_SETTINGS = {
  workMin: WORK_MIN,
  shortBreakMin: SHORT_BREAK_MIN,
  longBreakMin: LONG_BREAK_MIN,
  track: "CKA",
  mode: "work", // "work", "shortBreak", "longBreak"
  status: "stopped", // "running", "paused", "stopped"
  cycleCount: 0,
  timeLeftSec: WORK_MIN * 60,
  targetEndTime: null,
  completedSessions: { CKA: 0, LFCS: 0 },
  breakCounts: { short: 0, long: 0 },
  todayDate: new Date().toLocaleDateString(),
  history: []
};

// User-configurable options (written by options.js)
const DEFAULT_OPTIONS = {
  workMin: WORK_MIN,
  shortBreakMin: SHORT_BREAK_MIN,
  longBreakMin: LONG_BREAK_MIN,
  volume: 85,
  muted: false,
  selectedChime: "bell",
  continueLastSession: false,
  notifications: true,
  dimScreen: false
};

async function getOptions() {
  const data = await chrome.storage.local.get("pomodoroOptions");
  return { ...DEFAULT_OPTIONS, ...(data.pomodoroOptions || {}) };
}

// Marinara-style Offscreen Audio
let creatingOffscreenPromise = null;
async function playSound(audioFile = null) {
  const opts = await getOptions();
  // Resolve chime file only if not explicitly passed
  if (!audioFile) {
    const chimeFiles = {
      "bell": "audio/bell.mp3", "chime": "audio/chime.mp3", "ding": "audio/ding.mp3",
      "gong": "audio/gong.mp3", "gong-2": "audio/gong-2.mp3", "glass-ping": "audio/glass-ping.mp3",
      "analog-alarm-clock": "audio/analog-alarm-clock.mp3",
      "digital-alarm-clock": "audio/digital-alarm-clock.mp3",
      "digital-watch": "audio/digital-watch.mp3",
      "computer-magic": "audio/computer-magic.mp3", "music-box": "audio/music-box.mp3",
      "pin-drop": "audio/pin-drop.mp3", "pulse": "audio/pulse.mp3",
      "robot-blip": "audio/robot-blip.mp3", "robot-blip-1": "audio/robot-blip-1.mp3",
      "wood-block": "audio/wood-block.mp3", "bike-horn": "audio/bike-horn.mp3",
      "fire-pager": "audio/fire-pager.mp3", "train-horn": "audio/train-horn.mp3",
      "tone": "audio/tone.mp3"
    };
    audioFile = chimeFiles[opts.selectedChime || "bell"] || "audio/bell.mp3";
  }
  // If muted, skip playback entirely
  if (opts.muted) return;

  try {
    const offscreenUrl = chrome.runtime.getURL("offscreen.html");
    const existingContexts = await chrome.runtime.getContexts({
      contextTypes: ["OFFSCREEN_DOCUMENT"],
      documentUrls: [offscreenUrl]
    });

    if (existingContexts.length === 0) {
      if (creatingOffscreenPromise) {
        await creatingOffscreenPromise;
      } else {
        creatingOffscreenPromise = chrome.offscreen.createDocument({
          url: "offscreen.html",
          reasons: ["AUDIO_PLAYBACK"],
          justification: "Play notification chime on pomodoro interval transition"
        });
        await creatingOffscreenPromise;
        creatingOffscreenPromise = null;
      }
    }

    chrome.runtime.sendMessage({
      target: "offscreen-audio",
      audioFile,
      volume: (opts.volume || 85) / 100
    }).catch(() => {});
  } catch (err) {
    console.error("Failed to play audio chime:", err);
  }
}

async function getState() {
  const data = await chrome.storage.local.get("pomodoroState");
  let state = data.pomodoroState;
  if (!state) {
    state = { ...DEFAULT_SETTINGS };
    await chrome.storage.local.set({ pomodoroState: state });
    return state;
  }

  // Daily reset
  const today = new Date().toLocaleDateString();
  if (state.todayDate !== today) {
    state.todayDate = today;
    state.completedSessions = { CKA: 0, LFCS: 0 };
    state.breakCounts = { short: 0, long: 0 };
    state.cycleCount = 0;
    await chrome.storage.local.set({ pomodoroState: state });
  }

  // Calculate remaining time from targetEndTime if running
  if (state.status === "running" && state.targetEndTime) {
    const remaining = Math.max(0, Math.round((state.targetEndTime - Date.now()) / 1000));
    state.timeLeftSec = remaining;
  }

  // Compatibility for older boolean isRunning
  state.isRunning = (state.status === "running");

  return state;
}

async function saveState(state) {
  state.isRunning = (state.status === "running");
  await chrome.storage.local.set({ pomodoroState: state });
  updateBadgeAndIcon(state);
}

function updateBadgeAndIcon(state) {
  const isWork = state.mode === "work";
  const titleTrack = `${state.track} (${isWork ? 'Focus' : (state.mode === 'longBreak' ? 'Long Break' : 'Short Break')})`;

  if (state.status === "stopped") {
    // Clear badge completely when stopped
    chrome.action.setBadgeText({ text: "" });
    chrome.action.setIcon({
      path: {
        16: "icons/icon16.png",
        48: "icons/icon48.png",
        128: "icons/icon128.png"
      }
    });
    chrome.action.setTitle({ title: `${titleTrack} - Stopped (Click to Start)` });
    return;
  }

  if (state.status === "paused") {
    const min = Math.ceil(state.timeLeftSec / 60);
    chrome.action.setBadgeText({ text: `${min}m` });
    chrome.action.setBadgeBackgroundColor({ color: "#F59E0B" }); // Amber paused badge
    chrome.action.setIcon({
      path: {
        16: "icons/icon_paused16.png",
        48: "icons/icon_paused48.png",
        128: "icons/icon_paused128.png"
      }
    });
    chrome.action.setTitle({ title: `${titleTrack} - Paused at ${formatTime(state.timeLeftSec)} (Click to Resume)` });
    return;
  }

  // Running
  const min = Math.ceil(state.timeLeftSec / 60);
  const badgeText = (state.timeLeftSec < 60) ? "<1m" : `${min}m`;
  chrome.action.setBadgeText({ text: badgeText });
  chrome.action.setBadgeBackgroundColor({ color: isWork ? "#EF4444" : "#10B981" });
  chrome.action.setIcon({
    path: {
      16: "icons/icon16.png",
      48: "icons/icon48.png",
      128: "icons/icon128.png"
    }
  });
  chrome.action.setTitle({ title: `${titleTrack} - ${formatTime(state.timeLeftSec)} remaining (Click to Pause)` });
}

function formatTime(totalSec) {
  const m = Math.floor(totalSec / 60);
  const s = totalSec % 60;
  return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
}

// 1-minute interval alarm for background sync
chrome.alarms.get(ALARM_NAME, (alarm) => {
  if (!alarm) {
    chrome.alarms.create(ALARM_NAME, { periodInMinutes: 1 / 60 });
  }
});

// Load user options on startup
refreshOptions();

chrome.alarms.onAlarm.addListener(async (alarm) => {
  if (alarm.name !== ALARM_NAME) return;
  const state = await getState();
  if (state.status !== "running") return;

  if (state.timeLeftSec > 0) {
    await saveState(state);
  } else {
    await handleCompletion(state);
  }
});

function startPhase(state, mode = null) {
  if (mode) state.mode = mode;
  state.status = "running";
  if (!state.timeLeftSec || state.timeLeftSec <= 0) {
    state.timeLeftSec = getPhaseTotalSec(state.mode);
  }
  state.targetEndTime = Date.now() + (state.timeLeftSec * 1000);
}

function pauseTimer(state) {
  if (state.targetEndTime) {
    state.timeLeftSec = Math.max(0, Math.round((state.targetEndTime - Date.now()) / 1000));
  }
  state.status = "paused";
  state.targetEndTime = null;
}

function resumeTimer(state) {
  state.status = "running";
  if (!state.timeLeftSec || state.timeLeftSec <= 0) {
    state.timeLeftSec = getPhaseTotalSec(state.mode);
  }
  state.targetEndTime = Date.now() + (state.timeLeftSec * 1000);
}

function stopTimer(state) {
  state.status = "stopped";
  state.targetEndTime = null;
  state.timeLeftSec = getPhaseTotalSec(state.mode);
}

// Marinara-style 3-state left click action
async function toggleTimerState() {
  const state = await getState();
  if (state.status === "running") {
    pauseTimer(state);
  } else if (state.status === "paused") {
    resumeTimer(state);
  } else {
    // stopped: start next / current phase
    // If starting a fresh work timer, auto-select the track matching the study schedule
    if (state.mode === "work") {
      const suggested = suggestTrack();
      if (suggested) state.track = suggested;
    }
    startPhase(state);
  }
  await saveState(state);
}

// Left-click icon
chrome.action.onClicked.addListener(() => {
  toggleTimerState();
});

// Clicking completion notification restarts / advances next timer
chrome.notifications.onClicked.addListener(async (notificationId) => {
  if (notificationId === "pomodoro-complete") {
    chrome.notifications.clear(notificationId);
    toggleTimerState();
  }
});

// Context menus setup
function setupContextMenus() {
  if (!chrome.contextMenus) return;
  chrome.contextMenus.removeAll(() => {
    const menus = [
      { id: "pomodoro-toggle", title: "Toggle Start / Pause" },
      { id: "pomodoro-stop", title: "Stop Timer" },
      { id: "pomodoro-reset", title: "Reset Current Phase" },
      { id: "pomodoro-start-short-break", title: "Start Short Break" },
      { id: "pomodoro-start-long-break", title: "Start Long Break" },
      { id: "pomodoro-open-settings", title: "Open Settings" },
      { id: "pomodoro-open-history", title: "Open History" },
      { id: "pomodoro-open-webapp", title: "Study WebApp (Port 5050)" }
    ];
    menus.forEach(item => {
      chrome.contextMenus.create({
        id: item.id,
        title: item.title,
        contexts: ["action"]
      }, () => {
        if (chrome.runtime.lastError) {
          // ignore duplicate id or context error
        }
      });
    });
  });
}

chrome.runtime.onInstalled.addListener(() => {
  setupContextMenus();
});

chrome.runtime.onStartup.addListener(() => {
  setupContextMenus();
});

if (chrome.contextMenus && chrome.contextMenus.onClicked) {
  chrome.contextMenus.onClicked.addListener(async (info) => {
    const state = await getState();
    switch (info.menuItemId) {
      case "pomodoro-toggle":
        await toggleTimerState();
        return;
      case "pomodoro-stop":
        stopTimer(state);
        break;
      case "pomodoro-reset":
        stopTimer(state);
        break;
      case "pomodoro-start-short-break":
        state.timeLeftSec = getPhaseTotalSec("shortBreak");
        startPhase(state, "shortBreak");
        break;
      case "pomodoro-start-long-break":
        state.timeLeftSec = getPhaseTotalSec("longBreak");
        startPhase(state, "longBreak");
        break;
      case "pomodoro-open-webapp":
        chrome.tabs.create({ url: WEBAPP_URL });
        return;
      case "pomodoro-open-settings":
        if (chrome.runtime.openOptionsPage) {
          chrome.runtime.openOptionsPage();
        } else {
          chrome.tabs.create({ url: chrome.runtime.getURL("options.html") });
        }
        return;
      case "pomodoro-open-history":
        chrome.tabs.create({ url: chrome.runtime.getURL("history.html") });
        return;
    }
    await saveState(state);
  });
}

async function handleCompletion(state) {
  const wasWork = state.mode === "work";
  const track = state.track;
  const now = new Date();

  // Record the total phase duration actually configured for this session
  const workTotalMin = Math.round(getPhaseTotalSec("work") / 60);
  const shortTotalMin = Math.round(getPhaseTotalSec("shortBreak") / 60);
  const longTotalMin = Math.round(getPhaseTotalSec("longBreak") / 60);

  if (wasWork) {
    state.cycleCount = (state.cycleCount || 0) + 1;
    state.completedSessions[track] = (state.completedSessions[track] || 0) + 1;
    state.history.unshift({
      id: Date.now(),
      track,
      type: "work",
      durationMin: workTotalMin,
      timestamp: now.toISOString(),
      timeFormatted: now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      dateStr: now.toLocaleDateString()
    });

    playSound();

    if (state.cycleCount >= 3) {
      state.mode = "longBreak";
      state.timeLeftSec = getPhaseTotalSec("longBreak");
      state.breakCounts.long += 1;
      state.cycleCount = 0;
      notify("🏆 3 Focus Blocks Done! 15‑Minute Break",
        "Great job! 15‑minute long break started.");
    } else {
      state.mode = "shortBreak";
      state.timeLeftSec = getPhaseTotalSec("shortBreak");
      state.breakCounts.short += 1;
      notify("☕ 25m Focus Block Finished!",
        `Take 5 min break! (Block ${state.cycleCount}/3 before long break)`);
    }
  } else {
    const wasLong = state.mode === "longBreak";
    state.history.unshift({
      id: Date.now(),
      track,
      type: wasLong ? "longBreak" : "shortBreak",
      durationMin: wasLong ? longTotalMin : shortTotalMin,
      timestamp: now.toISOString(),
      timeFormatted: now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      dateStr: now.toLocaleDateString()
    });

    playSound();

    state.mode = "work";
    const nextTrack = suggestTrack();
    if (nextTrack) state.track = nextTrack;
    state.timeLeftSec = getPhaseTotalSec("work");
    notify("⚡ Break Over — 25m Focus Session",
      `Ready for ${state.track}? ${Math.round(getPhaseTotalSec("work")/60)} minutes focus started!`);
  }

  if (state.history.length > 200) state.history = state.history.slice(0, 200);
  startPhase(state);
  await saveState(state);
}

function notify(title, message) {
  // Respect the user's notification preference in options
  getOptions().then(opts => {
    if (opts.notifications === false) return;
    chrome.notifications.create("pomodoro-complete", {
      type: "basic",
      iconUrl: "icons/icon128.png",
      title,
      message,
      priority: 2,
      requireInteraction: true
    });
  });
}

chrome.runtime.onMessage.addListener((req, sender, sendResponse) => {
  if (req.action === "getState") {
    getState().then(sendResponse);
    return true;
  }
  if (req.action === "settingsChanged") {
    // Store options, update current timer duration if idle
    const opts = req.settings || {};
    getOptions().then(async (stored) => {
      const merged = { ...stored, ...opts };
      await chrome.storage.local.set({ pomodoroOptions: merged });
      cachedOptions = { ...cachedOptions, ...merged };
      const state = await getState();
      if (state.status !== "running") {
        state.timeLeftSec = getPhaseTotalSec(state.mode);
        await saveState(state);
      }
      sendResponse({ ok: true });
    });
    return true;
  }
  if (req.action === "toggleTimer") {
    toggleTimerState().then(() => getState()).then(sendResponse);
    return true;
  }
  if (req.action === "stopTimer") {
    getState().then(async (state) => {
      stopTimer(state);
      await saveState(state);
      sendResponse(state);
    });
    return true;
  }
  if (req.action === "resetTimer") {
    getState().then(async (state) => {
      stopTimer(state);
      await saveState(state);
      sendResponse(state);
    });
    return true;
  }
  if (req.action === "setTrack") {
    getState().then(async (state) => {
      state.track = req.track;
      await saveState(state);
      sendResponse(state);
    });
    return true;
  }
  if (req.action === "setMode") {
    getState().then(async (state) => {
      state.mode = req.mode;
      stopTimer(state);
      await saveState(state);
      sendResponse(state);
    });
    return true;
  }
  if (req.action === "clearHistory") {
    getState().then(async (state) => {
      state.history = [];
      state.breakCounts = { short: 0, long: 0 };
      await saveState(state);
      sendResponse(state);
    });
    return true;
  }
});