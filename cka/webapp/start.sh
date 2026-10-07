#!/usr/bin/env bash
# Start CKA Study Todo Webapp & Simulator
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${DIR}/../.." && pwd)"
cd "$REPO_DIR"

if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
fi

PORT="${1:-5051}"
echo "======================================================================"
echo "  ☸ Starting CKA Study Todo & killer.sh Simulator on http://localhost:$PORT"
echo "======================================================================"
export PORT
exec python3 "${DIR}/app.py"
