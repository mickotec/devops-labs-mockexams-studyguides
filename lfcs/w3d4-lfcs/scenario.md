# [LFCS W3D4-LFCS] Process Diagnostics & Signal Management

**Date:** 2026-10-15  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Rogue Process Termination
A rogue process simulating a memory leak (`rogue-sim`) is running in the background.
1. Locate its PID using `pgrep` or `ps`.
2. Terminate it gracefully with `SIGTERM` (15); if it remains, force terminate with `SIGKILL` (9).

### Task 2: Nice Priority Adjustment
A background workload process `batch-calc` is running.
- Use `renice` to lower its scheduling priority to nice value `+12`.

### Task 3: Resource Inventory
Generate `/var/tmp/process_report.txt` containing:
- The top 5 memory-consuming processes formatted with headers: `PID,USER,%MEM,COMMAND`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d4-lfcs
```
