# [LFCS W5D3-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Welcome template:
`echo "Corporate System Policy: All activity is monitored." | sudo tee /etc/skel/WELCOME.txt`
`sudo chmod 644 /etc/skel/WELCOME.txt`

2. Profile variable:
`echo 'export CORPORATE_ENV="production"' | sudo tee /etc/profile.d/corp_vars.sh`
`sudo chmod 644 /etc/profile.d/corp_vars.sh`

3. Limits:
`echo -e "student soft nofile 2048
student hard nofile 4096" | sudo tee /etc/security/limits.d/80-nofile.conf`
