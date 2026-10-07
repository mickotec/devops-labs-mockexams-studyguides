# [LFCS W5D1-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create user:
`sudo useradd -u 1600 -m -s /bin/bash -c "DevOps Service Account" devops_user`

2. Set aging:
`sudo chage -E 2027-12-31 -M 90 -W 7 devops_user`

3. Lock account:
`sudo passwd -l test_lock_user`
