# [LFCS W2D4-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Stream separation:
```bash
find /etc -name "*shadow*" 1> /var/tmp/stdout.log 2> /var/tmp/stderr.log
```

2. Process tee pipeline:
```bash
ps -ef | tee /var/tmp/process_dump.txt | wc -l > /var/tmp/process_count.txt
```

3. Health script with heredoc:
```bash
cat << 'EOF' > /var/tmp/gen_health.sh
#!/usr/bin/env bash
cat << 'REPORT' > /var/tmp/health.report
HOST: $(hostname)
KERNEL: $(uname -r)
REPORT
EOF
chmod +x /var/tmp/gen_health.sh
bash /var/tmp/gen_health.sh
```
