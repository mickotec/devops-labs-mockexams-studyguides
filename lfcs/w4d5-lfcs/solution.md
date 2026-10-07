# [LFCS W4D5-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create `/usr/local/bin/daily-maint.sh`:
```bash
#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: daily-maint.sh <dir>" >&2
  exit 1
fi

TARGET_DIR="$1"
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Directory $TARGET_DIR does not exist" >&2
  exit 2
fi

COUNT=$(find "$TARGET_DIR" -maxdepth 1 -name "*.log" 2>/dev/null | wc -l)
echo "[$(date)] Processed logs in $TARGET_DIR: $COUNT files" >> /var/log/daily-maint.log
logger -t daily-maint "Maintenance completed for $TARGET_DIR"
```
`sudo chmod 755 /usr/local/bin/daily-maint.sh`

2. Run test:
`sudo /usr/local/bin/daily-maint.sh /var/log`
