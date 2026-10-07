# [LFCS W2D6-LFCS] Week 2 Speed Drills & Git Version Control

**Date:** 2026-10-10  
**Time Limit:** 45m  
**Difficulty:** Hard (Milestone Assessment 2)  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Milestone 2 Triathlon Tasks:
1. Initialize a git repository in `/srv/repo`.
2. Create and commit a configuration file `system.conf` with content `config=v1`.
3. Create a branch `feature-audit`, modify `system.conf` to `config=v2`, commit with message `feat: update v2`, switch back to `main` (or `master`), and merge `feature-audit`.
4. Create a tar.gz backup of the entire git repo into `/var/backups/repo.tar.gz`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d6-lfcs
```
