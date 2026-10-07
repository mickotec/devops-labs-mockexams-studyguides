# [LFCS W8D1-LFCS] Containers & Virtual Machines on Linux

**Date:** 2026-11-16  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Launch Detached Web Container
1. Ensure `podman` or `docker` is available on the system.
2. Run a detached container named `web-container` using image `docker.io/library/nginx:alpine` (or `nginx:alpine`):
   - Publish port `8085` on host to port `80` in container.

### Task 2: Container Volume Bind Mount
1. Create directory `/var/data/worker` on the host:
   `sudo mkdir -p /var/data/worker && sudo chmod 777 /var/data/worker`
2. Run a container named `data-worker` using image `docker.io/library/busybox:1.36` (or `busybox:1.36`):
   - Mount host directory `/var/data/worker` to `/data` in the container.
   - Command: `sh -c "while true; do date >> /data/timestamp.log; sleep 2; done"`

### Task 3: Extract Container IP Address
1. Use `podman inspect` or `docker inspect` to extract the IP address (or NetworkSettings IP) of `web-container`.
2. Save the IP address to `/var/tmp/container_ip.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w8d1-lfcs
```
