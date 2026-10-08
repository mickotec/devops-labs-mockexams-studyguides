// popup.js - handles UI updates and user interactions
let updateTimerInterval = null;

document.addEventListener('DOMContentLoaded', () => {
  // DOM elements
  const ckaTab = document.getElementById('ckaTab');
  const lfcsTab = document.getElementById('lfcsTab');
  const workModeBtn = document.getElementById('workModeBtn');
  const shortBreakBtn = document.getElementById('shortBreakBtn');
  const longBreakBtn = document.getElementById('longBreakBtn');
  const timerDisplay = document.getElementById('timerDisplay');
  const modeLabel = document.getElementById('modeLabel');
  const startBtn = document.getElementById('startBtn');
  const resetBtn = document.getElementById('resetBtn');
  const statusDot = document.getElementById('statusDot');
  const sessionStats = document.getElementById('sessionStats');
  const shortBreakCount = document.getElementById('shortBreakCount');
  const longBreakCount = document.getElementById('longBreakCount');
  const breakStats = document.getElementById('breakStats');
  const pill1 = document.getElementById('pill1');
  const pill2 = document.getElementById('pill2');
  const pill3 = document.getElementById('pill3');
  const historyList = document.getElementById('historyList');
  const clearHistoryBtn = document.getElementById('clearHistoryBtn');
  const openWebApp = document.getElementById('openWebApp');
  const titleWebAppBtn = document.getElementById('titleLink');

  let state = {
    workMin: 25,
    shortBreakMin: 5,
    longBreakMin: 15,
    track: 'CKA',
    mode: 'work',
    cycleCount: 0,
    timeLeftSec: 25 * 60,
    isRunning: false,
    status: 'stopped',
    completedSessions: { CKA: 0, LFCS: 0 },
    breakCounts: { short: 0, long: 0 },
    history: []
  };

  // Initialize
  initializeUI();
  startTimerUpdate();

  // Event Listeners
  if (titleWebAppBtn) {
    titleWebAppBtn.addEventListener('click', (e) => {
      e.preventDefault();
      chrome.tabs.create({ url: 'http://127.0.0.1:5050' });
    });
  }

  ckaTab.addEventListener('click', () => {
    sendCommand({ action: 'setTrack', track: 'CKA' });
  });

  lfcsTab.addEventListener('click', () => {
    sendCommand({ action: 'setTrack', track: 'LFCS' });
  });

  workModeBtn.addEventListener('click', () => {
    sendCommand({ action: 'setMode', mode: 'work' });
  });

  shortBreakBtn.addEventListener('click', () => {
    sendCommand({ action: 'setMode', mode: 'shortBreak' });
  });

  longBreakBtn.addEventListener('click', () => {
    sendCommand({ action: 'setMode', mode: 'longBreak' });
  });

  startBtn.addEventListener('click', () => {
    sendCommand({ action: 'toggleTimer' });
  });

  resetBtn.addEventListener('click', () => {
    sendCommand({ action: 'resetTimer' });
  });

  clearHistoryBtn.addEventListener('click', () => {
    sendCommand({ action: 'clearHistory' });
  });

  openWebApp.addEventListener('click', () => {
    chrome.tabs.create({ url: 'http://127.0.0.1:5051' });
  });

  const openSettingsLink = document.getElementById('openSettingsLink');
  if (openSettingsLink) {
    openSettingsLink.addEventListener('click', (e) => {
      e.preventDefault();
      if (chrome.runtime.openOptionsPage) {
        chrome.runtime.openOptionsPage();
      } else {
        chrome.tabs.create({ url: chrome.runtime.getURL('options.html') });
      }
    });
  }

  // Functions
  function initializeUI() {
    chrome.runtime.sendMessage({ action: 'getState' }, (response) => {
      if (chrome.runtime.lastError) return;
      if (response) {
        state = response;
        updateAllUI();
      }
    });
  }

  function sendCommand(message) {
    chrome.runtime.sendMessage(message, (response) => {
      if (chrome.runtime.lastError) return;
      if (response) {
        state = response;
        updateAllUI();
      }
    });
  }

  function startTimerUpdate() {
    clearInterval(updateTimerInterval);
    updateTimerInterval = setInterval(() => {
      chrome.runtime.sendMessage({ action: 'getState' }, (response) => {
        if (chrome.runtime.lastError) return;
        if (response) {
          state = response;
          updateAllUI();
        }
      });
    }, 1000);
  }

  function updateAllUI() {
    updateTimerDisplay();
    updateStartButton();
    updateSessionStats();
    updateBreakStats();
    updateCyclePills();
    updateTrackTabs();
    updateModeButtons();
    updateStatusDot();
    updateHistoryList();
  }

  function updateTimerDisplay() {
    const minutes = Math.floor(state.timeLeftSec / 60);
    const seconds = state.timeLeftSec % 60;
    timerDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    timerDisplay.className = `timer-digits ${state.mode === 'work' ? 'work' : 'break'}`;
  }

  function updateStartButton() {
    const isRunning = (state.status === 'running' || state.isRunning);
    const isPaused = (state.status === 'paused');

    if (isRunning) {
      startBtn.textContent = '⏸ Pause';
      startBtn.className = 'btn btn-main running';
    } else if (isPaused) {
      startBtn.textContent = '▶ Resume';
      startBtn.className = 'btn btn-main';
    } else {
      startBtn.textContent = '▶ Start Focus';
      startBtn.className = 'btn btn-main';
    }
  }

  function updateSessionStats() {
    const ckaDone = state.completedSessions?.CKA || 0;
    const lfcsDone = state.completedSessions?.LFCS || 0;
    sessionStats.textContent = `Today: CKA ${ckaDone} • LFCS ${lfcsDone}`;
  }

  function updateBreakStats() {
    const short = state.breakCounts?.short || 0;
    const long = state.breakCounts?.long || 0;
    shortBreakCount.textContent = short;
    longBreakCount.textContent = long;
    breakStats.style.display = 'flex';
  }

  function updateCyclePills() {
    const cycle = state.cycleCount || 0;
    pill1.className = cycle >= 1 ? 'pill filled' : 'pill';
    pill2.className = cycle >= 2 ? 'pill filled' : 'pill';
    pill3.className = cycle >= 3 ? 'pill filled' : 'pill';
  }

  function updateTrackTabs() {
    if (state.track === 'CKA') {
      ckaTab.className = 'track-btn active cka';
      lfcsTab.className = 'track-btn lfcs';
    } else {
      ckaTab.className = 'track-btn cka';
      lfcsTab.className = 'track-btn active lfcs';
    }
  }

  function updateModeButtons() {
    const mode = state.mode;
    workModeBtn.className = mode === 'work' ? 'mode-btn active' : 'mode-btn';
    shortBreakBtn.className = mode === 'shortBreak' ? 'mode-btn active' : 'mode-btn';
    longBreakBtn.className = mode === 'longBreak' ? 'mode-btn active' : 'mode-btn';

    if (mode === 'work') {
      modeLabel.textContent = `${state.track === 'CKA' ? 'CKA' : 'LFCS'} 25m Focus`;
    } else if (mode === 'shortBreak') {
      modeLabel.textContent = '5m Break';
    } else if (mode === 'longBreak') {
      modeLabel.textContent = '15m Long Break';
    }
  }

  function updateStatusDot() {
    const isRunning = (state.status === 'running' || state.isRunning);
    if (isRunning) {
      statusDot.className = 'status-dot active';
    } else {
      statusDot.className = 'status-dot';
    }
  }

  function updateHistoryList() {
    const history = state.history || [];
    if (history.length === 0) {
      historyList.innerHTML = '<div style="color: var(--text-muted); text-align: center; padding: 4px;">No completed sessions yet</div>';
      return;
    }
    const recent = history.slice(0, 5);
    historyList.innerHTML = recent.map(item => {
      const time = item.timeFormatted;
      let label, cls;
      if (item.type === 'work') {
        label = `${item.track} 25m Focus`;
        cls = 'tag-work';
      } else if (item.type === 'shortBreak') {
        label = '5m Break';
        cls = 'tag-short';
      } else if (item.type === 'longBreak') {
        label = '15m Long Break';
        cls = 'tag-long';
      }
      return `<div class="history-item"><span class="${cls}">${label}</span><span>${time}</span></div>`;
    }).join('');
  }

  // Cleanup on unload
  window.addEventListener('unload', () => {
    clearInterval(updateTimerInterval);
  });
});