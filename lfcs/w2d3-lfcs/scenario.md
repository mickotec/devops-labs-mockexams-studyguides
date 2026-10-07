# [LFCS W2D3-LFCS] Advanced Stream Analysis: Sed & Awk Fundamentals

**Date:** 2026-10-07  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Awk Field Extraction
Extract users from `/etc/passwd` whose UID is >= 1000 and print formatted output:
`User: <name> (UID: <uid>, Shell: <shell>)`
Save output to `/var/tmp/regular_users.txt`.

### Task 2: Sed Stream Editing
In file `/var/tmp/config_sample.ini`:
1. Replace all occurrences of `PORT = 8080` with `PORT = 443`.
2. Delete any line containing `DEBUG = True`.
3. Insert `ENVIRONMENT = Production` on a new line immediately after `[server]`.

### Task 3: CSV Aggregation with Awk
Given `/var/tmp/sales.csv`, compute the total sum of the values in column 2 (revenue).
Output the total number as plain text to `/var/tmp/sales_total.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d3-lfcs
```
