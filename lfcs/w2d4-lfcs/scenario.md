# [LFCS W2D4-LFCS] I/O Redirection & Stream Multiplexing

**Date:** 2026-10-08  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Separate Standard Streams
Search the `/etc` directory for files containing `shadow`:
- Redirect all stdout matches to `/var/tmp/stdout.log` (`1>`).
- Redirect all stderr permission errors to `/var/tmp/stderr.log` (`2>`).

### Task 2: Tee Pipeline Logging
Using `ps -ef` and `tee`, generate a process snapshot:
- Write the full output to `/var/tmp/process_dump.txt`.
- Simultaneously count the total number of lines into `/var/tmp/process_count.txt` via pipe.

### Task 3: Automated Health Report via Heredoc
Write a bash script `/var/tmp/gen_health.sh`:
- When executed, it uses a Here-Document (`cat << 'EOF' > ...`) to write `/var/tmp/health.report`.
- The report must contain lines for `HOST: $(hostname)` and `KERNEL: $(uname -r)`.
- Execute the script and ensure `/var/tmp/health.report` exists.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d4-lfcs
```
