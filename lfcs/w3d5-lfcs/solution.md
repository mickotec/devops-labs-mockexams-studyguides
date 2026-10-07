# [LFCS W3D5-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Hardware report:
```bash
MEM=$(free -m | awk '/Mem:/ {print "RAM: "$2"MB"}')
CPU=$(lscpu | awk -F: '/CPU\(s\):/ {print "CPU Cores: "$2}' | head -1)
LOAD=$(awk '{print "Load Average: "$1", "$2", "$3}' /proc/loadavg)
echo "$MEM" > /var/tmp/system_specs.txt
echo "$CPU" >> /var/tmp/system_specs.txt
echo "$LOAD" >> /var/tmp/system_specs.txt
```

2. Tune swappiness:
`echo "vm.swappiness = 15" | sudo tee /etc/sysctl.d/99-swappiness.conf`
`sudo sysctl -p /etc/sysctl.d/99-swappiness.conf`
