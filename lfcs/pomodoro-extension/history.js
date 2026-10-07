// history.js - History page logic for CKA & LFCS Study Pomodoro
// Day / Session / Week views, timeline, stats, CSV export

const DAY_LABELS = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
const MONTH_LABELS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

let allHistory = [];
let view = 'day';        // 'day' | 'session' | 'week'
let navDate = new Date(); // current navigation date

// Init
document.addEventListener('DOMContentLoaded', () => {
  loadData();
  bindTabs();
  bindNav();
  document.getElementById('exportBtn').addEventListener('click', exportCSV);
});

// --- Load data from storage ---
function loadData() {
  chrome.storage.local.get('pomodoroState', (data) => {
    const state = data.pomodoroState;
    allHistory = (state && state.history) ? state.history : [];
    render();
  });
  // Listen for live updates
  chrome.storage.onChanged.addListener((changes) => {
    if (changes.pomodoroState) {
      const state = changes.pomodoroState.newValue;
      allHistory = (state && state.history) ? state.history : [];
      render();
    }
  });
}

// --- Tabs ---
function bindTabs() {
  document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      view = tab.dataset.view;
      render();
    });
  });
}

// --- Navigation ---
function bindNav() {
  document.getElementById('prevBtn').addEventListener('click', () => {
    if (view === 'day') {
      navDate.setDate(navDate.getDate() - 1);
    } else if (view === 'week') {
      navDate.setDate(navDate.getDate() - 7);
    } else {
      navDate.setDate(navDate.getDate() - 1);
    }
    render();
  });
  document.getElementById('nextBtn').addEventListener('click', () => {
    if (view === 'day') {
      navDate.setDate(navDate.getDate() + 1);
    } else if (view === 'week') {
      navDate.setDate(navDate.getDate() + 7);
    } else {
      navDate.setDate(navDate.getDate() + 1);
    }
    render();
  });
}

// --- Get filtered sessions for current view ---
function getFilteredSessions() {
  const d = new Date(navDate);
  if (view === 'day') {
    const key = toDateKey(d);
    return allHistory.filter(s => toDateKey(parseDate(s.timestamp)) === key);
  }
  if (view === 'week') {
    const weekStart = getWeekStart(d);
    const weekEnd = new Date(weekStart);
    weekEnd.setDate(weekEnd.getDate() + 7);
    return allHistory.filter(s => {
      const dt = parseDate(s.timestamp);
      return dt >= weekStart && dt < weekEnd;
    });
  }
  // session view: all sessions (filtered by date nav)
  const key = toDateKey(d);
  return allHistory.filter(s => toDateKey(parseDate(s.timestamp)) === key);
}

// --- Render everything ---
function render() {
  renderDateLabel();
  renderTimeline();
  renderStats();
  renderSessionList();
}

function renderDateLabel() {
  const el = document.getElementById('dateLabel');
  const d = new Date(navDate);
  if (view === 'week') {
    const ws = getWeekStart(d);
    const we = new Date(ws);
    we.setDate(we.getDate() + 6);
    el.textContent = `${formatShortDate(ws)} – ${formatShortDate(we)}`;
  } else {
    const today = new Date();
    const isToday = toDateKey(d) === toDateKey(today);
    el.textContent = isToday ? 'Today' : formatFullDate(d);
  }
}

// --- Timeline (hour-by-hour bar chart) ---
function renderTimeline() {
  const chart = document.getElementById('timelineChart');
  const labels = document.getElementById('timelineLabels');
  chart.innerHTML = '';
  labels.innerHTML = '';

  const sessions = getFilteredSessions();
  // Count work sessions per hour
  const hourCounts = new Array(24).fill(0);
  sessions.filter(s => s.type === 'work').forEach(s => {
    const dt = parseDate(s.timestamp);
    hourCounts[dt.getHours()]++;
  });
  const maxCount = Math.max(...hourCounts, 1);

  for (let h = 0; h < 24; h++) {
    const bar = document.createElement('div');
    bar.className = 'timeline-bar' + (hourCounts[h] > 0 ? ' filled' : '');
    const pct = hourCounts[h] / maxCount;
    bar.style.height = (pct * 100) + '%';
    bar.title = `${h}:00 – ${hourCounts[h]} sessions`;
    chart.appendChild(bar);

    const lbl = document.createElement('div');
    lbl.className = 'timeline-label';
    lbl.textContent = (h % 3 === 0) ? formatHour(h) : '';
    labels.appendChild(lbl);
  }
}

// --- Stats ---
function renderStats() {
  const sessions = getFilteredSessions();
  const workSessions = sessions.filter(s => s.type === 'work');
  const breakSessions = sessions.filter(s => s.type !== 'work');

  // Total work sessions
  document.getElementById('statTotal').textContent = workSessions.length;
  document.getElementById('statTotalSub').textContent = 'focus sessions';

  // Total breaks
  document.getElementById('statBreaks').textContent = breakSessions.length;
  const shortCount = breakSessions.filter(s => s.type === 'shortBreak').length;
  const longCount = breakSessions.filter(s => s.type === 'longBreak').length;
  document.getElementById('statBreaksSub').textContent = `${shortCount} short + ${longCount} long`;

  // Total focus time
  const totalMin = workSessions.reduce((sum, s) => sum + (s.durationMin || 25), 0);
  const hours = Math.floor(totalMin / 60);
  const mins = totalMin % 60;
  document.getElementById('statFocus').textContent = totalMin >= 60 ? `${hours}h${mins > 0 ? mins + 'm' : ''}` : `${totalMin}m`;
  document.getElementById('statFocusSub').textContent = `${workSessions.length} sessions × 25m`;

  // Best hour
  const hourCounts = new Array(24).fill(0);
  workSessions.forEach(s => {
    hourCounts[parseDate(s.timestamp).getHours()]++;
  });
  const bestHour = hourCounts.indexOf(Math.max(...hourCounts));
  document.getElementById('statBest').textContent = Math.max(...hourCounts) > 0 ? formatHour(bestHour) : '—';
  document.getElementById('statBestSub').textContent = Math.max(...hourCounts) > 0 ? `${Math.max(...hourCounts)} sessions` : 'no data';
}

// --- Session list ---
function renderSessionList() {
  const list = document.getElementById('sessionList');
  const title = document.getElementById('sessionTitle');
  const d = new Date(navDate);

  if (view === 'week') {
    const ws = getWeekStart(d);
    title.textContent = `Week of ${formatShortDate(ws)}`;
  } else if (view === 'session') {
    const isToday = toDateKey(d) === toDateKey(new Date());
    title.textContent = isToday ? 'All sessions today' : `Sessions for ${formatShortDate(d)}`;
  } else {
    const isToday = toDateKey(d) === toDateKey(new Date());
    title.textContent = isToday ? 'Today\'s sessions' : formatFullDate(d);
  }

  let sessions;
  if (view === 'week') {
    // Group by day for week view
    const ws = getWeekStart(d);
    const days = [];
    for (let i = 0; i < 7; i++) {
      const day = new Date(ws);
      day.setDate(day.getDate() + i);
      const key = toDateKey(day);
      const daySessions = allHistory.filter(s => toDateKey(parseDate(s.timestamp)) === key);
      if (daySessions.length > 0) {
        days.push({ date: day, sessions: daySessions });
      }
    }
    if (days.length === 0) {
      list.innerHTML = emptyState('No sessions this week');
      return;
    }
    list.innerHTML = days.map(({ date, sessions: ds }) => {
      const header = `<div style="padding:8px 16px;font-size:12px;font-weight:700;color:var(--accent);background:rgba(56,189,248,0.05);border-bottom:1px solid var(--border)">${formatFullDate(date)} · ${ds.filter(s=>s.type==='work').length} focus blocks</div>`;
      const items = ds.map(sessionRow).join('');
      return header + items;
    }).join('');
    return;
  }

  sessions = getFilteredSessions();
  // Sort newest first
  sessions.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

  if (sessions.length === 0) {
    list.innerHTML = emptyState('No completed sessions');
    return;
  }

  // Group by day
  const grouped = {};
  sessions.forEach(s => {
    const key = toDateKey(parseDate(s.timestamp));
    if (!grouped[key]) grouped[key] = [];
    grouped[key].push(s);
  });

  list.innerHTML = Object.keys(grouped).sort().reverse().map(key => {
    const daySessions = grouped[key];
    const dt = parseDate(daySessions[0].timestamp);
    const isToday = key === toDateKey(new Date());
    const dayLabel = isToday ? 'Today' : formatFullDate(dt);
    const count = daySessions.filter(s => s.type === 'work').length;
    const header = `<div style="padding:8px 16px;font-size:11px;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.5px;border-bottom:1px solid var(--border)">${dayLabel} · ${count} focus blocks</div>`;
    return header + daySessions.map(sessionRow).join('');
  }).join('');
}

function sessionRow(s) {
  const dt = parseDate(s.timestamp);
  const time = dt.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  const dur = s.durationMin || 25;
  let typeLabel, typeClass, dotClass;
  if (s.type === 'work') {
    typeLabel = `${s.track || 'Study'} Focus`;
    typeClass = s.track === 'LFCS' ? 'lfcs' : 'cka';
    dotClass = 'work';
  } else if (s.type === 'shortBreak') {
    typeLabel = 'Short Break';
    typeClass = '';
    dotClass = 'short';
  } else {
    typeLabel = 'Long Break';
    typeClass = '';
    dotClass = 'long';
  }
  const trackBadge = s.track ? `<span class="session-track ${typeClass}">${s.track}</span>` : '';
  return `
    <div class="session-item">
      <div class="session-dot ${dotClass}"></div>
      <div class="session-info">
        <div class="session-type">${typeLabel} ${trackBadge}</div>
        <div class="session-detail">${time}</div>
      </div>
      <div class="session-dur">${dur}m</div>
    </div>`;
}

function emptyState(msg) {
  return `<div class="empty-state"><div class="empty-icon">🍅</div><div>${msg}</div></div>`;
}

// --- CSV Export ---
function exportCSV() {
  const sessions = getFilteredSessions();
  if (sessions.length === 0) return;
  const rows = [['Type','Track','Duration (min)','Timestamp','Date','Time']];
  sessions.forEach(s => {
    const dt = parseDate(s.timestamp);
    rows.push([
      s.type === 'work' ? 'Focus' : s.type === 'shortBreak' ? 'Short Break' : 'Long Break',
      s.track || '',
      s.durationMin || 25,
      s.timestamp,
      dt.toLocaleDateString(),
      dt.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    ]);
  });
  const csv = rows.map(r => r.map(c => `"${String(c).replace(/"/g,'""')}"`).join(',')).join('\n');
  const blob = new Blob([csv], { type: 'text/csv' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `pomodoro-history-${toDateKey(navDate)}.csv`;
  a.click();
  URL.revokeObjectURL(url);
}

// --- Utilities ---
function parseDate(ts) {
  if (!ts) return new Date();
  return new Date(ts);
}

function toDateKey(d) {
  return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
}

function getWeekStart(d) {
  const result = new Date(d);
  const day = result.getDay(); // 0=Sun
  result.setDate(result.getDate() - day); // Start on Sunday
  result.setHours(0, 0, 0, 0);
  return result;
}

function formatShortDate(d) {
  return `${MONTH_LABELS[d.getMonth()]} ${d.getDate()}`;
}

function formatFullDate(d) {
  return `${DAY_LABELS[d.getDay()]}, ${MONTH_LABELS[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}`;
}

function formatHour(h) {
  if (h === 0) return '12am';
  if (h === 12) return '12pm';
  return h < 12 ? h + 'am' : (h - 12) + 'pm';
}
