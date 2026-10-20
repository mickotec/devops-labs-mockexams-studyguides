# [CKAD W2D3-CKAD] Mounting ConfigMaps as Filesystem Volumes

**Date:** 2026-10-21  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Mount Custom Configuration File into Nginx
1. In namespace `ckad-w2d3`, create a ConfigMap named `custom-nginx-conf` containing key `default.conf` with content:
   `server { listen 8088; location / { return 200 "CUSTOM-PORT-OK
"; } }`
2. Deploy Pod `nginx-custom-port` using image `nginx:1.24-alpine`.
3. Mount the ConfigMap volume at `/etc/nginx/conf.d` so Nginx loads the custom configuration.
4. Verify that running `wget -qO- 127.0.0.1:8088` inside the container returns `"CUSTOM-PORT-OK"`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d3-ckad
```
