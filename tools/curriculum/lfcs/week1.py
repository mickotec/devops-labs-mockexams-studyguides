"""
LFCS Curriculum Content: Week 1 (Days 1 to 6)
Day 1: Consoles, Navigation & Docs
Day 2: Hard & Soft Links
Day 3: Standard Linux File Permissions
Day 4: Special Permissions (SUID/SGID/Sticky)
Day 5: Pagers, Vim Mastery & Terminal Editing
Day 6: Week 1 Consolidation & Permission Auditing
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <p>
      The Linux Foundation Certified System Administrator (LFCS) exam is conducted in a strictly <strong>air-gapped environment</strong>. Fast offline navigation and man section mastery are vital.
    </p>
    <ul>
      <li><strong>Section 1:</strong> User commands (e.g. <code>passwd</code>, <code>chmod</code>, <code>tar</code>).</li>
      <li><strong>Section 5:</strong> File formats and configurations (e.g. <code>man 5 fstab</code>, <code>man 5 shadow</code>). Always check Section 5 when you forget column syntax!</li>
      <li><strong>Section 8:</strong> System administration tools (e.g. <code>man 8 useradd</code>, <code>man 8 mkfs</code>).</li>
      <li><strong>Directory Stacks:</strong> <code>pushd &lt;dir&gt;</code>, <code>popd</code>, and <code>dirs -v</code> provide a LIFO stack to jump between configuration paths without losing context.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 1.2: Linux Manual Hierarchy (Sections 1, 5, 8) & Offline Examination Querying</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="260" height="190" rx="9" fill="url(#cardDark)" stroke="#3b82f6" stroke-width="1.5"/>
      <rect x="30" y="50" width="260" height="28" rx="9" fill="#3b82f6" opacity="0.18"/>
      <text x="44" y="70" fill="#60a5fa" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">MAN SECTION 1</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">User Executables</text>
    </g>
    
    <text x="45" y="100" fill="#e2e8f0" font-size="9" font-family="sans-serif">• Commands for normal users</text>
    <text x="45" y="120" fill="#e2e8f0" font-size="9" font-family="sans-serif">• Examples: passwd, ls, cp, tar</text>
    
    <rect x="45" y="145" width="230" height="75" rx="5" fill="#030712" stroke="#334155" stroke-width="1"/>
    <text x="55" y="161" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">man passwd</text><text x="55" y="175" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace"># Changes user password</text><text x="55" y="189" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">man 1 ls</text>
    

    
    <g filter="url(#shadow)">
      <rect x="320" y="50" width="260" height="190" rx="9" fill="url(#cardDark)" stroke="#10b981" stroke-width="1.5"/>
      <rect x="320" y="50" width="260" height="28" rx="9" fill="#10b981" opacity="0.18"/>
      <text x="334" y="70" fill="#34d399" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">MAN SECTION 5</text>
      <text x="334" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">File Formats & Config</text>
    </g>
    
    <text x="335" y="100" fill="#e2e8f0" font-size="9" font-family="sans-serif">• System file layouts &amp; columns</text>
    <text x="335" y="120" fill="#e2e8f0" font-size="9" font-family="sans-serif">• Examples: /etc/fstab, crontab</text>
    
    <rect x="335" y="145" width="230" height="75" rx="5" fill="#030712" stroke="#334155" stroke-width="1"/>
    <text x="345" y="161" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">man 5 fstab</text><text x="345" y="175" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace"># Explains mount fields</text><text x="345" y="189" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">man 5 passwd</text>
    

    
    <g filter="url(#shadow)">
      <rect x="610" y="50" width="260" height="190" rx="9" fill="url(#cardDark)" stroke="#f59e0b" stroke-width="1.5"/>
      <rect x="610" y="50" width="260" height="28" rx="9" fill="#f59e0b" opacity="0.18"/>
      <text x="624" y="70" fill="#fbbf24" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">MAN SECTION 8</text>
      <text x="624" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">System Admin Daemons</text>
    </g>
    
    <text x="625" y="100" fill="#e2e8f0" font-size="9" font-family="sans-serif">• Privileged root tools &amp; init</text>
    <text x="625" y="120" fill="#e2e8f0" font-size="9" font-family="sans-serif">• Examples: useradd, fdisk, iptables</text>
    
    <rect x="625" y="145" width="230" height="75" rx="5" fill="#030712" stroke="#334155" stroke-width="1"/>
    <text x="635" y="161" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">man 8 useradd</text><text x="635" y="175" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace"># Explains useradd flags</text><text x="635" y="189" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">man 8 fdisk</text>
    
    
</svg>"""
    aliases = """alias ll='ls -laF --time-style=long-iso'
man 5 fstab | grep -A5 defaults"""
    checklist = [('LFCS', 'Can you query the exact field structure of /etc/fstab without internet?', 'man 5 fstab'), ('LFCS', 'Can you traverse and return from deep directory trees using directory stacks?', 'pushd /path && popd'), ('LFCS', 'Can you extract man documentation non-interactively in shell scripts?', 'man <cmd> | col -b | awk ...')]
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
      Linux filesystems separate file metadata (Inodes) from directory entries (Names).
    </p>
    <ul>
      <li><strong>Inodes:</strong> Contain permissions, owner, timestamps, and data block pointers, but <em>not the file name</em>!</li>
      <li><strong>Hard Links (<code>ln src dst</code>):</strong> Creates a new directory entry pointing to the <em>same inode</em>. Deleting the source file does not lose data because the inode link count remains $>0$. Cannot span across different filesystems.</li>
      <li><strong>Soft Links (<code>ln -s src dst</code>):</strong> A distinct file containing the pathname to another file. Can span filesystems. Relative paths are essential for portability.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 2.2: Linux File System Inodes, Hard Links vs Symbolic Link Resolution</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="400" height="190" rx="9" fill="url(#cardDark)" stroke="#3b82f6" stroke-width="1.5"/>
      <rect x="30" y="50" width="400" height="28" rx="9" fill="#3b82f6" opacity="0.18"/>
      <text x="44" y="70" fill="#60a5fa" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">HARD LINK ARCHITECTURE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Direct Pointer to Same Inode</text>
    </g>
    
    <rect x="50" y="90" width="160" height="45" rx="5" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="130" y="110" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" font-family="sans-serif">file.txt (Name 1)</text>
    <text x="130" y="125" fill="#93c5fd" font-size="8" text-anchor="middle" font-family="monospace">Points to Inode #84920</text>

    <rect x="250" y="90" width="160" height="45" rx="5" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="330" y="110" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" font-family="sans-serif">hardlink.txt (Name 2)</text>
    <text x="330" y="125" fill="#93c5fd" font-size="8" text-anchor="middle" font-family="monospace">Points to Inode #84920</text>

    <rect x="150" y="150" width="160" height="70" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="230" y="172" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Inode #84920</text>
    <text x="230" y="190" fill="#a7f3d0" font-size="8.5" text-anchor="middle" font-family="sans-serif">Link Count: 2</text>
    <text x="230" y="206" fill="#ecfdf5" font-size="8" text-anchor="middle" font-family="monospace">Disk Blocks: [B42, B43]</text>

    
    <line x1="130" y1="135" x2="180" y2="150" stroke="#34d399" stroke-width="2" marker-end="url(#arrowGreen)"/>
    
    
    
    <line x1="330" y1="135" x2="280" y2="150" stroke="#34d399" stroke-width="2" marker-end="url(#arrowGreen)"/>
    
    

    
    <g filter="url(#shadow)">
      <rect x="470" y="50" width="400" height="190" rx="9" fill="url(#cardDark)" stroke="#f59e0b" stroke-width="1.5"/>
      <rect x="470" y="50" width="400" height="28" rx="9" fill="#f59e0b" opacity="0.18"/>
      <text x="484" y="70" fill="#fbbf24" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">SYMBOLIC (SOFT) LINK ARCHITECTURE</text>
      <text x="484" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Pointer to Target Path</text>
    </g>
    
    <rect x="490" y="90" width="170" height="45" rx="5" fill="#78350f" stroke="#fbbf24"/>
    <text x="575" y="110" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" font-family="sans-serif">symlink.txt</text>
    <text x="575" y="125" fill="#fef3c7" font-size="8" text-anchor="middle" font-family="monospace">Own Inode #91144</text>

    <rect x="680" y="90" width="170" height="45" rx="5" fill="#064e3b" stroke="#34d399"/>
    <text x="765" y="110" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" font-family="sans-serif">target.txt</text>
    <text x="765" y="125" fill="#a7f3d0" font-size="8" text-anchor="middle" font-family="monospace">Target Inode #84920</text>

    <rect x="490" y="150" width="360" height="70" rx="6" fill="#1e293b" stroke="#64748b"/>
    <text x="505" y="172" fill="#38bdf8" font-size="9" font-weight="bold" font-family="monospace">ln -s ../path/target symlink</text>
    <text x="505" y="190" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Relative symlinks stay valid across chroot or root moves.</text>
    <text x="505" y="206" fill="#fca5a5" font-size="8" font-family="sans-serif">• If target.txt is deleted, symlink.txt becomes broken (dangling)!</text>
    
    <line x1="660" y1="112" x2="678" y2="112" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrowAmber)"/>
    <text x="669" y="107" fill="#fbbf24" font-size="8.8" font-weight="bold" text-anchor="middle" font-family="-apple-system, sans-serif">points to</text>
    
    
</svg>"""
    aliases = """alias lsl='ls -lhi'
find / -samefile /path/to/target 2>/dev/null"""
    checklist = [('LFCS', 'Can you identify files sharing the same inode number?', 'ls -li file1 file2'), ('LFCS', "Can you create a relative symbolic link that won't break if directory is moved?", 'ln -sf ../target symlink'), ('LFCS', 'Can you find all files with hard link count greater than 1?', 'find /dir -type f -links +1')]
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
      Linux file permissions govern access for Owner, Group, and Other. Permissions are represented symbolically (<code>rwxr-xr-x</code>) or in octal notation (<code>755</code>).
    </p>
    <ul>
      <li><strong>Directory Permissions:</strong> <code>r</code> allows listing files (<code>ls</code>); <code>w</code> allows creating/deleting files inside the directory; <code>x</code> allows traversing into the directory (<code>cd</code>) and accessing inodes.</li>
      <li><strong>Umask:</strong> Subtracts bits from default maximums (666 for regular files, 777 for directories). A umask of <code>027</code> yields <code>640</code> for files and <code>750</code> for directories.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 3.2: Linux Standard File Permission Triad, Octal Mapping & Umask Logic</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">LINUX FILE PERMISSIONS (OCTAL BITMASK & UMASK)</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Permission Triad: User (Owner) | Group | Others</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">USER (Owner): rwx (4+2+1=7)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">r = 4 (Read: view contents)</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">w = 2 (Write: modify contents)</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">x = 1 (Execute: run / cd into dir)</text>
    <text x="65" y="205" fill="#fde047" font-size="9" font-family="monospace">chmod 755 script.sh</text>

    <rect x="310" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="430" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">GROUP: r-x (4+0+1=5)</text>
    <text x="325" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Applies to users in the group</text>
    <text x="325" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">chown owner:group file</text>
    <text x="325" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">chgrp devops /var/www</text>
    <text x="325" y="205" fill="#a7f3d0" font-size="9" font-family="monospace">chmod g+w,o-rwx file</text>

    <rect x="570" y="90" width="280" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="710" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">UMASK CALCULATION</text>
    <text x="585" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">Base Files: 666 (rw-rw-rw-)</text>
    <text x="585" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">Base Dirs:  777 (rwxrwxrwx)</text>
    <text x="585" y="180" fill="#fbbf24" font-size="8.5" font-family="monospace">Default Umask 022 -> File: 644, Dir: 755</text>
    <text x="585" y="205" fill="#fca5a5" font-size="8.5" font-family="monospace">Umask 027 -> File: 640, Dir: 750</text>
    
</svg>"""
    aliases = """alias perm='stat -c "%a %n" *'
umask 027"""
    checklist = [('LFCS', 'Can you calculate octal permissions and apply them with chmod?', 'chmod 640 file && stat -c %a file'), ('LFCS', 'Can you configure umask in /etc/profile or ~/.bashrc?', 'umask 027'), ('LFCS', 'Can you change both owner and group recursively?', 'chown -R user:group /target')]
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
      Special permissions extend the standard DAC permissions for specific operational security patterns.
    </p>
    <ul>
      <li><strong>SUID (4000):</strong> Executes as the file owner rather than the calling user (e.g. <code>passwd</code> writing to <code>/etc/shadow</code>).</li>
      <li><strong>SGID (2000):</strong> On files, executes with group privileges. On directories, newly created files automatically inherit the parent directory's group.</li>
      <li><strong>Sticky Bit (1000):</strong> Appended to shared directories like <code>/tmp</code> so users cannot delete or rename each other's files.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 4.2: Linux Special Permissions (SUID, SGID, Sticky Bit) Mechanics</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#f43f5e" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">SPECIAL PERMISSIONS: SUID, SGID & STICKY BIT</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Octal 4000, 2000, 1000 Bitmasks</text>
    </g>
    
    <rect x="50" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="175" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SUID (Set User ID: 4000)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Executes with file owner's privileges</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Example: <code>/usr/bin/passwd</code> (rwsr-xr-x)</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">chmod u+s /path/to/binary</text>
    <text x="65" y="205" fill="#cbd5e1" font-size="8" font-family="sans-serif">Symbol: 's' (or 'S' if owner not executable)</text>

    <rect x="325" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="450" y="115" fill="#fde047" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SGID (Set Group ID: 2000)</text>
    <text x="340" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• On directory: new files inherit dir group</text>
    <text x="340" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Crucial for shared team folders!</text>
    <text x="340" y="180" fill="#38bdf8" font-size="8.5" font-family="monospace">chmod g+s /shared/team</text>
    <text x="340" y="205" fill="#cbd5e1" font-size="8" font-family="sans-serif">Octal: <code>chmod 2775 /shared/team</code></text>

    <rect x="600" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="725" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">STICKY BIT (1000)</text>
    <text x="615" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Prevents users from deleting others' files</text>
    <text x="615" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Only file owner or root can remove</text>
    <text x="615" y="180" fill="#34d399" font-size="8.5" font-family="monospace">chmod +t /tmp</text>
    <text x="615" y="205" fill="#cbd5e1" font-size="8" font-family="sans-serif">Representation: <code>drwxrwxrwt</code> (1777)</text>
    
</svg>"""
    aliases = """find / -perm -4000 -type f 2>/dev/null # Find SUID binaries"""
    checklist = [('LFCS', 'Can you configure SGID on a directory for team collaboration?', 'chmod 2775 /dir && chgrp team /dir'), ('LFCS', 'Can you audit all SUID binaries on the filesystem?', 'find / -perm -4000 2>/dev/null'), ('LFCS', "Can you explain the difference between 's' and 'S' in permission strings?", "'s' means executable bit was set; 'S' means it was not")]
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
      Efficient terminal editing using Vim and pager mastery (<code>less</code>) prevents getting bogged down when reviewing config files:
    </p>
    <ul>
      <li>Set YAML formatting in <code>~/.vimrc</code>: <code>set tabstop=2 shiftwidth=2 expandtab</code>.</li>
      <li>In <code>less</code>: <code>/keyword</code> searches forward; <code>?keyword</code> searches backward; <code>n</code> / <code>N</code> cycles matches; <code>G</code> goes to EOF.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 5.2: Vim Modal State Architecture & High-Speed Keyboard Navigation</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">VIM MODAL ARCHITECTURE & TERMINAL NAVIGATION</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Modes, Motion Vectors & Productivity Shortcuts</text>
    </g>
    
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">NORMAL MODE</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">dd: delete line</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">yy / p: yank / paste</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">u / Ctrl-r: undo / redo</text>
    <text x="65" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">/pattern: search</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="340" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">INSERT MODE</text>
    <text x="265" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">i: insert before cursor</text>
    <text x="265" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">a: append after cursor</text>
    <text x="265" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">o: open new line below</text>
    <text x="265" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">Esc: return to Normal</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="540" y="115" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">VISUAL MODE</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">v: character selection</text>
    <text x="465" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">V: line selection</text>
    <text x="465" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">Ctrl-v: block select</text>
    <text x="465" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">&gt; / &lt;: indent / unindent</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="750" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">COMMAND MODE (:)</text>
    <text x="665" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">:w / :q!: save / quit</text>
    <text x="665" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">:%s/old/new/g: replace</text>
    <text x="665" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">:set tabstop=2 shiftwidth=2 expandtab</text>
    <text x="665" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">:set nu: line numbers</text>
    
</svg>"""
    aliases = """echo 'set ts=2 sw=2 et' >> ~/.vimrc"""
    checklist = [('LFCS', 'Can you configure ~/.vimrc for optimal 2-space YAML editing?', 'set tabstop=2 shiftwidth=2 expandtab'), ('LFCS', 'Can you execute search and replace globally across an open file in vim?', ':%s/foo/bar/g')]
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
      Week 1 consolidation synthesizes file hierarchies, inode links, standard and special permissions, umask calculations, and security auditing to ensure total confidence on the Linux CLI.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 6.2: Linux Security & Permission Auditing Framework</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#10b981" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">WEEK 1 CONSOLIDATION & PERMISSION AUDIT FLOW</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Security Verification Matrix</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">AUDIT SUID / SGID</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">find / -perm /6000 -type f</text>
    <text x="65" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Finds all binaries with SUID or SGID</text>
    <text x="65" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">chmod -s /untrusted/binary</text>
    <text x="65" y="205" fill="#fca5a5" font-size="8.5" font-family="sans-serif">Strips special execution privileges</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">AUDIT PERMISSIONS</text>
    <text x="325" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">find /dir -perm 777 -type f</text>
    <text x="325" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Locates dangerous world-writable files</text>
    <text x="325" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">find / -nouser -o -nogroup</text>
    <text x="325" y="205" fill="#fef3c7" font-size="8.5" font-family="sans-serif">Finds orphaned files from deleted users</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">INODE &amp; LINK INTEGRITY</text>
    <text x="595" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">find / -xtype l 2>/dev/null</text>
    <text x="595" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Discovers broken symbolic links</text>
    <text x="595" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">df -i</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Verifies filesystem inode availability</text>
    
</svg>"""
    aliases = """alias audit_perm='find . -perm /002 -type f'"""
    checklist = [('LFCS', 'Can you audit and remediate world-writable files across a directory tree?', 'find /target -perm -002 -exec chmod o-w {} +'), ('LFCS', 'Can you identify and prune broken symlinks across a filesystem?', 'find . -xtype l -delete')]
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
