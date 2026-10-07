# [LFCS W3D3-LFCS] Creating & Managing Systemd Services

**Date:** 2026-10-14  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Worker Script
Create a background script at `/usr/local/bin/worker-daemon.sh`:
- Make it executable (`chmod 755`).
- Contents: An infinite loop that writes `Worker ping: $(date)` to `/var/log/worker-daemon.log` every 3 seconds.

### Task 2: Create Systemd Service Unit
Create `/etc/systemd/system/worker-daemon.service`:
- `Description=Worker Daemon Service`
- `ExecStart=/usr/local/bin/worker-daemon.sh`
- `Restart=always`
- `[Install]` section with `WantedBy=multi-user.target`

### Task 3: Service Activation
1. Reload systemd (`systemctl daemon-reload`).
2. Enable and start `worker-daemon.service`.
3. Verify the service is active and the log file `/var/log/worker-daemon.log` is receiving entries.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d3-lfcs
```
