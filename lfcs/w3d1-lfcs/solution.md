# [LFCS W3D1-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Edit `/etc/default/grub`:
Set `GRUB_TIMEOUT=8`
Update `GRUB_CMDLINE_LINUX_DEFAULT="... consoleblank=600"`
Run: `sudo update-grub`

2. Generate report:
`journalctl -b -k | grep -m1 -E "Command line|BOOT_IMAGE" > /var/tmp/boot_diagnostic.txt`
`findmnt / -no UUID | awk '{print "UUID="$1}' >> /var/tmp/boot_diagnostic.txt`
