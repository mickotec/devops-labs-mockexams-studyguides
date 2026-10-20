# [CKAD W5D6-CKAD] Batch Jobs, CronJobs & Concurrency Policies

**Date:** 2026-11-14  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox K8s Cluster (`controlplane`, `node01`, `node02`)  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Create Batch Job & Scheduled CronJob
1. In namespace `ckad-w5d6`, create a Job named `db-indexer`:
   - Image: `busybox:1.36`
   - Command: `["sh", "-c", "echo Indexing complete; exit 0"]`
   - `completions`: `3`
   - `parallelism`: `2`
   - `backoffLimit`: `3`
2. Create a CronJob named `log-archiver`:
   - Schedule: every 5 minutes (`*/5 * * * *`)
   - Image: `busybox:1.36`
   - Command: `["echo", "Archive completed"]`
   - `concurrencyPolicy`: `Forbid`
   - `successfulJobsHistoryLimit`: `3`
3. Verify `db-indexer` reaches 3/3 completions and `log-archiver` is active.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w5d6-ckad
```
