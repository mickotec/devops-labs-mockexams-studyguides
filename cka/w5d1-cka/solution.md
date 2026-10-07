# [CKA W5D1-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Cordon:
`kubectl cordon node02`

2. Drain:
`kubectl drain node02 --ignore-daemonsets --delete-emptydir-data --force`

3. Uncordon:
`kubectl uncordon node02`
