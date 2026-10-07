# [LFCS W4D3-LFCS] Package Managers (APT, DNF/YUM & RPM)

**Date:** 2026-10-21  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Package Version & File Query
Find which package owns `/usr/bin/tar` and record the package name and installed version into `/var/tmp/tar_package.txt` (use `dpkg -S` and `dpkg -l` or `apt-cache policy`).

### Task 2: Pin Package Version with apt-mark
Place a package hold on `tar` to prevent it from being upgraded during automated system upgrades.
- Confirm with `apt-mark showhold`.

### Task 3: Download Debian Package Archive Without Installing
Download the `.deb` package file for `tree` into directory `/var/tmp/pkg_cache/` using `apt-get download`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w4d3-lfcs
```
