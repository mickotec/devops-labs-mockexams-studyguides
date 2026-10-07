"""
Curriculum Content: Week 7 (Days 1 to 6)
Day 1: Cluster & Pod Networking Prerequisites | Linux Networking Configuration (IP & Routing)
Day 2: Service Networking & CoreDNS Deep Dive | Network Bonding & Bridging
Day 3: Ingress Controllers & Routing Rules | Packet Filtering with Firewalld & Iptables
Day 4: Gateway API (2025 Updates) | NAT, Port Redirection & Reverse Proxies
Day 5: Network Policies Deep Dive | SSH Hardening, Key Auth & Time Sync
Day 6: Week 7 Network Mastery Triathlon | Week 7 Linux Networking Marathon
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    # Day 1: Pod Networking & IP/Routing
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES FLAT POD NETWORK & CNI ARCHITECTURE", "Every Pod Receives a Unique, Routable IP (No NAT Between Pods)", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">NODE 1 (CIDR: 10.244.1.0/24)</text>
    <rect x="65" y="135" width="160" height="40" rx="4" fill="#065f46" stroke="#34d399"/>
    <text x="145" y="155" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" font-family="monospace">Pod A (10.244.1.15)</text>
    <text x="145" y="168" fill="#a7f3d0" font-size="7.5" text-anchor="middle" font-family="monospace">veth0 -> cbr0 / cni0</text>

    <rect x="245" y="135" width="160" height="40" rx="4" fill="#065f46" stroke="#34d399"/>
    <text x="325" y="155" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" font-family="monospace">Pod B (10.244.1.16)</text>
    <text x="325" y="168" fill="#a7f3d0" font-size="7.5" text-anchor="middle" font-family="monospace">veth1 -> cbr0 / cni0</text>
    <text x="235" y="205" fill="#e2e8f0" font-size="8.5" text-anchor="middle" font-family="sans-serif">Local bridge forwards traffic within node directly.</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">NODE 2 (CIDR: 10.244.2.0/24)</text>
    <rect x="570" y="135" width="160" height="40" rx="4" fill="#065f46" stroke="#34d399"/>
    <text x="650" y="155" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" font-family="monospace">Pod C (10.244.2.22)</text>
    <text x="650" y="168" fill="#a7f3d0" font-size="7.5" text-anchor="middle" font-family="monospace">veth0 -> cbr0 / cni0</text>

    <text x="650" y="195" fill="#38bdf8" font-size="8.5" text-anchor="middle" font-family="sans-serif">CNI Overlay Tunnel (VXLAN / Geneve / BGP)</text>
    <text x="650" y="210" fill="#94a3b8" font-size="8" text-anchor="middle" font-family="sans-serif">Pod A can reach Pod C without NAT via CNI plugin (Flannel/Calico)</text>
    """, "Figure 1.1: Kubernetes Flat Pod Networking Model & CNI Plugin Architecture")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX NETWORKING STACK: IP COMMAND & ROUTING TABLE", "Modern Iproute2 Architecture: ip link, ip addr, ip route", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">LINK LAYER (ip link)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">ip link show</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">ip link set eth0 up/down</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">ip link set mtu 1450 eth0</text>
    <text x="65" y="200" fill="#94a3b8" font-size="8" font-family="sans-serif">Physical / virtual interface status</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="440" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">ADDRESS LAYER (ip addr)</text>
    <text x="325" y="140" fill="#34d399" font-size="8.5" font-family="monospace">ip addr show dev eth0</text>
    <text x="325" y="160" fill="#34d399" font-size="8.5" font-family="monospace">ip addr add 192.168.1.50/24 \</text>
    <text x="325" y="175" fill="#34d399" font-size="8.5" font-family="monospace">  dev eth0</text>
    <text x="325" y="195" fill="#fde047" font-size="8.5" font-family="monospace">ip addr del ... dev eth0</text>
    <text x="325" y="210" fill="#94a3b8" font-size="8" font-family="sans-serif">Replaces deprecated ifconfig</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="720" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">ROUTING TABLE (ip route)</text>
    <text x="605" y="140" fill="#fde047" font-size="8.5" font-family="monospace">ip route show</text>
    <text x="605" y="160" fill="#fde047" font-size="8.5" font-family="monospace">ip route add default via \</text>
    <text x="605" y="175" fill="#fde047" font-size="8.5" font-family="monospace">  192.168.1.1 dev eth0</text>
    <text x="605" y="195" fill="#fde047" font-size="8.5" font-family="monospace">ip route add 10.0.0.0/8 via ...</text>
    <text x="605" y="210" fill="#a7f3d0" font-size="8" font-family="sans-serif">Directs egress IP packets</text>
    """, "Figure 1.2: Linux Iproute2 Network Configuration Architecture")

    cka_theory = """
    <p>
      Kubernetes networking mandates: All pods communicate with all other pods without NAT. All nodes communicate with all pods without NAT.
    </p>
    <ul>
      <li>CNI plugin config: <code>/etc/cni/net.d/</code>. If this directory is empty or contains an invalid config, the node reports <code>NotReady: NetworkPluginNotReady</code>!</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      The <code>iproute2</code> suite (<code>ip</code> command) replaces legacy <code>net-tools</code>.
    </p>
    <ul>
      <li>Configure persistent static IP via Netplan (<code>/etc/netplan/*.yaml</code>) or NetworkManager (<code>nmcli</code>).</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kcni='ls -la /etc/cni/net.d/'",
        "lfcs_aliases": "alias ipa='ip -br -c addr show'\nalias ipr='ip route show'",
        "checklist": [
            ("CKA", "Can you troubleshoot a Node in NotReady state due to missing CNI plugin?", "Inspect /etc/cni/net.d/ and kubelet logs"),
            ("LFCS", "Can you assign an IP address and default gateway using ip command?", "ip addr add and ip route add default via"),
        ]
    }

def get_day_2():
    # Day 2: Service Networking & Bonding/Bridging
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBE-PROXY MODES & SERVICE PACKET ROUTING", "IPTables vs IPVS Virtual IP Translation Engine", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">IPTABLES MODE (Sequential O(N) Rules)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">KUBE-SERVICES -> KUBE-SVC-XXX -> KUBE-SEP-YYY</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Random statistical DNAT load balancing.</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Translates Virtual ClusterIP to actual Pod IP.</text>
    <text x="65" y="200" fill="#fde047" font-size="8.5" font-family="monospace">sudo iptables -t nat -L KUBE-SERVICES -n -v</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">IPVS MODE (Hash Tables O(1) Routing)</text>
    <text x="465" y="140" fill="#34d399" font-size="8.5" font-family="monospace">ipvsadm -ln  # Inspect virtual servers</text>
    <text x="465" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• High-performance for large clusters (10k+ services).</text>
    <text x="465" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Advanced load balancing: round-robin, least-connection.</text>
    <text x="465" y="200" fill="#a7f3d0" font-size="8.5" font-family="monospace">mode: "ipvs" in kube-proxy ConfigMap</text>
    """, "Figure 2.1: Kubernetes Kube-Proxy Modes: IPTables vs IPVS Virtual Routing")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX LINK AGGREGATION: BONDING VS BRIDGING", "High Availability / Bandwidth Aggregation vs Virtual Switch", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">NETWORK BONDING (Link Aggregation)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Combines 2+ physical NICs into <code>bond0</code></text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">Mode 1 (active-backup): High availability failover</text>
    <text x="65" y="178" fill="#4ade80" font-size="8.5" font-family="monospace">Mode 4 (802.3ad LACP): Aggregates throughput</text>
    <text x="65" y="196" fill="#fde047" font-size="8.5" font-family="monospace">/proc/net/bonding/bond0  # Check status</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">LINUX SOFTWARE BRIDGE (br0)</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">ip link add br0 type bridge &amp;&amp; ip link set br0 up</text>
    <text x="465" y="160" fill="#fde047" font-size="8.5" font-family="monospace">ip link set eth1 master br0</text>
    <text x="465" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Acts as an internal software L2 network switch.</text>
    <text x="465" y="200" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Bridges VMs (KVM/QEMU) and containers onto host network.</text>
    """, "Figure 2.2: Linux Network Bonding Modes & Software Bridge Architecture")

    cka_theory = """
    <p>
      <code>kube-proxy</code> runs on each node and programs netfilter (iptables or IPVS) rules to intercept ClusterIP connections and forward them to backend Pods.
    </p>
    """

    lfcs_theory = """
    <p>
      Network bonding provides hardware redundancy. Software bridges (<code>br0</code>) connect virtual guests directly to physical networks.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kproxy='kubectl logs -n kube-system -l k8s-app=kube-proxy'",
        "lfcs_aliases": "alias bondstatus='cat /proc/net/bonding/bond0 2>/dev/null'",
        "checklist": [
            ("CKA", "Can you inspect kube-proxy configuration and mode in kube-system?", "kubectl get cm -n kube-system kube-proxy -o yaml"),
            ("LFCS", "Can you create a Linux bridge interface and attach a physical port?", "ip link add br0 type bridge && ip link set dev master br0"),
        ]
    }

def get_day_3():
    # Day 3: Ingress & Firewalld/Iptables
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "INGRESS CONTROLLER & PATH ROUTING ARCHITECTURE", "Edge Layer 7 Routing: Hosts, TLS & Context Paths", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">INGRESS RESOURCE</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">spec.ingressClassName: nginx</text>
    <text x="65" y="160" fill="#fde047" font-size="8.5" font-family="monospace">host: shop.example.com</text>
    <text x="65" y="180" fill="#34d399" font-size="8.5" font-family="monospace">path: /api -> svc: api-svc:8080</text>
    <text x="65" y="200" fill="#34d399" font-size="8.5" font-family="monospace">path: /    -> svc: web-svc:80</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="440" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">INGRESS CONTROLLER (Nginx)</text>
    <text x="325" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Reverse proxy pod running in cluster</text>
    <text x="325" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Dynamically updates nginx.conf</text>
    <text x="325" y="180" fill="#fde047" font-size="8.5" font-family="monospace">tls: [{{hosts: [...], secretName: ...}}]</text>
    <text x="325" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Terminates TLS with Secret cert</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">BACKEND SERVICES</text>
    <text x="605" y="140" fill="#34d399" font-size="8.5" font-family="monospace">api-svc (ClusterIP: 10.96.2.14)</text>
    <text x="605" y="160" fill="#94a3b8" font-size="8" font-family="sans-serif">-> Pods: api-1, api-2</text>
    <text x="605" y="180" fill="#34d399" font-size="8.5" font-family="monospace">web-svc (ClusterIP: 10.96.8.99)</text>
    <text x="605" y="200" fill="#94a3b8" font-size="8" font-family="sans-serif">-> Pods: web-1, web-2, web-3</text>
    """, "Figure 3.1: Kubernetes Ingress Controller HTTP/HTTPS Traffic Routing Topology")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX PACKET FILTERING: FIREWALLD & IPTABLES", "Zone-Based Security Architecture & Netfilter Tables", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">FIREWALLD (Zone-Based Management)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">firewall-cmd --get-active-zones</text>
    <text x="65" y="158" fill="#4ade80" font-size="8.5" font-family="monospace">firewall-cmd --zone=public --add-port=80/tcp --permanent</text>
    <text x="65" y="176" fill="#4ade80" font-size="8.5" font-family="monospace">firewall-cmd --add-service=https --permanent</text>
    <text x="65" y="194" fill="#fde047" font-size="8.5" font-family="monospace">firewall-cmd --reload  # Apply permanent rules!</text>
    <text x="65" y="210" fill="#fca5a5" font-size="8" font-family="sans-serif">Without --permanent, rules disappear on reload!</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">IPTABLES (Netfilter Chains)</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">iptables -L -n -v    # List all rules</text>
    <text x="465" y="158" fill="#fde047" font-size="8.5" font-family="monospace">iptables -A INPUT -p tcp --dport 22 -j ACCEPT</text>
    <text x="465" y="176" fill="#fca5a5" font-size="8.5" font-family="monospace">iptables -A INPUT -p tcp --dport 80 -j DROP</text>
    <text x="465" y="194" fill="#e2e8f0" font-size="8.5" font-family="monospace">iptables -P INPUT DROP  # Default policy</text>
    <text x="465" y="210" fill="#a7f3d0" font-size="8" font-family="monospace">sudo netfilter-persistent save (Debian)</text>
    """, "Figure 3.2: Linux Packet Filtering Architecture: Firewalld vs Iptables")

    cka_theory = """
    <p>
      An Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster.
    </p>
    <ul>
      <li>Create Ingress imperatively: <code>kubectl create ingress my-ing --rule="host/path=service:port"</code></li>
      <li>Path types: <code>Prefix</code> (matches URL prefixes) or <code>Exact</code> (strict path matching).</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Linux firewalls manage network traffic entering or leaving the system.
    </p>
    <ul>
      <li>In <code>firewalld</code>: Always test with <code>--permanent</code> and then execute <code>firewall-cmd --reload</code>.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias king='kubectl get ingress'",
        "lfcs_aliases": "alias fw='sudo firewall-cmd'",
        "checklist": [
            ("CKA", "Can you configure an Ingress with path-based routing to multiple services?", "spec.rules.http.paths"),
            ("LFCS", "Can you open a port permanently in firewalld and reload?", "firewall-cmd --add-port=... --permanent && reload"),
        ]
    }

def get_day_4():
    # Day 4: Gateway API & NAT/Proxies
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES GATEWAY API HIERARCHY", "GatewayClass (Infra) -> Gateway (Cluster Admin) -> HTTPRoute (App Dev)", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">GATEWAYCLASS (Infra Provider)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">kind: GatewayClass</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Managed by cloud/infra team</text>
    <text x="65" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Defines controller implementation</text>
    <text x="65" y="200" fill="#a7f3d0" font-size="8.5" font-family="monospace">controllerName: example.com/gateway</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="440" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">GATEWAY (Cluster Admin)</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">kind: Gateway</text>
    <text x="325" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Defines listeners: port, protocol</text>
    <text x="325" y="180" fill="#fde047" font-size="8.5" font-family="monospace">listeners: [{{port: 80, protocol: HTTP}}]</text>
    <text x="325" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Binds to GatewayClass</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">HTTPROUTE (Application Dev)</text>
    <text x="605" y="140" fill="#34d399" font-size="8.5" font-family="monospace">kind: HTTPRoute</text>
    <text x="605" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Attaches to parent Gateway</text>
    <text x="605" y="180" fill="#34d399" font-size="8.5" font-family="monospace">parentRefs: [{{name: prod-gateway}}]</text>
    <text x="605" y="205" fill="#4ade80" font-size="8.5" font-family="monospace">backendRefs: [{{name: web, port: 80}}]</text>
    """, "Figure 4.1: Kubernetes Gateway API Role-Oriented Architecture")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "NETWORK ADDRESS TRANSLATION: SNAT & DNAT (PORT FORWARDING)", "Netfilter Nat Table: PREROUTING vs POSTROUTING Chains", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">DNAT (Port Forwarding: PREROUTING)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">iptables -t nat -A PREROUTING -p tcp --dport 8080 \</text>
    <text x="65" y="155" fill="#4ade80" font-size="8.5" font-family="monospace">  -j DNAT --to-destination 192.168.1.50:80</text>
    <text x="65" y="175" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Redirects external port to internal server</text>
    <text x="65" y="195" fill="#fde047" font-size="8.5" font-family="monospace">firewall-cmd --add-forward-port=port=8080:proto=tcp:toport=80</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SNAT / MASQUERADE (Egress Gateway)</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE</text>
    <text x="465" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Allows internal private network to access the Internet</text>
    <text x="465" y="180" fill="#fde047" font-size="8.5" font-family="monospace">firewall-cmd --zone=public --add-masquerade --permanent</text>
    <text x="465" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Requires <code>net.ipv4.ip_forward = 1</code> in sysctl!</text>
    """, "Figure 4.2: Linux NAT Architecture: Port Forwarding (DNAT) & Masquerading (SNAT)")

    cka_theory = """
    <p>
      The Gateway API is the modern successor to Ingress, providing role-oriented networking resources (GatewayClass, Gateway, HTTPRoute, GRPCRoute).
    </p>
    """

    lfcs_theory = """
    <p>
      Network Address Translation alters packet headers in transit. DNAT forwards incoming ports; SNAT/MASQUERADE masks outgoing local network traffic.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kgw='kubectl get gateways,httproutes'",
        "lfcs_aliases": "alias natrules='sudo iptables -t nat -L -n -v'",
        "checklist": [
            ("CKA", "Can you explain the difference between Gateway and HTTPRoute in Gateway API?", "Gateway defines entry point; HTTPRoute binds paths"),
            ("LFCS", "Can you configure port forwarding in firewalld or iptables?", "firewall-cmd --add-forward-port"),
        ]
    }

def get_day_5():
    # Day 5: Network Policies & SSH Hardening
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES NETWORK POLICY FILTERING ENGINE", "Ingress & Egress Microsegmentation (Default Deny vs Selectors)", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="235" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">DEFAULT DENY INGRESS</text>
    <text x="65" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">spec:</text>
    <text x="75" y="155" fill="#fca5a5" font-size="8.5" font-family="monospace">  podSelector: {{}}   # Selects ALL pods in namespace</text>
    <text x="75" y="170" fill="#fca5a5" font-size="8.5" font-family="monospace">  policyTypes: [Ingress]</text>
    <text x="65" y="190" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Isolates all pods in the namespace.</text>
    <text x="65" y="205" fill="#4ade80" font-size="8.5" font-family="sans-serif">• All inbound traffic blocked until explicitly allowed!</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SELECTIVE ALLOW RULE</text>
    <text x="465" y="140" fill="#34d399" font-size="8.5" font-family="monospace">ingress:</text>
    <text x="475" y="155" fill="#34d399" font-size="8.5" font-family="monospace">- from:</text>
    <text x="485" y="170" fill="#34d399" font-size="8.5" font-family="monospace">  - podSelector: {{matchLabels: {{role: frontend}}}}</text>
    <text x="475" y="185" fill="#34d399" font-size="8.5" font-family="monospace">  ports: [{{protocol: TCP, port: 5432}}]</text>
    <text x="465" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Only pods with <code>role=frontend</code> can reach port 5432!</text>
    """, "Figure 5.1: Kubernetes NetworkPolicy Packet Filtering Architecture")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "OPENSSH HARDENING & CHRONY TIME SYNCHRONIZATION", "Server Security (/etc/ssh/sshd_config) & NTP Sync", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="235" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SSH HARDENING (/etc/ssh/sshd_config)</text>
    <text x="65" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">PermitRootLogin no</text>
    <text x="65" y="155" fill="#fca5a5" font-size="8.5" font-family="monospace">PasswordAuthentication no</text>
    <text x="65" y="170" fill="#4ade80" font-size="8.5" font-family="monospace">PubkeyAuthentication yes</text>
    <text x="65" y="185" fill="#4ade80" font-size="8.5" font-family="monospace">Port 2222</text>
    <text x="65" y="205" fill="#fde047" font-size="8.5" font-family="monospace">sudo sshd -t &amp;&amp; sudo systemctl restart sshd</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">CHRONY NTP TIME SYNCHRONIZATION</text>
    <text x="465" y="140" fill="#34d399" font-size="8.5" font-family="monospace">chronyc sources -v    # Query NTP time servers</text>
    <text x="465" y="160" fill="#34d399" font-size="8.5" font-family="monospace">chronyc tracking      # Check clock offset &amp; drift</text>
    <text x="465" y="180" fill="#34d399" font-size="8.5" font-family="monospace">chronyc makestep      # Force immediate clock sync</text>
    <text x="465" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Config: /etc/chrony/chrony.conf (Debian) or /etc/chrony.conf (RHEL)</text>
    """, "Figure 5.2: OpenSSH Security Hardening & Chrony NTP Clock Sync")

    cka_theory = """
    <p>
      By default, all pods in Kubernetes can talk to all other pods. <strong>NetworkPolicies</strong> enforce microsegmentation.
    </p>
    <ul>
      <li>NetworkPolicies require a CNI plugin that supports policy enforcement (e.g. Calico, Cilium). Flannel alone does NOT enforce NetworkPolicies!</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      System security mandates hardening SSH (disabling root login and enforcing public key auth) and keeping clocks synchronized via Chrony.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias knp='kubectl get netpol'",
        "lfcs_aliases": "alias ntpcheck='chronyc tracking'",
        "checklist": [
            ("CKA", "Can you write a NetworkPolicy that restricts pod ingress to specific pods on a specific port?", "NetworkPolicy with podSelector and ports"),
            ("LFCS", "Can you harden sshd_config and test syntax with sshd -t?", "PermitRootLogin no && sshd -t"),
            ("LFCS", "Can you check NTP synchronization status with chronyc?", "chronyc sources -v"),
        ]
    }

def get_day_6():
    # Day 6: Network Triathlon & Marathon
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "WEEK 7 NETWORK MASTERY TRIATHLON TOPOLOGY", "Multi-Tier Isolation: Ingress -> Frontend -> Backend (Isolated) -> Database", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="60" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="140" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Ingress Edge</text>
    <text x="140" y="135" fill="#93c5fd" font-size="8.5" text-anchor="middle" font-family="monospace">TLS / Path Routing</text>

    <rect x="260" y="90" width="180" height="60" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="350" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Frontend Pods</text>
    <text x="350" y="135" fill="#a7f3d0" font-size="8.5" text-anchor="middle" font-family="monospace">Accessible via Ingress</text>

    <rect x="470" y="90" width="180" height="60" rx="6" fill="#78350f" stroke="#fbbf24"/>
    <text x="560" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Backend API</text>
    <text x="560" y="135" fill="#fef3c7" font-size="8.5" text-anchor="middle" font-family="monospace">NetPol: Allow Frontend</text>

    <rect x="680" y="90" width="170" height="60" rx="6" fill="#881337" stroke="#f43f5e"/>
    <text x="765" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Database Tier</text>
    <text x="765" y="135" fill="#fca5a5" font-size="8.5" text-anchor="middle" font-family="monospace">Default Deny Ingress</text>

    {code_box(50, 160, 800, 65, "Triathlon Network Stack:\n1. Ingress routes traffic to frontend service\n2. Backend accepts traffic ONLY from pods with role=frontend\n3. Database accepts traffic ONLY from backend on port 5432")}
    """, "Figure 6.1: Multi-Tier Network Segmentation & Policy Topology")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "WEEK 7 LINUX NETWORKING & FIREWALL MARATHON", "Defense in Depth: Interface -> Routing -> NAT -> Firewalld -> SSH", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">INTERFACE &amp; ROUTE</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">ip addr add ... dev eth0</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">ip route add default ...</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">DNS: /etc/resolv.conf</text>
    <text x="65" y="205" fill="#a7f3d0" font-size="8.5" font-family="monospace">ping -c 3 8.8.8.8</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">FIREWALL RULES</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">firewall-cmd --add-service=ssh</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">firewall-cmd --add-port=443/tcp</text>
    <text x="325" y="180" fill="#fde047" font-size="8.5" font-family="monospace">firewall-cmd --add-masquerade</text>
    <text x="325" y="205" fill="#34d399" font-size="8.5" font-family="monospace">firewall-cmd --runtime-to-permanent</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SSH &amp; AUDIT</text>
    <text x="595" y="140" fill="#34d399" font-size="8.5" font-family="monospace">ss -tulpn  # Check open listening ports</text>
    <text x="595" y="160" fill="#34d399" font-size="8.5" font-family="monospace">tcpdump -nn -i eth0 port 80</text>
    <text x="595" y="180" fill="#34d399" font-size="8.5" font-family="monospace">traceroute 1.1.1.1</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Complete network verification</text>
    """, "Figure 6.2: Linux Network Defense in Depth & Diagnostic Verification")

    cka_theory = """
    <p>
      Week 7 consolidation tests complete cluster networking: CNI verification, Ingress path routing, CoreDNS resolution, and microsegmentation using NetworkPolicies.
    </p>
    """

    lfcs_theory = """
    <p>
      Week 7 consolidation evaluates end-to-end Linux network configuration: IP addressing, routing, bonding, firewall packet filtering, port forwarding, and SSH security.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias knet='kubectl get netpol,svc,ing'",
        "lfcs_aliases": "alias ports='ss -tulpn'",
        "checklist": [
            ("CKA", "Can you construct an end-to-end multi-tier network policy in under 5 minutes?", "Default deny with explicit allows"),
            ("LFCS", "Can you inspect listening sockets and trace routes to an external host?", "ss -tulpn && traceroute"),
        ]
    }

def get_day_content(day: int) -> dict:
    dispatch = {
        1: get_day_1,
        2: get_day_2,
        3: get_day_3,
        4: get_day_4,
        5: get_day_5,
        6: get_day_6,
    }
    return dispatch.get(day, get_day_1)()
