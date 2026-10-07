# [LFCS W3D4-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Kill rogue process:
`killall -15 rogue-sim || killall -9 rogue-sim`

2. Renice batch-calc:
`renice -n 12 -p $(pgrep -f batch-calc)`

3. Top 5 memory processes:
`ps -eo pid,user,%mem,command --sort=-%mem | head -n 6 > /var/tmp/process_report.txt`
