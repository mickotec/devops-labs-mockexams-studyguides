#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w3d6-lfcs (Week 3 Systemd & Process Orchestration)..."
sudo mkdir -p /var/tmp/cache /usr/local/bin
sudo tee /usr/local/bin/payment-bridge.sh << 'EOF' >/dev/null
#!/usr/bin/env bash
while true; do sleep 3600; done
EOF
sudo chmod 755 /usr/local/bin/payment-bridge.sh

sudo tee /etc/systemd/system/payment-bridge.service << 'EOF' >/dev/null
[Unit]
Description=Payment Bridge Service
After=network.target

[Service]
Type=simple
ExecStart=/nonexistent/bridge
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo rm -f /etc/systemd/system/cache-cleaner.* /etc/security/limits.d/50-worker.conf
sudo systemctl daemon-reload
echo "[✓] Environment ready. Review tasks with: ./lab show w3d6-lfcs"
