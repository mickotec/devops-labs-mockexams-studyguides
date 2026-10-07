"""
LFCS Curriculum Content: Week 7 (Days 1 to 6)
Day 1: Linux Networking Configuration (IP & Routing)
Day 2: Network Bonding & Bridging
Day 3: Packet Filtering with Firewalld & Iptables
Day 4: NAT, Port Redirection & Reverse Proxies
Day 5: SSH Hardening, Key Auth & Time Sync
Day 6: Week 7 Linux Networking Marathon
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <p>
      The <code>iproute2</code> suite (<code>ip</code> command) replaces legacy <code>net-tools</code>.
    </p>
    <ul>
      <li>Configure persistent static IP via Netplan (<code>/etc/netplan/*.yaml</code>) or NetworkManager (<code>nmcli</code>).</li>
    </ul>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 1.2: Linux Iproute2 Network Configuration Architecture</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LINUX NETWORKING STACK: IP COMMAND & ROUTING TABLE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Modern Iproute2 Architecture: ip link, ip addr, ip route</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias ipa='ip -br -c addr show'
alias ipr='ip route show'"""
    checklist = [('LFCS', 'Can you assign an IP address and default gateway using ip command?', 'ip addr add and ip route add default via')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "lfcs_theory_html": theory,
        "lfcs_svg": svg,
        "lfcs_aliases": aliases,
    }

def get_day_2():
    theory = """
    <p>
      Network bonding provides hardware redundancy. Software bridges (<code>br0</code>) connect virtual guests directly to physical networks.
    </p>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 2.2: Linux Network Bonding Modes & Software Bridge Architecture</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LINUX LINK AGGREGATION: BONDING VS BRIDGING</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">High Availability / Bandwidth Aggregation vs Virtual Switch</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias bondstatus='cat /proc/net/bonding/bond0 2>/dev/null'"""
    checklist = [('LFCS', 'Can you create a Linux bridge interface and attach a physical port?', 'ip link add br0 type bridge && ip link set dev master br0')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "lfcs_theory_html": theory,
        "lfcs_svg": svg,
        "lfcs_aliases": aliases,
    }

def get_day_3():
    theory = """
    <p>
      Linux firewalls manage network traffic entering or leaving the system.
    </p>
    <ul>
      <li>In <code>firewalld</code>: Always test with <code>--permanent</code> and then execute <code>firewall-cmd --reload</code>.</li>
    </ul>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 3.2: Linux Packet Filtering Architecture: Firewalld vs Iptables</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LINUX PACKET FILTERING: FIREWALLD & IPTABLES</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Zone-Based Security Architecture & Netfilter Tables</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias fw='sudo firewall-cmd'"""
    checklist = [('LFCS', 'Can you open a port permanently in firewalld and reload?', 'firewall-cmd --add-port=... --permanent && reload')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "lfcs_theory_html": theory,
        "lfcs_svg": svg,
        "lfcs_aliases": aliases,
    }

def get_day_4():
    theory = """
    <p>
      Network Address Translation alters packet headers in transit. DNAT forwards incoming ports; SNAT/MASQUERADE masks outgoing local network traffic.
    </p>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 4.2: Linux NAT Architecture: Port Forwarding (DNAT) & Masquerading (SNAT)</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">NETWORK ADDRESS TRANSLATION: SNAT & DNAT (PORT FORWARDING)</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Netfilter Nat Table: PREROUTING vs POSTROUTING Chains</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias natrules='sudo iptables -t nat -L -n -v'"""
    checklist = [('LFCS', 'Can you configure port forwarding in firewalld or iptables?', 'firewall-cmd --add-forward-port')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "lfcs_theory_html": theory,
        "lfcs_svg": svg,
        "lfcs_aliases": aliases,
    }

def get_day_5():
    theory = """
    <p>
      System security mandates hardening SSH (disabling root login and enforcing public key auth) and keeping clocks synchronized via Chrony.
    </p>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 5.2: OpenSSH Security Hardening & Chrony NTP Clock Sync</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">OPENSSH HARDENING & CHRONY TIME SYNCHRONIZATION</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Server Security (/etc/ssh/sshd_config) & NTP Sync</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias ntpcheck='chronyc tracking'"""
    checklist = [('LFCS', 'Can you harden sshd_config and test syntax with sshd -t?', 'PermitRootLogin no && sshd -t'), ('LFCS', 'Can you check NTP synchronization status with chronyc?', 'chronyc sources -v')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "lfcs_theory_html": theory,
        "lfcs_svg": svg,
        "lfcs_aliases": aliases,
    }

def get_day_6():
    theory = """
    <p>
      Week 7 consolidation evaluates end-to-end Linux network configuration: IP addressing, routing, bonding, firewall packet filtering, port forwarding, and SSH security.
    </p>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 6.2: Linux Network Defense in Depth & Diagnostic Verification</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">WEEK 7 LINUX NETWORKING & FIREWALL MARATHON</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Defense in Depth: Interface -> Routing -> NAT -> Firewalld -> SSH</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias ports='ss -tulpn'"""
    checklist = [('LFCS', 'Can you inspect listening sockets and trace routes to an external host?', 'ss -tulpn && traceroute')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "lfcs_theory_html": theory,
        "lfcs_svg": svg,
        "lfcs_aliases": aliases,
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
