# [LFCS W2D5-LFCS] Archiving, Compression & Remote Backups

**Date:** 2026-10-09  
**Time Limit:** 30m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: Gzip Compressed Tar Archive
Create a compressed tar archive of `/etc/systemd/` saved to `/var/tmp/systemd_backup.tar.gz`. Preserve all file permissions (`-p`).

### Task 2: Extract to Alternate Target
Extract `/var/tmp/systemd_backup.tar.gz` into directory `/var/tmp/extracted_systemd/` without changing your current directory.

### Task 3: Tarball Content Verification
List the table of contents of `/var/tmp/systemd_backup.tar.gz` (`-tzf`) and save the file list to `/var/tmp/archive_manifest.txt`.

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w2d5-lfcs
```
