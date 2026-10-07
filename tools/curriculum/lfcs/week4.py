"""
LFCS Curriculum Content: Week 4 (Days 1 to 6)
Day 1: Journald & System Log File Analysis
Day 2: Task Scheduling with Cron & At
Day 3: Package Managers (APT, DNF/YUM & RPM)
Day 4: Compiling Software from Source Code
Day 5: Bash Automation & Scripting
Day 6: Week 4 Automation Triathlon
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <p>
      <code>journalctl</code> inspects binary logs managed by <code>systemd-journald</code>.
    </p>
    <ul>
      <li>Filter by unit: <code>journalctl -u sshd -e</code></li>
      <li>Filter by priority level: <code>journalctl -p 3</code> (Errors and worse).</li>
      <li>To persist logs across reboots, create <code>/var/log/journal</code> and restart the daemon.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 1.2: Systemd Journal Architecture & Query Optimization Engine</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">SYSTEMD-JOURNALD BINARY LOGGING ARCHITECTURE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">High-Performance Querying & Filter Combinations</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">STORAGE &amp; PERSISTENCE</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">/run/log/journal/ (Volatile)</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">/var/log/journal/ (Persistent)</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">/etc/systemd/journald.conf</text>
    <text x="65" y="205" fill="#94a3b8" font-size="8" font-family="sans-serif">Set <code>Storage=persistent</code></text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">QUERY FILTERING</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">journalctl -u nginx.service</text>
    <text x="325" y="158" fill="#fde047" font-size="8.5" font-family="monospace">journalctl -p err..emerg</text>
    <text x="325" y="176" fill="#fde047" font-size="8.5" font-family="monospace">journalctl -b  # Current boot</text>
    <text x="325" y="194" fill="#fde047" font-size="8.5" font-family="monospace">journalctl --since "1 hour ago"</text>
    <text x="325" y="212" fill="#fde047" font-size="8.5" font-family="monospace">journalctl -k  # dmesg / kernel</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">OUTPUT &amp; ROTATION</text>
    <text x="595" y="140" fill="#34d399" font-size="8.5" font-family="monospace">journalctl -f  # Real-time tail</text>
    <text x="595" y="160" fill="#34d399" font-size="8.5" font-family="monospace">journalctl -n 50 --no-pager</text>
    <text x="595" y="180" fill="#34d399" font-size="8.5" font-family="monospace">journalctl --disk-usage</text>
    <text x="595" y="205" fill="#e2e8f0" font-size="8.5" font-family="monospace">journalctl --vacuum-size=500M</text>
    
</svg>"""
    aliases = """alias jerr='journalctl -p err -b --no-pager'"""
    checklist = [('LFCS', 'Can you configure journald for persistent disk storage?', 'Storage=persistent in /etc/systemd/journald.conf'), ('LFCS', 'Can you filter journal logs for specific service errors in the last 30 minutes?', "journalctl -u <svc> -p err --since '-30m'")]
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
      Recurring task scheduling with <code>cron</code> is an LFCS core requirement.
    </p>
    <ul>
      <li>Edit user crontab: <code>crontab -e</code> (never edit <code>/var/spool/cron/crontabs</code> directly).</li>
      <li>System crontab: <code>/etc/crontab</code> contains an extra <code>user</code> column before the command!</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 2.2: Linux Automated Task Scheduling: Cron vs At Queue</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LINUX TASK SCHEDULING: CRON & AT DAEMONS</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Recurring Crontab Syntax & One-Shot At Queue</text>
    </g>
    
    <rect x="50" y="90" width="450" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="275" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">CRONTAB SYNTAX (min, hr, dom, mon, dow)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">*    *    *    *    *    command to execute</text>
    <text x="65" y="155" fill="#fde047" font-size="8" font-family="monospace">┬    ┬    ┬    ┬    ┬</text>
    <text x="65" y="170" fill="#fde047" font-size="8" font-family="monospace">│    │    │    │    └─ Day of week (0-6, 0=Sunday)</text>
    <text x="65" y="185" fill="#fde047" font-size="8" font-family="monospace">│    │    │    └────── Month (1-12)</text>
    <text x="65" y="200" fill="#fde047" font-size="8" font-family="monospace">│    │    └─────────── Day of month (1-31)</text>
    <text x="65" y="215" fill="#fde047" font-size="8" font-family="monospace">│    └──────────────── Hour (0-23) | Minute (0-59)</text>

    <rect x="520" y="90" width="330" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="685" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">ONE-SHOT: AT UTILITY</text>
    <text x="535" y="140" fill="#fde047" font-size="8.5" font-family="monospace">echo "sh /opt/backup.sh" | at 02:00 AM</text>
    <text x="535" y="160" fill="#fde047" font-size="8.5" font-family="monospace">echo "reboot" | at now + 10 minutes</text>
    <text x="535" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">atq     # List queued jobs</text>
    <text x="535" y="205" fill="#fca5a5" font-size="8.5" font-family="monospace">atrm &lt;job-id&gt;   # Remove job</text>
    
</svg>"""
    aliases = """alias mycron='crontab -l'"""
    checklist = [('LFCS', 'Can you schedule a cron job to run every 15 minutes on weekdays?', '*/15 * * * 1-5 /path/to/cmd'), ('LFCS', 'Can you queue a one-off task using at?', 'at now + 5 minutes')]
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
      Package managers resolve dependencies and track installed files on Linux systems.
    </p>
    <ul>
      <li>Determine which package owns a binary: <code>dpkg -S /usr/bin/git</code> or <code>rpm -qf /usr/bin/git</code>.</li>
      <li>List all files in an installed package: <code>dpkg -L nginx</code> or <code>rpm -ql nginx</code>.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 3.2: Linux Package Management Architecture (APT vs DNF/RPM)</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LINUX PACKAGE MANAGEMENT: APT (DEBIAN) VS DNF/YUM (RHEL)</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Repository Architecture & Package Operations</text>
    </g>
    
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">DEBIAN / UBUNTU (APT &amp; DPKG)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">apt update &amp;&amp; apt install -y &lt;pkg&gt;</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">dpkg -i package.deb   # Low-level install</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">dpkg -L &lt;pkg&gt;         # List files in package</text>
    <text x="65" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">dpkg -S /path/file    # Which package owns file</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">RHEL / CENTOS (DNF &amp; RPM)</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">dnf install -y &lt;pkg&gt;</text>
    <text x="465" y="160" fill="#fde047" font-size="8.5" font-family="monospace">rpm -ivh package.rpm  # Low-level install</text>
    <text x="465" y="180" fill="#fde047" font-size="8.5" font-family="monospace">rpm -ql &lt;pkg&gt;         # List files in package</text>
    <text x="465" y="200" fill="#fde047" font-size="8.5" font-family="monospace">rpm -qf /path/file    # Query owning package</text>
    
</svg>"""
    aliases = """alias owns='dpkg -S'"""
    checklist = [('LFCS', 'Can you find which package installed a specific command?', 'dpkg -S /path/file or rpm -qf /path/file'), ('LFCS', 'Can you install and query an RPM or DEB package file locally?', 'dpkg -i or rpm -ivh')]
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
      Compiling software from source requires the standard build toolchain (<code>gcc</code>, <code>make</code>, <code>libc-dev</code>).
    </p>
    <ul>
      <li>Inspect binary library dependencies with <code>ldd &lt;binary&gt;</code>.</li>
      <li>Update the dynamic linker library cache with <code>ldconfig</code>.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 4.2: Software Compilation Toolchain & Shared Library Management</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">C/C++ SOURCE COMPILATION TOOLCHAIN PIPELINE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Preprocessing -> Compiling -> Assembling -> Linking</text>
    </g>
    
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. CONFIGURE</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">./configure --prefix=/usr/local</text>
    <text x="65" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Checks system headers</text>
    <text x="65" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Verifies libraries &amp; gcc</text>
    <text x="65" y="200" fill="#fde047" font-size="8.5" font-family="sans-serif">Generates Makefile</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="340" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. MAKE (Compile)</text>
    <text x="265" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">make -j$(nproc)</text>
    <text x="265" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Invokes gcc / g++</text>
    <text x="265" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Compiles source to .o</text>
    <text x="265" y="200" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Links into binary ELF</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="540" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. INSTALL</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">sudo make install</text>
    <text x="465" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Copies binary to /bin</text>
    <text x="465" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Installs man pages</text>
    <text x="465" y="200" fill="#fde047" font-size="8.5" font-family="monospace">ldconfig (update cache)</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="750" y="115" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. SHARED LIBS</text>
    <text x="665" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">ldd /path/to/binary</text>
    <text x="665" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Lists dynamic .so dependencies</text>
    <text x="665" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">/etc/ld.so.conf.d/</text>
    <text x="665" y="205" fill="#a7f3d0" font-size="8.5" font-family="monospace">ldconfig -v</text>
    
</svg>"""
    aliases = """alias lddcheck='ldd'"""
    checklist = [('LFCS', 'Can you compile a C program and inspect shared library linkage?', 'gcc -o app app.c && ldd app'), ('LFCS', 'Can you update shared library paths with ldconfig?', '/etc/ld.so.conf and sudo ldconfig')]
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
      Reliable sysadmin automation requires robust Bash standards.
    </p>
    <ul>
      <li>Always use <code>set -euo pipefail</code> at the start of every script.</li>
      <li>Clean up temporary files with <code>trap 'rm -rf "$TMPDIR"' EXIT</code>.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 5.2: Production Bash Scripting Patterns & Defensive Standards</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">PRODUCTION BASH AUTOMATION ARCHITECTURE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Robust Error Trapping, Parameter Expansion & Functions</text>
    </g>
    
    <rect x="50" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="180" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">DEFENSIVE PREAMBLE</text>
    <text x="65" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">#!/bin/bash</text>
    <text x="65" y="160" fill="#fca5a5" font-size="8.5" font-family="monospace">set -euo pipefail</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8" font-family="sans-serif">-e: exit on error | -u: error on unset var</text>
    <text x="65" y="195" fill="#e2e8f0" font-size="8" font-family="sans-serif">-o pipefail: fail if ANY pipe element fails</text>
    <text x="65" y="210" fill="#38bdf8" font-size="8" font-family="monospace">trap 'echo "Error on line $LINENO"' ERR</text>

    <rect x="330" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="455" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">PARAMETER EXPANSION</text>
    <text x="345" y="140" fill="#fde047" font-size="8.5" font-family="monospace">${VAR:-default}  # Default if unset</text>
    <text x="345" y="160" fill="#fde047" font-size="8.5" font-family="monospace">${VAR:?error}    # Error if unset</text>
    <text x="345" y="180" fill="#fde047" font-size="8.5" font-family="monospace">${#VAR}          # String length</text>
    <text x="345" y="200" fill="#fde047" font-size="8.5" font-family="monospace">${VAR%/*}        # Strip dirname</text>

    <rect x="600" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="725" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TEST OPERATORS</text>
    <text x="615" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">[[ -f $FILE ]]  # Regular file</text>
    <text x="615" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">[[ -d $DIR ]]   # Directory</text>
    <text x="615" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">[[ -z $STR ]]   # Empty string</text>
    <text x="615" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">[[ $A =~ ^[0-9]+$ ]]  # Regex</text>
    
</svg>"""
    aliases = """alias bashstrict='set -euo pipefail'"""
    checklist = [('LFCS', 'Can you write a bash script with proper exit traps and error handling?', 'trap on EXIT and ERR'), ('LFCS', 'Can you evaluate regex patterns within bash [[ ... ]] test conditions?', '[[ $var =~ ^[0-9]+$ ]]')]
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
      Week 4 consolidation validates practical maintenance scripting, cron scheduling, journald inspection, and package installation.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 6.2: Automated System Maintenance & Verification Pipeline</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">SYSTEM MAINTENANCE TRIATHLON WORKFLOW</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Crontab -> Automated Bash Script -> Journald Logging</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">CRON DISPATCH</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">0 3 * * * /opt/backup.sh</text>
    <text x="65" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Triggers daily maintenance script</text>
    <text x="65" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">logger -t backup "Started"</text>
    <text x="65" y="205" fill="#a7f3d0" font-size="8" font-family="sans-serif">Sends syslog entries to journald</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">BASH AUTOMATION</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">tar -czf /bkp/$(date +%F).tar.gz</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">find /bkp -mtime +7 -delete</text>
    <text x="325" y="185" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Cleans archives older than 7 days</text>
    <text x="325" y="205" fill="#34d399" font-size="8.5" font-family="monospace">systemctl status --failed</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">VERIFICATION</text>
    <text x="595" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">journalctl -t backup -n 20</text>
    <text x="595" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">df -h /bkp</text>
    <text x="595" y="180" fill="#38bdf8" font-size="8.5" font-family="monospace">tar -tf /bkp/latest.tar.gz</text>
    <text x="595" y="205" fill="#94a3b8" font-size="8" font-family="sans-serif">Validates archive integrity</text>
    
</svg>"""
    aliases = """alias bkp='tar -czvf backup-$(date +%Y%m%d).tar.gz'"""
    checklist = [('LFCS', 'Can you create an automated backup script triggered by cron with journal logging?', 'Cron + bash + logger')]
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
