# [LFCS W1D5-LFCS] Pagers, Vim Mastery & Terminal Editing

**Date:** 2026-09-18  
**Time Limit:** 25m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Engineer Vim Profile Configuration
Configure your user's `~/.vimrc` with:
- Line numbering (`set number`)
- Syntax highlighting (`syntax on`)
- 4-space indentation (`set tabstop=4`, `set shiftwidth=4`, `set expandtab`)
- Incremental search highlighting (`set hlsearch`, `set incsearch`)

### Task 2: In-place Refactoring of Legacy Configuration
A configuration file `/var/tmp/app_legacy.conf` requires updating:
1. Replace all occurrences of `PORT = 8080` with `PORT = 8443`.
2. Uncomment the line `# SSL_ENABLED = true` to `SSL_ENABLED = true`.
3. Delete all lines containing `DEPRECATED`.

### Task 3: Text Pipeline Analysis
Analyze `/var/tmp/sample_audit.log`:
1. Extract all unique status code fields (`STATUS: <CODE>`).
2. Count occurrences of each status and output the sorted counts to `/var/tmp/status_summary.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d5-lfcs
```
