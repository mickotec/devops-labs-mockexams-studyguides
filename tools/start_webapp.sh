#!/usr/bin/env bash
# Start the CKA & LFCS Study Todo Web App
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${DIR}/.." && pwd)"
cd "$ROOT_DIR"

if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
elif [ -f "${DIR}/.venv/bin/activate" ]; then
    source "${DIR}/.venv/bin/activate"
else
    python3 -m venv .venv
    source .venv/bin/activate
    pip install flask flask-sock
fi

PORT="${1:-5050}"
echo "Starting Study Todo Web App on http://localhost:$PORT"
echo "Press Ctrl+C to stop"
exec python3 tools/webapp/app.py
