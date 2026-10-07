"""
LFCS Curriculum Content: Week 8 (Days 1 to 6)
Day 1: Containers & VMs on Linux
Day 2: Timed Mock Exam 1
Day 3: Timed Mock Exam 2
Day 4: Timed Mock Exam 3
Day 5: Timed Mock Exam 4 & Final Speed Marathon
Day 6: Certification Gate Review & Readiness Audit
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <p>
      Modern Linux administration features container management via Podman (an OCI daemonless runtime) and virtualization management via <code>virsh</code> (libvirt).
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 1.2: Linux Container Runtimes (Podman) & Virtual Machine Architecture</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">CONTAINERS & VIRTUAL MACHINES ON LINUX</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Podman OCI Engine & KVM/QEMU Virtualization Stack</text>
    </g>
    
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">PODMAN (Daemonless &amp; Rootless OCI)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">podman run -d --name web -p 8080:80 nginx</text>
    <text x="65" y="158" fill="#4ade80" font-size="8.5" font-family="monospace">podman ps -a</text>
    <text x="65" y="176" fill="#4ade80" font-size="8.5" font-family="monospace">podman generate systemd --name web --files</text>
    <text x="65" y="194" fill="#38bdf8" font-size="8.5" font-family="monospace">podman generate kube web > pod.yaml</text>
    <text x="65" y="210" fill="#94a3b8" font-size="8" font-family="sans-serif">Generates systemd units or K8s pod YAML!</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">KVM / QEMU / LIBVIRT</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">virsh list --all</text>
    <text x="465" y="158" fill="#fde047" font-size="8.5" font-family="monospace">virsh start &lt;vm-name&gt;</text>
    <text x="465" y="176" fill="#fde047" font-size="8.5" font-family="monospace">virsh shutdown &lt;vm-name&gt;</text>
    <text x="465" y="194" fill="#fde047" font-size="8.5" font-family="monospace">virsh console &lt;vm-name&gt;</text>
    <text x="465" y="210" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Kernel-based Virtual Machine management</text>
    
</svg>"""
    aliases = """alias pman='podman'"""
    checklist = [('LFCS', 'Can you run a rootless container with Podman and manage it with systemd?', 'podman generate systemd')]
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
      Timed mock exams simulate real test conditions: strictly air-gapped, high-tempo, with precise grading requirements.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 2.2: LFCS Timed Mock Exam Strategy & Time Budgeting Matrix</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LFCS TIMED MOCK EXAM 1 STRATEGY MATRIX</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Time Budgeting & Systematic Domain Execution Framework</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TIME ALLOCATION</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• 120 Minutes / ~20 Questions</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="sans-serif">• Target: 5.5 min per question</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="sans-serif">• If stuck > 7 min: Flag &amp; skip!</text>
    <text x="65" y="205" fill="#38bdf8" font-size="8.5" font-family="sans-serif">Save 20 min for end verification.</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="440" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">VERIFICATION DRILL</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">systemctl status &lt;svc&gt;</text>
    <text x="325" y="158" fill="#fde047" font-size="8.5" font-family="monospace">mount -a  # Test fstab before reboot!</text>
    <text x="325" y="176" fill="#fde047" font-size="8.5" font-family="monospace">id &lt;user&gt; # Check UID and groups</text>
    <text x="325" y="194" fill="#fde047" font-size="8.5" font-family="monospace">ip -br a  # Check IP assignments</text>
    <text x="325" y="210" fill="#a7f3d0" font-size="8" font-family="sans-serif">Never assume it worked without testing!</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">PASSING THRESHOLD</text>
    <text x="605" y="140" fill="#4ade80" font-size="8.5" font-family="sans-serif">• Pass score: ~66%</text>
    <text x="605" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Easy questions: Useradd, cron, links</text>
    <text x="605" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Medium questions: LVM, systemd, tar</text>
    <text x="605" y="205" fill="#34d399" font-size="8.5" font-family="sans-serif">Secure 100% on easy &amp; medium!</text>
    
</svg>"""
    aliases = """alias timer='echo Mock Exam In Progress'"""
    checklist = [('LFCS', 'Can you complete a full 5-task administrative drill in under 25 minutes?', 'Timed execution')]
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
      Storage speed drills test fluent execution of LVM partitioning, UUID fstab entries, and filesystem resizing without hesitation.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 3.2: LFCS Rapid Storage & Filesystem Execution Pipeline</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LFCS TIMED MOCK EXAM 2: STORAGE & FILESYSTEM OPERATIONS</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Rapid Partitioning, LVM Sizing & Mount Configuration</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TASK 1: LVM CREATION</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">pvcreate /dev/sdb1</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">vgcreate web_vg /dev/sdb1</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">lvcreate -L 2G -n web_lv web_vg</text>
    <text x="65" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">mkfs.ext4 /dev/web_vg/web_lv</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TASK 2: PERSISTENT MOUNT</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">mkdir -p /srv/web</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">blkid /dev/web_vg/web_lv</text>
    <text x="325" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">UUID=... /srv/web ext4 defaults 0 2</text>
    <text x="325" y="200" fill="#34d399" font-size="8.5" font-family="monospace">mount -a &amp;&amp; df -h /srv/web</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TASK 3: ONLINE RESIZE</text>
    <text x="595" y="140" fill="#34d399" font-size="8.5" font-family="monospace">lvextend -L +1G /dev/web_vg/web_lv</text>
    <text x="595" y="160" fill="#34d399" font-size="8.5" font-family="monospace">resize2fs /dev/web_vg/web_lv</text>
    <text x="595" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">df -h /srv/web (Verify 3GB!)</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Completed in under 6 minutes!</text>
    
</svg>"""
    aliases = """alias blk='lsblk -f'"""
    checklist = [('LFCS', 'Can you format and mount an LVM partition in fstab in under 4 minutes?', 'End-to-end storage speed run')]
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
      Mock Exam 3 tests rapid response across networking, sudo permissions, systemd service creation, and security hardening.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 4.2: LFCS Networking & Security Triage Workflow</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LFCS TIMED MOCK EXAM 3: NETWORKING & SECURITY TRIAGE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Rapid IP Routing, Firewalls, Users & SSH Hardening</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">NETWORKING TRIAGE</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">ip addr add ... dev eth0</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">ip route add default via ...</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">firewall-cmd --add-port=443/tcp --permanent</text>
    <text x="65" y="200" fill="#34d399" font-size="8.5" font-family="monospace">firewall-cmd --reload</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SECURITY DELEGATION</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">visudo -f /etc/sudoers.d/ops</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">chmod 0440 /etc/sudoers.d/ops</text>
    <text x="325" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">chmod 2775 /shared/dev</text>
    <text x="325" y="200" fill="#a7f3d0" font-size="8.5" font-family="monospace">restorecon -Rv /var/www</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SERVICE ORCHESTRATION</text>
    <text x="595" y="140" fill="#34d399" font-size="8.5" font-family="monospace">systemctl daemon-reload</text>
    <text x="595" y="160" fill="#34d399" font-size="8.5" font-family="monospace">systemctl enable --now myapp</text>
    <text x="595" y="180" fill="#38bdf8" font-size="8.5" font-family="monospace">systemctl is-active myapp</text>
    <text x="595" y="205" fill="#4ade80" font-size="8.5" font-family="sans-serif">All tasks verified active!</text>
    
</svg>"""
    aliases = """alias chk='systemctl is-active'"""
    checklist = [('LFCS', 'Can you complete Mock Exam 3 with zero syntax errors in sudoers or fstab?', 'Tested with visudo and mount -a')]
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
      The final speed marathon reinforces rapid terminal instincts across text parsing, storage, security, and process management.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 5.2: LFCS Final Speed Marathon Tactics Across All 5 Exam Domains</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LFCS FINAL SPEED MARATHON TACTICS</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Rapid Automation, Text Processing & System Triage</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TEXT EXTRACTION</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">awk -F: '$3>=1000 {print $1}'</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">sed -i '/DEBUG/d' file.log</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">grep -oE '[0-9]+\.[0-9]+...'</text>
    <text x="65" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">sort -n | uniq -c</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">STORAGE &amp; ARCHIVE</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">tar -czf /bkp/data.tar.gz /dir</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">lvextend -r -L +2G /dev/vg/lv</text>
    <text x="325" y="180" fill="#fde047" font-size="8.5" font-family="monospace">swapon /dev/sdb3</text>
    <text x="325" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">find / -size +100M</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SECURITY &amp; SYSTEMD</text>
    <text x="595" y="140" fill="#34d399" font-size="8.5" font-family="monospace">chmod 2775 /shared</text>
    <text x="595" y="160" fill="#34d399" font-size="8.5" font-family="monospace">systemctl isolate rescue</text>
    <text x="595" y="180" fill="#34d399" font-size="8.5" font-family="monospace">journalctl -u app -p err</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Full domain mastery verified!</text>
    
</svg>"""
    aliases = """alias fast='echo Speed Marathon Ready'"""
    checklist = [('LFCS', 'Can you solve any standard LFCS question in under 4 minutes?', 'Motor skill fluency')]
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
      All 5 LFCS exam domains have been thoroughly drilled with hands-on lab automation, speed drills, and rigorous verification. You are fully prepared to pass the LFCS exam on your first attempt!
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 6.2: LFCS 5-Domain Final Certification Readiness Audit</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LFCS CERTIFICATION GATE REVIEW & DOMAIN READINESS AUDIT</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Comprehensive Competency Map Across All 5 Linux Domains</text>
    </g>
    
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. ESSENTIAL CMDS (25%)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Navigation, inodes, links</text>
    <text x="65" y="158" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Permissions &amp; special bits</text>
    <text x="65" y="176" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Tar, gzip, bzip2, xz</text>
    <text x="65" y="194" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Find, grep, sed, awk</text>
    <text x="65" y="210" fill="#4ade80" font-size="8.5" font-weight="bold" font-family="sans-serif">100% Mastered</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="340" y="115" fill="#fbbf24" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. OPERATION (20%)</text>
    <text x="265" y="140" fill="#e2e8f0" font-size="8" font-family="sans-serif">• GRUB2 &amp; boot sequence</text>
    <text x="265" y="158" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Systemd units &amp; targets</text>
    <text x="265" y="176" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Journald logging</text>
    <text x="265" y="194" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Cron &amp; at task queues</text>
    <text x="265" y="210" fill="#4ade80" font-size="8.5" font-weight="bold" font-family="sans-serif">100% Mastered</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="540" y="115" fill="#c084fc" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. USER &amp; SEC (15%)</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8" font-family="sans-serif">• /etc/passwd &amp; shadow</text>
    <text x="465" y="158" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Visudo &amp; sudo privileges</text>
    <text x="465" y="176" fill="#e2e8f0" font-size="8" font-family="sans-serif">• User limits &amp; PAM</text>
    <text x="465" y="194" fill="#e2e8f0" font-size="8" font-family="sans-serif">• SELinux &amp; AppArmor</text>
    <text x="465" y="210" fill="#4ade80" font-size="8.5" font-weight="bold" font-family="sans-serif">100% Mastered</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="750" y="115" fill="#34d399" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. STORAGE &amp; NET (40%)</text>
    <text x="665" y="140" fill="#e2e8f0" font-size="8" font-family="sans-serif">• MBR / GPT / Swap</text>
    <text x="665" y="155" fill="#e2e8f0" font-size="8" font-family="sans-serif">• LVM creation &amp; resize</text>
    <text x="665" y="170" fill="#e2e8f0" font-size="8" font-family="sans-serif">• /etc/fstab &amp; NFS</text>
    <text x="665" y="185" fill="#e2e8f0" font-size="8" font-family="sans-serif">• IP, routing, firewalld</text>
    <text x="665" y="200" fill="#34d399" font-size="10" font-weight="bold" font-family="sans-serif">CERTIFICATION READY!</text>
    
</svg>"""
    aliases = """alias lfpass='echo Congratulations LFCS Certified!'"""
    checklist = [('LFCS', 'Have you cleared all 8 weeks of LFCS labs and mock marathons?', 'Full curriculum completed')]
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
