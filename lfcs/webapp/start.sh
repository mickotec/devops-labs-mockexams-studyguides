#!/usr/bin/env bash
# Start LFCS Study Todo Webapp & Simulator
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${DIR}/../.." && pwd)"
cd "$REPO_DIR"

if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
fi

PORT="${1:-5052}"
echo "======================================================================"
echo "  🐧 Starting LFCS Study Todo & Linux Exam Simulator on http://localhost:$PORT"
echo "======================================================================"
export PORT
exec python3 "${DIR}/app.py"
