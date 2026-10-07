# [LFCS W5D2-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Group & user:
`sudo groupadd -g 2800 sysaudit`
`sudo usermod -aG sysaudit student`

2. Sudoers file:
`echo "%sysaudit ALL=(ALL) NOPASSWD: /usr/bin/journalctl" | sudo tee /etc/sudoers.d/90-sysaudit`
`sudo chmod 0440 /etc/sudoers.d/90-sysaudit`
`sudo visudo -cf /etc/sudoers.d/90-sysaudit`
