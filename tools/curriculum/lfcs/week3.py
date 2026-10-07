"""
LFCS Curriculum Content: Week 3 (Days 1 to 6)
Day 1: Linux Boot Architecture & GRUB2
Day 2: Systemd Targets & Runlevel Management
Day 3: Creating & Managing Systemd Services
Day 4: Process Diagnostics & Signal Management
Day 5: System Integrity, Resource Monitoring & Top
Day 6: Week 3 Systemd & Process Orchestration
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <p>
      The Linux boot pipeline moves from hardware initialization to GRUB2, kernel unpacking, initramfs root filesystem mount, and handoff to PID 1 (<code>systemd</code>).
    </p>
    <ul>
      <li>GRUB config template: <code>/etc/default/grub</code> (apply with <code>update-grub</code> or <code>grub2-mkconfig -o /boot/grub2/grub.cfg</code>).</li>
      <li>Emergency root recovery: Append <code>init=/bin/bash</code> or <code>rd.break</code> to kernel parameters in GRUB to bypass root password.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 1.2: Linux Boot Architecture: UEFI -> GRUB2 -> Kernel/Initramfs -> Systemd</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LINUX BOOT SEQUENCE: UEFI/BIOS TO SYSTEMD PID 1</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Hardware Initialization -> Kernel Boot -> User Space Systemd</text>
    </g>
    
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. FIRMWARE</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• UEFI / BIOS</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Power-On Self Test (POST)</text>
    <text x="65" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Reads ESP partition or MBR</text>
    <text x="65" y="200" fill="#a7f3d0" font-size="8.5" font-family="monospace">/boot/efi (EFI/)</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="340" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. GRUB2 BOOTLOADER</text>
    <text x="265" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <code>/boot/grub/grub.cfg</code></text>
    <text x="265" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Edits in <code>/etc/default/grub</code></text>
    <text x="265" y="180" fill="#fde047" font-size="8.5" font-family="monospace">update-grub</text>
    <text x="265" y="200" fill="#fca5a5" font-size="8.5" font-family="sans-serif">Press 'e' at boot to edit kernel</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="540" y="115" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. KERNEL &amp; INITRAMFS</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">vmlinuz-&lt;version&gt;</text>
    <text x="465" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">initrd.img-&lt;version&gt;</text>
    <text x="465" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Loads root disk drivers</text>
    <text x="465" y="200" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Mounts read-only rootfs (/)</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="750" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. SYSTEMD (PID 1)</text>
    <text x="665" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">/sbin/init -> systemd</text>
    <text x="665" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Initializes system targets</text>
    <text x="665" y="180" fill="#34d399" font-size="8.5" font-family="monospace">default.target</text>
    <text x="665" y="200" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Spawns all daemons in parallel</text>
    
</svg>"""
    aliases = """alias grubup='sudo update-grub'"""
    checklist = [('LFCS', 'Can you edit GRUB parameters permanently via /etc/default/grub?', 'GRUB_CMDLINE_LINUX_DEFAULT and update-grub'), ('LFCS', 'Can you explain the function of initramfs during early boot?', 'Provides disk/storage drivers to mount real root filesystem')]
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
      Systemd uses <strong>Targets</strong> (.target units) to group dependencies and bring the system into a desired state, replacing legacy SysV runlevels.
    </p>
    <ul>
      <li>View active target: <code>systemctl get-default</code></li>
      <li>Change default boot target: <code>systemctl set-default multi-user.target</code></li>
      <li>Switch active target immediately: <code>systemctl isolate rescue.target</code></li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 2.2: Systemd Target Dependency Hierarchy & Runlevel Transition</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">SYSTEMD TARGETS & RUNLEVEL HIERARCHY</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Target Synchronization & Default Target Management</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">MULTI-USER.TARGET (Runlevel 3)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Standard server console environment</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Networking, storage &amp; multi-user logins</text>
    <text x="65" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• No graphical display server</text>
    <text x="65" y="205" fill="#4ade80" font-size="8.5" font-family="monospace">systemctl isolate multi-user.target</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">GRAPHICAL.TARGET (Runlevel 5)</text>
    <text x="325" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Extends <code>multi-user.target</code></text>
    <text x="325" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Spawns X11 / Wayland &amp; Display Manager</text>
    <text x="325" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl get-default</text>
    <text x="325" y="205" fill="#fde047" font-size="8.5" font-family="monospace">systemctl set-default graphical.target</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="715" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">RESCUE &amp; EMERGENCY TARGETS</text>
    <text x="595" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">rescue.target (Runlevel 1)</text>
    <text x="595" y="155" fill="#94a3b8" font-size="8" font-family="sans-serif">Single user root shell, minimal mounts</text>
    <text x="595" y="175" fill="#e2e8f0" font-size="8.5" font-family="monospace">emergency.target</text>
    <text x="595" y="190" fill="#fca5a5" font-size="8" font-family="sans-serif">Read-only root, no services initialized</text>
    <text x="595" y="210" fill="#38bdf8" font-size="8" font-family="monospace">systemctl isolate rescue.target</text>
    
</svg>"""
    aliases = """alias target='systemctl get-default'"""
    checklist = [('LFCS', 'Can you query and set the default systemd target?', 'systemctl get-default && systemctl set-default <target>'), ('LFCS', 'Can you switch the running system to rescue mode?', 'systemctl isolate rescue.target')]
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
      Creating and debugging custom systemd service files is a prominent LFCS requirement.
    </p>
    <ul>
      <li>Unit locations: <code>/etc/systemd/system/</code> (administrator custom units), <code>/lib/systemd/system/</code> (package-installed).</li>
      <li>After creating or modifying a unit file, you must run <code>systemctl daemon-reload</code>!</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 3.2: Systemd Custom Service Architecture & Management</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">SYSTEMD SERVICE UNIT ARCHITECTURE & LIFECYCLE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Unit File Layout: [Unit], [Service], [Install]</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">[Unit] SECTION</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">Description=My Custom Daemon</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">After=network.target</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">Wants=redis.service</text>
    <text x="65" y="200" fill="#94a3b8" font-size="8" font-family="sans-serif">Defines metadata and boot ordering</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="440" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">[Service] SECTION</text>
    <text x="325" y="138" fill="#4ade80" font-size="8.5" font-family="monospace">Type=simple / forking / oneshot</text>
    <text x="325" y="156" fill="#4ade80" font-size="8.5" font-family="monospace">ExecStart=/usr/local/bin/app</text>
    <text x="325" y="174" fill="#4ade80" font-size="8.5" font-family="monospace">Restart=on-failure</text>
    <text x="325" y="192" fill="#4ade80" font-size="8.5" font-family="monospace">User=appuser</text>
    <text x="325" y="210" fill="#fde047" font-size="8" font-family="monospace">EnvironmentFile=/etc/app.env</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="720" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">[Install] &amp; SYSTEMCTL</text>
    <text x="605" y="138" fill="#fde047" font-size="8.5" font-family="monospace">WantedBy=multi-user.target</text>
    <text x="605" y="158" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl daemon-reload</text>
    <text x="605" y="176" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl enable --now app</text>
    <text x="605" y="194" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl status app</text>
    <text x="605" y="212" fill="#a7f3d0" font-size="8" font-family="sans-serif">Path: /etc/systemd/system/app.service</text>
    
</svg>"""
    aliases = """alias sc='systemctl'
alias scu='systemctl daemon-reload'"""
    checklist = [('LFCS', 'Can you create a systemd service from scratch in /etc/systemd/system?', 'Create unit file, reload daemon, enable and start'), ('LFCS', 'Can you restart a failed systemd service and inspect its journal logs?', 'systemctl restart <svc> && journalctl -u <svc> -e')]
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
      Managing processes and sending proper signals is foundational to Linux systems engineering.
    </p>
    <ul>
      <li>Always try <code>SIGTERM (15)</code> first to allow the application to flush buffers and close connections cleanly before resorting to <code>SIGKILL (9)</code>.</li>
      <li>Processes in state <code>D</code> (Disk sleep) cannot be killed even with <code>SIGKILL</code> because they are waiting on uninterruptible kernel I/O!</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 4.2: Linux Process States & Signal Dispatch Architecture</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LINUX PROCESS STATES & POSIX SIGNALS</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Process Lifecycle States & Signal Handling Dispatch</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">PROCESS STATES (ps / top)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">R: Running / Runnable on CPU</text>
    <text x="65" y="158" fill="#e2e8f0" font-size="8.5" font-family="monospace">S: Interruptible Sleep (waiting for event)</text>
    <text x="65" y="176" fill="#fca5a5" font-size="8.5" font-family="monospace">D: Uninterruptible Sleep (I/O wait!)</text>
    <text x="65" y="194" fill="#fbbf24" font-size="8.5" font-family="monospace">Z: Zombie (terminated, uncollected)</text>
    <text x="65" y="212" fill="#e2e8f0" font-size="8.5" font-family="monospace">T: Stopped (SIGSTOP / Ctrl-Z)</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="435" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">KEY POSIX SIGNALS</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">1 (SIGHUP): Reload configuration</text>
    <text x="325" y="158" fill="#fde047" font-size="8.5" font-family="monospace">2 (SIGINT): Interrupt (Ctrl-C)</text>
    <text x="325" y="176" fill="#fde047" font-size="8.5" font-family="monospace">9 (SIGKILL): Force kill (Uncatchable!)</text>
    <text x="325" y="194" fill="#fde047" font-size="8.5" font-family="monospace">15 (SIGTERM): Graceful termination</text>
    <text x="325" y="212" fill="#fde047" font-size="8.5" font-family="monospace">19 (SIGSTOP): Pause process execution</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">COMMAND DISPATCH</text>
    <text x="595" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">kill -15 &lt;pid&gt;    # Graceful</text>
    <text x="595" y="158" fill="#4ade80" font-size="8.5" font-family="monospace">kill -9 &lt;pid&gt;     # Immediate kill</text>
    <text x="595" y="176" fill="#4ade80" font-size="8.5" font-family="monospace">pkill -u user nginx</text>
    <text x="595" y="194" fill="#4ade80" font-size="8.5" font-family="monospace">pgrep -l app</text>
    <text x="595" y="212" fill="#38bdf8" font-size="8.5" font-family="monospace">killall -HUP nginx</text>
    
</svg>"""
    aliases = """alias psig='kill -l'
alias topmem='ps aux --sort=-%mem | head -n 10'"""
    checklist = [('LFCS', 'Can you identify high CPU/memory processes with ps or top?', 'ps aux --sort=-%cpu | head'), ('LFCS', 'Can you send a reload signal (SIGHUP) to a running service?', 'kill -HUP <pid> or pkill -HUP <name>')]
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
      System performance diagnostics rely on understanding the load average and CPU states in <code>top</code>, <code>htop</code>, <code>uptime</code>, and <code>vmstat</code>.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 5.2: Linux Resource Diagnostics: Load Average & CPU Utilization Metrics</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">SYSTEM INTEGRITY & RESOURCE MONITORING (TOP / UPTIME)</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Load Average, CPU State Breakdown & Memory Utilization</text>
    </g>
    
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">LOAD AVERAGE (1, 5, 15 min)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">load average: 0.85, 1.20, 1.45</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Number of processes running or waiting on CPU / disk I/O.</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="sans-serif">• On an 8-core CPU, load &lt; 8.0 means normal capacity.</text>
    <text x="65" y="200" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• If load &gt;&gt; core count, system is saturated (bottlenecked).</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">CPU STATE METRICS (top / mpstat)</text>
    <text x="465" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">us (user): User space application CPU</text>
    <text x="465" y="158" fill="#38bdf8" font-size="8.5" font-family="monospace">sy (system): Kernel syscall overhead</text>
    <text x="465" y="176" fill="#fca5a5" font-size="8.5" font-family="monospace">wa (iowait): Time CPU waits on disk I/O</text>
    <text x="465" y="194" fill="#94a3b8" font-size="8.5" font-family="monospace">id (idle): Free CPU capacity</text>
    <text x="465" y="210" fill="#fbbf24" font-size="8" font-family="sans-serif">High 'wa' indicates disk thrashing or slow I/O subsystem!</text>
    
</svg>"""
    aliases = """alias vm='vmstat 1 5'"""
    checklist = [('LFCS', 'Can you explain load average relative to CPU core count?', 'Load >= CPU cores indicates queued processes'), ('LFCS', 'Can you determine if high load is caused by disk I/O wait?', 'Inspect %wa in top or vmstat')]
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
      Week 3 consolidation synthesizes boot processes, runlevels/targets, unit creation, and process signal management into an integrated administrative toolkit.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 6.2: Systemd Process Control, Cgroups & Diagnostic Tooling</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">WEEK 3 SYSTEMD & PROCESS ORCHESTRATION PIPELINE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Service Dependencies, Cgroups & Resource Throttling</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SYSTEMD CGROUPS</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Resource slices: system.slice, user.slice</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">CPUQuota=50%</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">MemoryMax=512M</text>
    <text x="65" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">systemd-cgtop</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">DEPENDENCY ORDERING</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">After=, Before= (Ordering)</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">Requires= (Hard dependency)</text>
    <text x="325" y="180" fill="#fde047" font-size="8.5" font-family="monospace">Wants= (Soft dependency)</text>
    <text x="325" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl list-dependencies</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SERVICE HEALTH TRIAGE</text>
    <text x="595" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">systemctl --failed</text>
    <text x="595" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">systemctl reset-failed</text>
    <text x="595" y="180" fill="#34d399" font-size="8.5" font-family="monospace">journalctl -u app.service -xe</text>
    <text x="595" y="200" fill="#94a3b8" font-size="8" font-family="sans-serif">Full contextual stacktrace analysis</text>
    
</svg>"""
    aliases = """alias failed='systemctl --failed'"""
    checklist = [('LFCS', 'Can you list failed systemd services and view their logs?', 'systemctl --failed && journalctl -u <svc> -xe'), ('LFCS', 'Can you inspect real-time cgroup resource consumption?', 'systemd-cgtop')]
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
