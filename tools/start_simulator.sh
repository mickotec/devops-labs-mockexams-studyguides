#!/usr/bin/env bash
# ==============================================================================
# killer.sh & Linux Foundation / CNCF Real Exam Simulator Launcher
# Reproduces the PSI Secure Browser + XFCE Remote Desktop Experience
# ==============================================================================
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${DIR}/.." && pwd)"
cd "$ROOT_DIR"

EXAM_ID="${1:-}"

if [ -z "$EXAM_ID" ]; then
  echo "======================================================================"
  echo "  killer.sh & Linux Foundation Real Exam Simulator"
  echo "======================================================================"
  echo "Available Mock Exams:"
  echo "  1) mock-cka-1  - CKA Full-Scale Timed Mock Exam 1 (17 Questions | 120m)"
  echo "  2) mock-cka-2  - CKA Full-Scale Timed Mock Exam 2 (17 Questions | 120m)"
  echo "  3) mock-lfcs-1 - LFCS Full-Scale Timed Mock Exam 1 (20 Questions | 120m)"
  echo "  4) mock-lfcs-2 - LFCS Full-Scale Timed Mock Exam 2 (20 Questions | 120m)"
  echo ""
  read -p "Select exam [1-4] or enter mock ID (default: mock-cka-1): " choice
  case "$choice" in
    1) EXAM_ID="mock-cka-1" ;;
    2) EXAM_ID="mock-cka-2" ;;
    3) EXAM_ID="mock-lfcs-1" ;;
    4) EXAM_ID="mock-lfcs-2" ;;
    mock-*) EXAM_ID="$choice" ;;
    *) EXAM_ID="mock-cka-1" ;;
  esac
fi

echo ""
echo "[*] Preparing killer.sh Simulator for: $EXAM_ID"

# Ensure venv python dependencies are ready
if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
elif [ -f "${DIR}/.venv/bin/activate" ]; then
  source "${DIR}/.venv/bin/activate"
fi

# Check if web server is running on port 5050 with simulator support
if ! curl -sf http://localhost:5050/api/exam/list >/dev/null 2>&1; then
  echo "[*] Starting/Restarting Exam Simulator Web Server on port 5050..."
  pkill -f "python.*webapp/app.py" || true
  sleep 1
  PY_BIN="$ROOT_DIR/.venv/bin/python3"
  [ ! -f "$PY_BIN" ] && PY_BIN="python3"
  nohup "$PY_BIN" tools/webapp/app.py > /tmp/exam_simulator.log 2>&1 &
  sleep 2
fi

# Set up the lab environment
echo "[*] Initializing scenario environment via ./lab start $EXAM_ID..."
./lab start "$EXAM_ID"

EXAM_URL="http://localhost:5050/exam/$EXAM_ID"
echo ""
echo "======================================================================"
echo "  [✓] killer.sh Exam Simulation Environment Ready!"
echo "  Access URL: $EXAM_URL"
echo "======================================================================"
echo "  Features in Simulator:"
echo "    • Remote Desktop with split Terminal & Documentation Browser"
echo "    • Real-time 120m countdown timer with proctor alerts"
echo "    • Live interactive PTY terminal to cluster nodes"
echo "    • Restricted Kubernetes / Linux documentation browser"
echo "    • Question navigator, Flag for review, and persistent Notepad"
echo "    • Automated grader evaluating official Linux Foundation domain weights"
echo "======================================================================"

# Open in browser if GUI available
if [ -n "${DISPLAY:-}" ]; then
  if command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$EXAM_URL" >/dev/null 2>&1 || true
  elif command -v google-chrome >/dev/null 2>&1; then
    google-chrome "$EXAM_URL" >/dev/null 2>&1 || true
  elif command -v firefox >/dev/null 2>&1; then
    firefox "$EXAM_URL" >/dev/null 2>&1 || true
  fi
fi
