#!/bin/bash
# Master cleanup script for all mock labs
# Iterates over all labs/*/reset.sh and executes them

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LAB_DIRS=$(find "${SCRIPT_DIR}/cka" "${SCRIPT_DIR}/lfcs" -mindepth 1 -maxdepth 1 -type d)

echo "Starting master cleanup of all labs..."
echo "======================================"

for lab_dir in $LAB_DIRS; do
    if [[ -f "$lab_dir/reset.sh" ]]; then
        echo ""
        echo "Running reset script for: $lab_dir"
        echo "----------------------------------------"
        # Make sure it's executable
        chmod +x "$lab_dir/reset.sh" 2>/dev/null || true
        LAB_NAME=$(basename "$lab_dir")
        if "${SCRIPT_DIR}/lab" reset "$LAB_NAME"; then
            echo "✓ Reset successful for $LAB_NAME"
        else
            echo "✗ Reset failed for $LAB_NAME"
            # Continue with other labs
        fi
    else
        echo "⚠ No reset.sh found in $lab_dir"
    fi
done

echo ""
echo "======================================"
echo "Master cleanup completed."
