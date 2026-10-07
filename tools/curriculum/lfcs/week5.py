"""
LFCS Curriculum Content: Week 5 (Days 1 to 6)
Day 1: Local User Management & /etc/passwd
Day 2: Groups, Sudo Privileges & Visudo
Day 3: Profiles, Templates & User Limits
Day 4: Kernel Runtime Tuning with Sysctl
Day 5: Mandatory Access Control: SELinux & AppArmor
Day 6: Security Audit, Quarantine & Recovery
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <p>
      User administration is governed by <code>/etc/passwd</code>, <code>/etc/shadow</code>, and <code>/etc/default/useradd</code>.
    </p>
    <ul>
      <li>Default skeleton files are copied from <code>/etc/skel</code> when <code>-m</code> is used with <code>useradd</code>.</li>
      <li>To lock an account: <code>usermod -L &lt;user&gt;</code> or <code>passwd -l &lt;user&gt;</code>.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 1.2: Linux User Account Architecture & /etc/passwd Structure</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LINUX USER ACCOUNT ARCHITECTURE & /ETC/PASSWD STRUCTURE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">User Identity, Shell Configuration & Password Hashes</text>
    </g>
    
    <rect x="50" y="90" width="450" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="275" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">/etc/passwd SEVEN FIELDS COLUMNS</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">micko : x : 1000 : 1000 : Micko Dev :/home/micko : /bin/bash</text>
    <text x="65" y="155" fill="#fde047" font-size="8" font-family="monospace">  1     2    3      4        5           6           7</text>
    <text x="65" y="170" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">1: Username | 2: Password marker ('x') | 3: UID | 4: GID</text>
    <text x="65" y="188" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">5: GECOS (User info) | 6: Home Directory | 7: Login Shell</text>
    <text x="65" y="208" fill="#fca5a5" font-size="8.5" font-family="monospace">/sbin/nologin or /bin/false (Disable login)</text>

    <rect x="520" y="90" width="330" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="685" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">USER MANAGEMENT COMMANDS</text>
    <text x="535" y="140" fill="#fde047" font-size="8.5" font-family="monospace">useradd -m -s /bin/bash -u 1500 bob</text>
    <text x="535" y="158" fill="#fde047" font-size="8.5" font-family="monospace">usermod -aG sudo,docker bob</text>
    <text x="535" y="176" fill="#fde047" font-size="8.5" font-family="monospace">passwd -l bob  # Lock account</text>
    <text x="535" y="194" fill="#fde047" font-size="8.5" font-family="monospace">userdel -r bob # Delete with home</text>
    <text x="535" y="210" fill="#34d399" font-size="8.5" font-family="monospace">chage -l bob   # Password expiry</text>
    
</svg>"""
    aliases = """alias ulist='cut -d: -f1,3 /etc/passwd | sort -t: -k2 -n'"""
    checklist = [('LFCS', 'Can you create a user with specific UID, home directory, and bash shell?', 'useradd -u 1200 -m -s /bin/bash <user>'), ('LFCS', 'Can you lock a user account and verify its status in /etc/shadow?', 'passwd -l <user> && grep <user> /etc/shadow')]
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
      The <code>sudoers</code> file governs root delegation.
    </p>
    <ul>
      <li>Always use <code>visudo</code> to prevent locking root out with a syntax typo.</li>
      <li>Drop-in files: <code>/etc/sudoers.d/&lt;filename&gt;</code> must not end in <code>~</code> or contain <code>.</code> in some distros, and must be mode <code>0440</code>.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 2.2: Linux Sudoers Privilege Architecture & Visudo Verification</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LINUX SUDO PRIVILEGES & /ETC/SUDOERS GRAMMAR</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Privilege Escalation Rules & Visudo Syntax Verification</text>
    </g>
    
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SUDOERS SYNTAX (who where=(as_whom) what)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">root    ALL=(ALL:ALL) ALL</text>
    <text x="65" y="158" fill="#4ade80" font-size="8.8" font-family="monospace">%sudo   ALL=(ALL:ALL) ALL</text>
    <text x="65" y="176" fill="#fde047" font-size="8.8" font-family="monospace">alice   ALL=(ALL) NOPASSWD: /bin/systemctl</text>
    <text x="65" y="194" fill="#fde047" font-size="8.8" font-family="monospace">%devops ALL=(root) /usr/bin/apt, /usr/bin/git</text>
    <text x="65" y="210" fill="#e2e8f0" font-size="8" font-family="sans-serif">% prefix indicates group rule</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">VISUDO SAFETY &amp; DROP-INS</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">sudo visudo</text>
    <text x="465" y="158" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Locks file and verifies syntax before saving.</text>
    <text x="465" y="176" fill="#fde047" font-size="8.5" font-family="monospace">sudo visudo -f /etc/sudoers.d/developers</text>
    <text x="465" y="194" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Drop-in files in <code>/etc/sudoers.d/</code> must have <code>0440</code> permissions!</text>
    <text x="465" y="210" fill="#fca5a5" font-size="8" font-family="sans-serif">Never edit /etc/sudoers with raw vim or nano!</text>
    
</svg>"""
    aliases = """alias vs='sudo visudo -f /etc/sudoers.d/custom'"""
    checklist = [('LFCS', 'Can you configure passwordless sudo for a specific command?', 'user ALL=(ALL) NOPASSWD: /path/to/binary in visudo')]
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
      Process and file descriptor limits prevent fork bombs and file table exhaustion.
    </p>
    <ul>
      <li>Soft limits: Can be modified by user up to hard limit.</li>
      <li>Hard limits: Upper ceiling enforceable by PAM.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 3.2: Linux Resource Limits & PAM Security Configuration</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">USER RESOURCE LIMITS & PAM CONFIGURATION</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Security Limits: /etc/security/limits.conf & ulimit</text>
    </g>
    
    <rect x="50" y="90" width="450" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="275" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">/etc/security/limits.conf COLUMNS</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">domain    type    item         value</text>
    <text x="65" y="158" fill="#fde047" font-size="8.5" font-family="monospace">*         soft    nofile       4096     # File descriptors</text>
    <text x="65" y="174" fill="#fde047" font-size="8.5" font-family="monospace">*         hard    nofile       65535</text>
    <text x="65" y="190" fill="#fde047" font-size="8.5" font-family="monospace">@devops   hard    nproc        1024     # Max processes</text>
    <text x="65" y="206" fill="#fde047" font-size="8.5" font-family="monospace">bob       hard    maxlogins    2        # Max concurrent logins</text>

    <rect x="520" y="90" width="330" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="685" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">ULIMIT SHELL COMMANDS</text>
    <text x="535" y="140" fill="#fde047" font-size="8.5" font-family="monospace">ulimit -a       # View all limits</text>
    <text x="535" y="160" fill="#fde047" font-size="8.5" font-family="monospace">ulimit -n 8192  # Set open file limit</text>
    <text x="535" y="180" fill="#fde047" font-size="8.5" font-family="monospace">ulimit -u 500   # Max user processes</text>
    <text x="535" y="205" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Hard limits can only be raised by root!</text>
    
</svg>"""
    aliases = """alias ulim='ulimit -a'"""
    checklist = [('LFCS', 'Can you configure max open file descriptors in limits.conf?', 'nofile in /etc/security/limits.conf')]
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
      Kernel parameters tune memory caching, swap aggressiveness (<code>vm.swappiness</code>), and network routing (<code>net.ipv4.ip_forward</code>).
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 4.2: Linux Kernel Runtime Parameter Tuning via Sysctl</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">KERNEL RUNTIME TUNING: SYSCTL & /PROC/SYS</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Modifying Kernel Behaviour in Memory & On Disk</text>
    </g>
    
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">RUNTIME INSPECTION (sysctl / proc)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">sysctl -a | grep ip_forward</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">cat /proc/sys/net/ipv4/ip_forward</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">sysctl -w net.ipv4.ip_forward=1</text>
    <text x="65" y="205" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Immediate change (lost on reboot!)</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">PERSISTENCE (/etc/sysctl.d/)</text>
    <text x="465" y="140" fill="#34d399" font-size="8.5" font-family="monospace">echo "net.ipv4.ip_forward = 1" | \</text>
    <text x="465" y="155" fill="#34d399" font-size="8.5" font-family="monospace">  sudo tee /etc/sysctl.d/99-k8s.conf</text>
    <text x="465" y="175" fill="#fde047" font-size="8.5" font-family="monospace">sudo sysctl --system</text>
    <text x="465" y="195" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Reloads all configs from <code>/etc/sysctl.d/</code></text>
    <text x="465" y="210" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Essential prerequisite for Kubernetes node networking!</text>
    
</svg>"""
    aliases = """alias sysreload='sudo sysctl --system'"""
    checklist = [('LFCS', 'Can you enable IPv4 forwarding permanently with sysctl?', '/etc/sysctl.d/99-ipforward.conf && sysctl --system')]
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
      Mandatory Access Control (MAC) enforces security rules even if the root user executes the application.
    </p>
    <ul>
      <li>SELinux: Restore correct context labels on modified directories with <code>restorecon -Rv /path</code>.</li>
      <li>AppArmor: Check status with <code>aa-status</code>.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 5.2: Linux Mandatory Access Control: SELinux & AppArmor</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">MANDATORY ACCESS CONTROL (MAC): SELINUX & APPARMOR</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Enforcing Process Confinement Beyond Standard DAC</text>
    </g>
    
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SELINUX CONTEXTS &amp; MODES</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">getenforce / setenforce [Enforcing|Permissive]</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">ls -Z /var/www/html</text>
    <text x="65" y="175" fill="#fde047" font-size="8" font-family="monospace">system_u:object_r:httpd_sys_content_t:s0</text>
    <text x="65" y="195" fill="#38bdf8" font-size="8.5" font-family="monospace">restorecon -Rv /var/www/html</text>
    <text x="65" y="210" fill="#94a3b8" font-size="8" font-family="sans-serif">Config: /etc/selinux/config</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">APPARMOR PROFILES (Ubuntu / Debian)</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">sudo aa-status</text>
    <text x="465" y="160" fill="#fde047" font-size="8.5" font-family="monospace">sudo aa-enforce /etc/apparmor.d/&lt;profile&gt;</text>
    <text x="465" y="180" fill="#fde047" font-size="8.5" font-family="monospace">sudo aa-complain /etc/apparmor.d/&lt;profile&gt;</text>
    <text x="465" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Restricts binaries by file paths and capabilities</text>
    
</svg>"""
    aliases = """alias se='getenforce'"""
    checklist = [('LFCS', 'Can you check SELinux mode and restore file security contexts?', 'getenforce && restorecon -Rv'), ('LFCS', 'Can you inspect active AppArmor profiles?', 'aa-status')]
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
      Week 5 consolidation synthesizes user identity, sudo delegation, MAC policies (SELinux/AppArmor), and incident response containment.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 6.2: Linux Security Forensics & User Quarantine Flowchart</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">SECURITY AUDIT & USER QUARANTINE FORENSICS PIPELINE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Isolating Compromised Accounts & Preserving Evidence</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="170" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. QUARANTINE ACCOUNT</text>
    <text x="65" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">passwd -l compromised_user</text>
    <text x="65" y="160" fill="#fca5a5" font-size="8.5" font-family="monospace">usermod -s /sbin/nologin user</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Locks password and revokes shell</text>
    <text x="65" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">pkill -KILL -u compromised_user</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. FORENSIC AUDIT</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">last -n 20 compromised_user</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">ausearch -ua &lt;uid&gt;</text>
    <text x="325" y="180" fill="#fde047" font-size="8.5" font-family="monospace">find / -user &lt;uid&gt; -mtime -1</text>
    <text x="325" y="205" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Locates recently modified files</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. CRON &amp; ACCESS PURGE</text>
    <text x="595" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">crontab -r -u user  # Purge cron</text>
    <text x="595" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">rm -rf /home/user/.ssh</text>
    <text x="595" y="180" fill="#34d399" font-size="8.5" font-family="monospace">sed -i '/user/d' /etc/sudoers</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">System sanitized and quarantined</text>
    
</svg>"""
    aliases = """alias qlock='passwd -l'"""
    checklist = [('LFCS', 'Can you terminate all processes and lock out a compromised user in 30 seconds?', 'pkill -u <user> && passwd -l <user>')]
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
