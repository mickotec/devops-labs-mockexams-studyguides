# [LFCS W1D1-LFCS] Consoles, Navigation & System Documentation

**Date:** 2026-09-14  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Documentation Discovery & Querying
1. Use `apropos` (or `man -k`) to search for all manual pages discussing:
   - "partition table"
   - "password file"
2. Save the formatted list of matches to `/var/tmp/lfcs-doc-search.txt`.
3. Locate the manual page for the configuration file format of `/etc/passwd` (man section 5). Extract the field definitions and append them to `/var/tmp/lfcs-passwd-fields.txt`.

### Task 2: Advanced Directory Navigation Speed Drills
1. Write a shell function or commands in `/var/tmp/lfcs-nav.sh` demonstrating:
   - Creating a nested directory tree `/var/tmp/lfcs/a/b/c/d/e` in a single command (`mkdir -p`).
   - Pushing the current directory to the directory stack (`pushd`), creating `evidence.txt` inside `/var/tmp/lfcs/a/b/c/d/e/`, and returning with `popd`.
2. Execute the script and ensure `/var/tmp/lfcs/a/b/c/d/e/evidence.txt` exists.

### Task 3: Build a Command Synopsis Extractor (`quickman`)
1. Create an executable bash script `/usr/local/bin/quickman` (permissions `755`):
   - It accepts one argument: the command name (e.g. `quickman tar`).
   - If no argument is passed, exit with code 1 and message: `Usage: quickman <command>`.
   - It extracts and outputs **only** the `NAME` and `SYNOPSIS` sections from the target command's man page without any interactive pager pause (plain text output).
2. Test that running `quickman useradd` prints only the Name and Synopsis cleanly.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w1d1-lfcs
```
