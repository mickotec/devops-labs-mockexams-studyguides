# [LFCS W7D2-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Create bridge br0:
`sudo ip link add br0 type bridge`
`sudo ip addr add 192.168.100.1/24 dev br0`
`sudo ip link set br0 up`

2. Create veth pair:
`sudo ip link add veth-host type veth peer name veth-guest`

3. Attach to bridge and bring up:
`sudo ip link set veth-host master br0`
`sudo ip link set veth-host up`
`sudo ip link set veth-guest up`
