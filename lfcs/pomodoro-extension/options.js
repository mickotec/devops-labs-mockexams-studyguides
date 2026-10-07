// options.js - Settings page logic for CKA & LFCS Study Pomodoro
// Handles: timer durations, audio chimes, volume, work prefs, dim screen, chime preview

const DEFAULTS = {
  workMin: 25,
  shortBreakMin: 5,
  longBreakMin: 15,
  volume: 85,
  muted: false,
  selectedChime: 'bell',
  continueLastSession: false,
  notifications: true,
  dimScreen: false
};

const CHIMES = [
  { id: 'bell',                label: 'Bell',                file: 'audio/bell.mp3' },
  { id: 'chime',               label: 'Chime',               file: 'audio/chime.mp3' },
  { id: 'ding',                label: 'Ding',                file: 'audio/ding.mp3' },
  { id: 'gong',                label: 'Gong',                file: 'audio/gong.mp3' },
  { id: 'gong-2',              label: 'Gong 2',              file: 'audio/gong-2.mp3' },
  { id: 'glass-ping',          label: 'Glass Ping',          file: 'audio/glass-ping.mp3' },
  { id: 'analog-alarm-clock',  label: 'Analog Alarm Clock',  file: 'audio/analog-alarm-clock.mp3' },
  { id: 'digital-alarm-clock', label: 'Digital Alarm Clock', file: 'audio/digital-alarm-clock.mp3' },
  { id: 'digital-watch',       label: 'Digital Watch',       file: 'audio/digital-watch.mp3' },
  { id: 'computer-magic',      label: 'Computer Magic',      file: 'audio/computer-magic.mp3' },
  { id: 'music-box',           label: 'Music Box',           file: 'audio/music-box.mp3' },
  { id: 'pin-drop',            label: 'Pin Drop',            file: 'audio/pin-drop.mp3' },
  { id: 'pulse',               label: 'Pulse',               file: 'audio/pulse.mp3' },
  { id: 'robot-blip',          label: 'Robot Blip',          file: 'audio/robot-blip.mp3' },
  { id: 'robot-blip-1',        label: 'Robot Blip 1',        file: 'audio/robot-blip-1.mp3' },
  { id: 'wood-block',          label: 'Wood Block',          file: 'audio/wood-block.mp3' },
  { id: 'bike-horn',           label: 'Bike Horn',           file: 'audio/bike-horn.mp3' },
  { id: 'fire-pager',          label: 'Fire Pager',          file: 'audio/fire-pager.mp3' },
  { id: 'train-horn',          label: 'Train Horn',          file: 'audio/train-horn.mp3' },
  { id: 'tone',                label: 'Tone',                file: 'audio/tone.mp3' },
  { id: 'clock-tick',          label: 'Clock Tick',          file: 'audio/clock-tick.mp3' },
  { id: 'clock-tock',          label: 'Clock Tock',          file: 'audio/clock-tock.mp3' },
  { id: 'desk-clock-tick',     label: 'Desk Clock Tick',     file: 'audio/desk-clock-tick.mp3' },
  { id: 'desk-clock-tock',     label: 'Desk Clock Tock',     file: 'audio/desk-clock-tock.mp3' },
  { id: 'stopwatch-tick',      label: 'Stopwatch Tick',      file: 'audio/stopwatch-tick.mp3' },
  { id: 'stopwatch-tock',      label: 'Stopwatch Tock',      file: 'audio/stopwatch-tock.mp3' },
  { id: 'wall-clock-tick',     label: 'Wall Clock Tick',     file: 'audio/wall-clock-tick.mp3' },
  { id: 'wall-clock-tock',     label: 'Wall Clock Tock',     file: 'audio/wall-clock-tock.mp3' },
  { id: 'wind-up-clock-tick',  label: 'Wind-up Clock Tick',  file: 'audio/wind-up-clock-tick.mp3' },
  { id: 'wind-up-clock-tock',  label: 'Wind-up Clock Tock',  file: 'audio/wind-up-clock-tock.mp3' },
  { id: 'metronome-tick',      label: 'Metronome Tick',      file: 'audio/metronome-tick.mp3' },
  { id: 'metronome-tock',      label: 'Metronome Tock',      file: 'audio/metronome-tock.mp3' },
  { id: 'wristwatch-tick',     label: 'Wristwatch Tick',     file: 'audio/wristwatch-tick.mp3' },
  { id: 'wristwatch-tock',     label: 'Wristwatch Tock',     file: 'audio/wristwatch-tock.mp3' }
];

let settings = { ...DEFAULTS };
let currentAudio = null;

// Init
document.addEventListener('DOMContentLoaded', async () => {
  await loadSettings();
  buildChimeList();
  bindInputs();
  bindToggles();
  bindVolume();
});

// --- Load / Save ---

async function loadSettings() {
  return new Promise(resolve => {
    chrome.storage.local.get('pomodoroOptions', (data) => {
      if (data.pomodoroOptions) {
        settings = { ...DEFAULTS, ...data.pomodoroOptions };
      }
      applyValues();
      resolve();
    });
  });
}

function saveSettings() {
  chrome.storage.local.set({ pomodoroOptions: settings });
  // Notify background.js
  chrome.runtime.sendMessage({ action: 'settingsChanged', settings });
  showToast();
}

function applyValues() {
  document.getElementById('workMin').value = settings.workMin;
  document.getElementById('shortBreakMin').value = settings.shortBreakMin;
  document.getElementById('longBreakMin').value = settings.longBreakMin;
  document.getElementById('volumeSlider').value = settings.muted ? 0 : settings.volume;
  updateVolumeUI();
  // Toggles
  ['continueLastSession', 'notifications', 'dimScreen'].forEach(key => {
    const el = document.getElementById(key.replace('LastSession', 'Toggle').replace('ions', 'ionsToggle').replace('creen', 'creenToggle'));
  });
  setToggle('continueToggle', settings.continueLastSession);
  setToggle('notificationsToggle', settings.notifications);
  setToggle('dimToggle', settings.dimScreen);
}

function setToggle(id, val) {
  const el = document.getElementById(id);
  if (el) {
    if (val) el.classList.add('on');
    else el.classList.remove('on');
  }
}

// --- Number inputs ---

function bindInputs() {
  ['workMin', 'shortBreakMin', 'longBreakMin'].forEach(id => {
    const el = document.getElementById(id);
    el.addEventListener('change', () => {
      let v = parseInt(el.value, 10);
      if (isNaN(v) || v < 1) v = 1;
      if (v > 120) v = 120;
      el.value = v;
      settings[id] = v;
      saveSettings();
    });
  });
}

// --- Toggles ---

function bindToggles() {
  document.querySelectorAll('.toggle').forEach(el => {
    el.addEventListener('click', () => {
      const key = el.dataset.key;
      el.classList.toggle('on');
      settings[key] = el.classList.contains('on');
      saveSettings();
    });
  });
}

// --- Volume ---

function bindVolume() {
  const slider = document.getElementById('volumeSlider');
  const icon = document.getElementById('volIcon');

  slider.addEventListener('input', () => {
    settings.volume = parseInt(slider.value, 10);
    settings.muted = settings.volume === 0;
    updateVolumeUI();
    saveSettings();
  });

  icon.addEventListener('click', () => {
    settings.muted = !settings.muted;
    if (settings.muted) {
      slider.value = 0;
    } else {
      slider.value = settings.volume || 85;
    }
    updateVolumeUI();
    saveSettings();
  });
}

function updateVolumeUI() {
  const slider = document.getElementById('volumeSlider');
  const icon = document.getElementById('volIcon');
  const val = document.getElementById('volVal');
  const vol = settings.muted ? 0 : settings.volume;
  slider.value = vol;
  val.textContent = vol + '%';
  if (vol === 0 || settings.muted) {
    icon.textContent = '🔇';
    icon.classList.add('muted');
  } else if (vol < 40) {
    icon.textContent = '🔉';
    icon.classList.remove('muted');
  } else {
    icon.textContent = '🔊';
    icon.classList.remove('muted');
  }
}

// --- Chime List ---

function buildChimeList() {
  const list = document.getElementById('chimeList');
  list.innerHTML = '';
  CHIMES.forEach(chime => {
    const item = document.createElement('div');
    item.className = 'chime-item' + (chime.id === settings.selectedChime ? ' selected' : '');
    item.dataset.id = chime.id;
    item.innerHTML = `
      <div class="chime-dot"></div>
      <span class="chime-name">${chime.label}</span>
      <span class="chime-speaker" title="Preview">▶</span>
    `;
    // Click to select + preview
    item.addEventListener('click', (e) => {
      // Don't select if clicking speaker
      if (e.target.classList.contains('chime-speaker')) return;
      settings.selectedChime = chime.id;
      // Update UI
      list.querySelectorAll('.chime-item').forEach(i => i.classList.remove('selected'));
      item.classList.add('selected');
      saveSettings();
      // Play preview
      playChime(chime);
    });
    // Speaker click = preview only
    item.querySelector('.chime-speaker').addEventListener('click', (e) => {
      e.stopPropagation();
      playChime(chime);
    });
    list.appendChild(item);
  });
}

function playChime(chime) {
  stopChime();
  currentAudio = new Audio(chrome.runtime.getURL(chime.file));
  currentAudio.volume = settings.muted ? 0 : settings.volume / 100;
  currentAudio.play().catch(() => {});
}

function stopChime() {
  if (currentAudio) {
    currentAudio.pause();
    currentAudio = null;
  }
}

// --- Toast ---

function showToast() {
  const toast = document.getElementById('toast');
  toast.classList.add('show');
  clearTimeout(showToast._timer);
  showToast._timer = setTimeout(() => toast.classList.remove('show'), 1500);
}
