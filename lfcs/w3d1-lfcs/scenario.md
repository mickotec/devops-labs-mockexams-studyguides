# [LFCS W3D1-LFCS] Linux Boot Architecture & GRUB2

**Date:** 2026-10-12  
**Time Limit:** 35m  
**Difficulty:** Medium  
**Target:** VirtualBox Ubuntu VM (`LFCS`) / Linux Terminal  

---

## 📋 Scenario Overview
Practice scenario aligned with your official certification preparation schedule. Complete all tasks under exam conditions.

---

## 🎯 Candidate Tasks

### Task 1: GRUB Configuration Tuning
1. In `/etc/default/grub`, modify `GRUB_CMDLINE_LINUX_DEFAULT` to append the kernel boot parameter `consoleblank=600`.
2. Change the default boot timeout (`GRUB_TIMEOUT`) to `8` seconds.
3. Run `sudo update-grub` to regenerate `/boot/grub/grub.cfg`.

### Task 2: System Boot Diagnostic Report
Extract boot diagnostics to `/var/tmp/boot_diagnostic.txt`:
1. Use `dmesg` or `journalctl -b` to find the kernel command-line arguments used during current boot and save the line containing `Command line:` or `Kernel command line:` as the first line of `/var/tmp/boot_diagnostic.txt`.
2. Append the UUID of the root filesystem mounted at `/` (use `findmnt` or `lsblk`).

---

## 🔍 Validation
Run the automated grader:
```bash
./lab check w3d1-lfcs
```
