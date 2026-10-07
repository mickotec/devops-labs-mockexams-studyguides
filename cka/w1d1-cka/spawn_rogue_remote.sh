#!/usr/bin/env bash
set -euo pipefail

# Pre-pull image if missing
crictl inspecti docker.io/library/busybox:1.36 >/dev/null 2>&1 || crictl pull docker.io/library/busybox:1.36 >/dev/null 2>&1

if crictl ps -a 2>/dev/null | grep -q rogue-crypto-miner; then
  echo "[pid] Rogue container already present"
  exit 0
fi

cat > /tmp/rogue-sandbox.json << 'EOF'
{
  "metadata": { "name": "rogue-sandbox", "namespace": "default", "attempt": 0, "uid": "rogue-uid-001" },
  "log_directory": "/tmp/rogue-logs",
  "linux": {
    "cgroup_parent": "kubepods.slice",
    "security_context": { "namespace_options": { "network": 2, "pid": 1, "ipc": 1 }, "run_as_user": { "value": 0 } }
  }
}
EOF

mkdir -p /tmp/rogue-logs
SB=$(crictl runp /tmp/rogue-sandbox.json)
[ -n "$SB" ] || { echo "[ERROR] Could not create sandbox"; exit 1; }

cat > /tmp/rogue-container.json << 'EOF'
{
  "metadata": { "name": "rogue-crypto-miner" },
  "image": { "image": "docker.io/library/busybox:1.36" },
  "command": ["sh", "-c", "while true; do sleep 3600; done"],
  "stdin": true,
  "linux": {}
}
EOF

CT=$(crictl create "$SB" /tmp/rogue-container.json /tmp/rogue-sandbox.json)
[ -n "$CT" ] || { echo "[ERROR] Could not create rogue container"; exit 1; }

crictl start "$CT" >/dev/null 2>&1
echo "[pid] Rogue container spawned via crictl"
