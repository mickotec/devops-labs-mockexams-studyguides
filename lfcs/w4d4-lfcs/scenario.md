# [LFCS W4D4-LFCS] Compiling Software from Source Code

**Date:** 2026-10-22  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Extract Source Code Archive
A C source code archive `/var/tmp/hello-c.tar.gz` has been prepared.
- Extract it into `/var/tmp/src-build/`.

### Task 2: Compile with GCC
Compile the extracted source code `hello.c` using `gcc` into an optimized binary at `/usr/local/bin/hello-app`:
- Ensure executable permissions (`chmod 755 /usr/local/bin/hello-app`).

### Task 3: Verify Binary Execution
Execute `/usr/local/bin/hello-app` and write its output to `/var/tmp/hello_output.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d4-lfcs
```
