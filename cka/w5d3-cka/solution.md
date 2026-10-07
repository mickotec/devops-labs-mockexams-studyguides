# [CKA W5D3-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Drain node01 and save output:
`kubectl drain node01 --ignore-daemonsets --delete-emptydir-data --force | sudo tee /opt/k8s/node01_drain.txt`

2. Check kubelet on node01:
`ssh node01 'sudo systemctl status kubelet'`

3. Uncordon:
`kubectl uncordon node01`
