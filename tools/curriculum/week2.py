"""
Curriculum Content: Week 2 (Days 1 to 6)
Day 1: ReplicaSets & Self-Healing Controllers | File Searching with Find & Locate
Day 2: Deployments, Rollouts & Revisions | Text Processing: Grep & Regex
Day 3: Services: ClusterIP, NodePort & LoadBalancer | Sed & Awk Fundamentals
Day 4: Namespaces & DNS Resolution Inside Clusters | I/O Redirection & Stream Multiplexing
Day 5: Kubectl Explain & Declarative Workflow | Archiving, Compression & Remote Backups
Day 6: Week 2 Speed Drills & Controller Triathlon | Week 2 Speed Drills & Git Version Control
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    # Day 1: ReplicaSets & Find/Locate
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "REPLICASET RECONCILIATION LOOP & SELECTOR ARCHITECTURE", "Desired State vs Actual State Synchronization", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="230" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="165" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">REPLICASET SPEC</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.8" font-family="monospace">replicas: 3</text>
    <text x="65" y="160" fill="#fde047" font-size="8.8" font-family="monospace">selector:</text>
    <text x="75" y="175" fill="#fde047" font-size="8.5" font-family="monospace">matchLabels:</text>
    <text x="85" y="190" fill="#fde047" font-size="8.5" font-family="monospace">app: web-store</text>
    <text x="65" y="210" fill="#94a3b8" font-size="8" font-family="sans-serif">Matches pod labels in same namespace</text>

    <rect x="310" y="90" width="220" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="420" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">ACTIVE MANAGED PODS</text>
    <rect x="325" y="130" width="190" height="25" rx="4" fill="#065f46" stroke="#34d399"/>
    <text x="420" y="147" fill="#ffffff" font-size="8.8" text-anchor="middle" font-family="monospace">web-store-a1 (labels: app=web-store)</text>
    <rect x="325" y="160" width="190" height="25" rx="4" fill="#065f46" stroke="#34d399"/>
    <text x="420" y="177" fill="#ffffff" font-size="8.8" text-anchor="middle" font-family="monospace">web-store-b2 (labels: app=web-store)</text>
    <rect x="325" y="190" width="190" height="25" rx="4" fill="#065f46" stroke="#34d399"/>
    <text x="420" y="207" fill="#ffffff" font-size="8.8" text-anchor="middle" font-family="monospace">web-store-c3 (labels: app=web-store)</text>

    <rect x="560" y="90" width="290" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="705" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SELF-HEALING CONTROLLER ACTION</text>
    <text x="575" y="140" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• If Pod web-store-a1 dies: Actual (2) &lt; Desired (3)</text>
    <text x="575" y="158" fill="#4ade80" font-size="8.5" font-family="sans-serif">  -> RS Controller immediately spawns replacement!</text>
    <text x="575" y="180" fill="#fde047" font-size="8.5" font-family="sans-serif">• If someone changes pod label:</text>
    <text x="575" y="198" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">  -> Pod is orphaned; RS spawns a new one to reach 3!</text>
    """, "Figure 1.1: ReplicaSet Selector Matching Loop & Self-Healing Action")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX FILE SEARCH ARCHITECTURE: FIND VS LOCATE", "Live Filesystem Traversal vs Pre-Indexed Database", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">FIND: Real-Time Inode Traversal</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">find /var/log -type f -mtime -2 -size +10M</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">find / -name "*.conf" -perm 644 -exec ...</text>
    <text x="65" y="185" fill="#34d399" font-size="8.5" font-family="sans-serif">• 100% accurate; queries disk in real-time</text>
    <text x="65" y="205" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Slower on huge disks; accepts complex expressions</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">LOCATE: Indexed Database Query</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">locate '/etc/systemd/*.conf' # Quote globs!</text>
    <text x="465" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">sudo updatedb   # Re-indexes locate database</text>
    <text x="465" y="185" fill="#fde047" font-size="8.5" font-family="sans-serif">• Lightning fast; instant lookups across millions of files</text>
    <text x="465" y="205" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• Stale until updatedb runs (new files not indexed immediately)</text>
    """, "Figure 1.2: Linux Find (Live Tree Traversal) vs Locate (Binary Index Database)")

    cka_theory = """
    <p>
      The <strong>ReplicaSet</strong> ensures a specified number of Pod replicas match a label selector at all times. In modern Kubernetes, administrators rarely create ReplicaSets directly; they use <strong>Deployments</strong>, which manage ReplicaSets declaratively.
    </p>
    <ul>
      <li><strong>MatchLabels:</strong> Must strictly match <code>template.metadata.labels</code> or admission is rejected.</li>
      <li><strong>Pod Adoption &amp; Orphanage:</strong> ReplicaSets manage pods based solely on label matching, not creation origin. Changing a pod's label causes the ReplicaSet to spawn a replacement.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Locating configuration files and auditing file assets under time constraints requires fluent <code>find</code> and <code>locate</code> usage.
    </p>
    <ul>
      <li><strong>Time predicates:</strong> <code>-mtime -2</code> (modified &lt; 48 hours ago), <code>-mmin -30</code> (modified &lt; 30 minutes ago).</li>
      <li><strong>Size predicates:</strong> <code>-size +50M</code> (greater than 50 Megabytes), <code>-size -1G</code>.</li>
      <li><strong>Actions:</strong> <code>-exec chmod 644 {} +</code> (batches arguments for high speed).</li>
      <li><strong>Locate &amp; Shell Globbing Trap:</strong> When querying patterns with wildcards, always quote arguments (e.g. <code>locate '/etc/systemd/*.conf'</code>). Unquoted wildcards cause Bash to expand the glob before execution, causing <code>plocate</code> multi-argument AND matching to return zero results.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias krs='kubectl get rs -o wide'\nalias kscale='kubectl scale rs --replicas'",
        "lfcs_aliases": "alias fconf='find /etc -name \"*.conf\" 2>/dev/null'",
        "checklist": [
            ("CKA", "Can you scale a ReplicaSet up and down imperatively and declaratively?", "kubectl scale rs <name> --replicas=5"),
            ("CKA", "Do you understand what happens when a managed pod label is removed?", "ReplicaSet detects deficit and spawns new pod"),
            ("LFCS", "Can you find all files modified in the last 60 minutes over 10MB?", "find / -type f -mmin -60 -size +10M 2>/dev/null"),
            ("LFCS", "Can you update the locate database and search with wildcards safely?", "sudo updatedb && locate '/etc/systemd/*.conf' (always quote wildcards)"),
        ]
    }

def get_day_2():
    # Day 2: Deployments, Rollouts & Revisions | Grep & Regex
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "DEPLOYMENT ROLLING UPDATE & REVISION HISTORY", "Zero-Downtime Releases via Dual ReplicaSet Scaling", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="220" height="135" rx="6" fill="#1e293b" stroke="#60a5fa"/>
    <text x="160" y="115" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">DEPLOYMENT SPEC</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">strategy: RollingUpdate</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">maxSurge: 25%</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">maxUnavailable: 25%</text>
    <text x="65" y="205" fill="#fde047" font-size="8.5" font-family="monospace">revisionHistoryLimit: 10</text>

    <rect x="300" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="420" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">OLD RS (v1: nginx:1.24)</text>
    <text x="315" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Scale down: 4 -> 3 -> 2 -> 1 -> 0</text>
    <text x="315" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Pods gracefully terminate (preStop)</text>
    <text x="315" y="185" fill="#cbd5e1" font-size="8.5" font-family="monospace">pod-v1-abc1 (Terminating)</text>
    <text x="315" y="205" fill="#fca5a5" font-size="8" font-family="sans-serif">Retained for instant rollback capability!</text>

    <rect x="570" y="90" width="280" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="710" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">NEW RS (v2: nginx:1.25)</text>
    <text x="585" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Scale up: 0 -> 1 -> 2 -> 3 -> 4</text>
    <text x="585" y="160" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Wait for Readiness Probes to pass</text>
    <text x="585" y="185" fill="#cbd5e1" font-size="8.5" font-family="monospace">pod-v2-xyz9 (Running &amp; Ready)</text>
    <text x="585" y="205" fill="#38bdf8" font-size="8" font-family="monospace">kubectl rollout undo deploy &lt;name&gt;</text>
    """, "Figure 2.1: Kubernetes Deployment RollingUpdate Mechanics & Rollout Controller")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "TEXT PROCESSING: GREP & POSIX REGULAR EXPRESSIONS", "Pattern Matching with BRE vs ERE", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">GREP FLAGS (High-Speed)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">grep -i "keyword" file</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">grep -v "^#" file | grep -v "^$"</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">grep -rE "(error|fatal)" /var/log</text>
    <text x="65" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">grep -n -C 3 "Failed" journal.txt</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">POSIX REGEX ANCHORS</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">^: Start of line</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">$: End of line</text>
    <text x="325" y="180" fill="#fde047" font-size="8.5" font-family="monospace">[0-9]{1,3}\.[0-9]{1,3}...: IP match</text>
    <text x="325" y="200" fill="#fde047" font-size="8.5" font-family="monospace">[^:]: Negated character class</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">ERE VS BRE RULES</text>
    <text x="595" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• BRE (grep): \( \) \+ \? require escaping</text>
    <text x="595" y="165" fill="#34d399" font-size="8.5" font-family="sans-serif">• ERE (grep -E / egrep):</text>
    <text x="605" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">+ (1 or more), ? (0 or 1), | (OR)</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Always use <code>grep -E</code> for complex regex!</text>
    """, "Figure 2.2: Linux Grep Pattern Matching & POSIX Regular Expressions")

    cka_theory = """
    <p>
      Deployments provide declarative updates for Pods and ReplicaSets.
    </p>
    <ul>
      <li><strong>Rolling Updates:</strong> Controlled by <code>maxSurge</code> (extra pods allowed above desired) and <code>maxUnavailable</code> (allowed deficit).</li>
      <li><strong>Rollout Management:</strong>
        <pre><code>kubectl rollout status deployment/my-deploy
kubectl rollout history deployment/my-deploy
kubectl rollout undo deployment/my-deploy --to-revision=2</code></pre>
      </li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Mastering <code>grep</code> is vital for isolating failures in system logs and stripping comments from config files.
    </p>
    <ul>
      <li>Strip comments and blank lines: <code>grep -Ev '^(#|$)' /etc/file.conf</code></li>
      <li>Context display: <code>grep -B 2 -A 4 "CRITICAL" /var/log/syslog</code></li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kroll='kubectl rollout status'\nalias kundo='kubectl rollout undo'",
        "lfcs_aliases": "alias nocomment='grep -Ev \"^(#|;|//|$)\"'",
        "checklist": [
            ("CKA", "Can you update an image in a deployment and check rollout status?", "kubectl set image deploy/<name> <c>=<img:tag> && kubectl rollout status deploy/<name>"),
            ("CKA", "Can you rollback a deployment to a previous revision?", "kubectl rollout undo deploy/<name> --to-revision=<n>"),
            ("LFCS", "Can you extract all non-comment active lines from a system config file?", "grep -Ev '^(#|$)' /etc/ssh/sshd_config"),
            ("LFCS", "Can you match IPv4 addresses using extended regular expressions?", "grep -E '([0-9]{1,3}\\.){3}[0-9]{1,3}'"),
        ]
    }

def get_day_3():
    # Day 3: Services | Sed & Awk
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES SERVICE TYPES & TRAFFIC ROUTING", "ClusterIP, NodePort & LoadBalancer", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="175" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. CLUSTERIP (Default)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Internal virtual IP inside cluster</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Inaccessible from external network</text>
    <text x="65" y="180" fill="#34d399" font-size="8.5" font-family="monospace">spec.type: ClusterIP</text>
    <text x="65" y="200" fill="#a7f3d0" font-size="8" font-family="monospace">Port: 80 -> TargetPort: 8080</text>

    <rect x="325" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="450" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. NODEPORT (30000-32767)</text>
    <text x="340" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Exposes port on every worker node</text>
    <text x="340" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Routes: NodeIP:NodePort -> Pod</text>
    <text x="340" y="180" fill="#fde047" font-size="8.5" font-family="monospace">spec.type: NodePort</text>
    <text x="340" y="200" fill="#fef3c7" font-size="8" font-family="monospace">NodePort: 31234 -> Port 80</text>

    <rect x="600" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="725" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. LOADBALANCER</text>
    <text x="615" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Provisions cloud provider load balancer</text>
    <text x="615" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Automatically configures NodePort</text>
    <text x="615" y="180" fill="#38bdf8" font-size="8.5" font-family="monospace">spec.type: LoadBalancer</text>
    <text x="615" y="200" fill="#7dd3fc" font-size="8" font-family="monospace">External-IP: 20.42.18.9</text>
    """, "Figure 3.1: Kubernetes Service Topologies & Endpoint Dispatch")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "STREAM TRANSFORMATION: SED & AWK ARCHITECTURE", "Non-Interactive Stream Editing & Field Extraction", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SED: Stream Editor (Line-Oriented)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">sed -i 's/foo/bar/g' /path/to/file</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">sed '/^#/d; /^$/d' config.conf</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">sed -n '10,25p' log.txt   # Print lines 10 to 25</text>
    <text x="65" y="205" fill="#34d399" font-size="8" font-family="sans-serif">Cycle: Read line -> Pattern Space -> Apply script -> Output</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">AWK: Column &amp; Report Processing</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">awk -F: '$3 &gt;= 1000 {{print $1, $3, $7}}' /etc/passwd</text>
    <text x="465" y="160" fill="#fde047" font-size="8.5" font-family="monospace">df -h | awk '$5 &gt; 80 {{print $1, $5}}'</text>
    <text x="465" y="185" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <code>$1, $2, ... $NF</code> refer to columns (fields)</text>
    <text x="465" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• <code>NR</code> is row number; <code>NF</code> is total column count</text>
    """, "Figure 3.2: Sed Pattern Replacement Cycle & Awk Field Parsing Pipeline")

    cka_theory = """
    <p>
      Services route traffic to Pods matching their selector. The <strong>EndpointSlice</strong> (or Endpoints) object lists healthy Pod IPs.
    </p>
    <ul>
      <li><strong>TargetPort vs Port:</strong> <code>port</code> is the Service port; <code>targetPort</code> is the port exposed on the Pod container.</li>
      <li><strong>Troubleshooting Tip:</strong> If <code>kubectl get endpoints &lt;svc&gt;</code> has no IPs, the Service selector does not match the Pod labels, or the Pods failed their Readiness Probes!</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      <code>sed</code> and <code>awk</code> are indispensable for scripting text manipulation in Linux administration.
    </p>
    <ul>
      <li><code>sed -i.bak 's/old/new/g' file</code>: Edits file in-place while saving a backup.</li>
      <li><code>awk -F',' '{sum += $2} END {print sum}' data.csv</code>: Calculates sums and columnar statistics.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias ksvc='kubectl get svc,endpoints'",
        "lfcs_aliases": "alias users='awk -F: \"$3 >= 1000 {print $1}\" /etc/passwd'",
        "checklist": [
            ("CKA", "Can you expose a deployment as a NodePort service imperatively?", "kubectl expose deploy <name> --type=NodePort --port=80"),
            ("CKA", "Can you inspect Endpoints to verify pod discovery?", "kubectl get endpoints <service-name>"),
            ("LFCS", "Can you replace all occurrences of a string in a config file using sed in-place?", "sed -i 's/PORT=80/PORT=8080/' /etc/app.conf"),
            ("LFCS", "Can you filter users with UID >= 1000 using awk?", "awk -F: '$3 >= 1000 {print $1, $3}' /etc/passwd"),
        ]
    }

def get_day_4():
    # Day 4: Namespaces & DNS | I/O Redirection
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES CLUSTER DNS RESOLUTION HIERARCHY", "FQDN Format: <service>.<namespace>.svc.cluster.local", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">POD /etc/resolv.conf</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">nameserver 10.96.0.10</text>
    <text x="65" y="160" fill="#fde047" font-size="8" font-family="monospace">search default.svc.cluster.local</text>
    <text x="65" y="175" fill="#fde047" font-size="8" font-family="monospace">       svc.cluster.local</text>
    <text x="65" y="190" fill="#fde047" font-size="8" font-family="monospace">       cluster.local</text>
    <text x="65" y="210" fill="#94a3b8" font-size="8" font-family="sans-serif">options ndots:5</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="435" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">COREDNS (kube-system)</text>
    <text x="325" y="140" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• CoreDNS static/deployment pods</text>
    <text x="325" y="160" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Watches Service &amp; Endpoint state</text>
    <text x="325" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">dig @10.96.0.10 web.prod.svc...</text>
    <text x="325" y="205" fill="#38bdf8" font-size="8" font-family="monospace">kubectl get pods -n kube-system -l k8s-app=kube-dns</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="715" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">CROSS-NAMESPACE CALLS</text>
    <text x="595" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Same namespace: <code>curl web-svc</code></text>
    <text x="595" y="165" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Across namespaces:</text>
    <text x="605" y="185" fill="#fde047" font-size="8.5" font-family="monospace">curl web-svc.finance.svc</text>
    <text x="595" y="205" fill="#4ade80" font-size="8" font-family="sans-serif">Fully Qualified: web-svc.finance.svc.cluster.local</text>
    """, "Figure 4.1: Kubernetes CoreDNS Service Discovery & FQDN Architecture")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX I/O REDIRECTION & STREAM MULTIPLEXING", "File Descriptors: 0 (stdin), 1 (stdout), 2 (stderr)", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">STANDARD REDIRECTIONS</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">&gt; file : Overwrite stdout</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">&gt;&gt; file : Append stdout</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">&lt; file : Read stdin</text>
    <text x="65" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">&lt;&lt;EOF : Here-document block</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="435" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">ERROR &amp; COMBINED</text>
    <text x="325" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">2&gt; /dev/null : Discard errors</text>
    <text x="325" y="160" fill="#fca5a5" font-size="8.5" font-family="monospace">2&gt;&amp;1 : Merge stderr into stdout</text>
    <text x="325" y="180" fill="#fca5a5" font-size="8.5" font-family="monospace">&amp;&gt; file : Redirect both to file</text>
    <text x="325" y="200" fill="#fde047" font-size="8.5" font-family="monospace">cmd |&amp; grep : Pipe both streams</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">PIPELINES &amp; TEE</text>
    <text x="595" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">cmd1 | cmd2 : Pipe stdout to stdin</text>
    <text x="595" y="160" fill="#a7f3d0" font-size="8.5" font-family="monospace">cmd | tee -a log.txt</text>
    <text x="595" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Splices output to screen AND file</text>
    <text x="595" y="205" fill="#fde047" font-size="8.5" font-family="monospace">echo "cfg" | sudo tee /etc/cfg</text>
    """, "Figure 4.2: Linux File Descriptor Redirection, Error Separation & Multiplexing")

    cka_theory = """
    <p>
      Kubernetes CoreDNS provides automatic DNS records for Services and Pods.
    </p>
    <ul>
      <li>Service FQDN: <code>&lt;service-name&gt;.&lt;namespace&gt;.svc.cluster.local</code></li>
      <li>Pod DNS: <code>&lt;pod-ip-dashed&gt;.&lt;namespace&gt;.pod.cluster.local</code></li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Stream redirection controls standard input (0), standard output (1), and standard error (2).
    </p>
    <ul>
      <li><code>command &> /var/log/output.log</code> redirects both stdout and stderr.</li>
      <li><code>tee -a file</code> appends output while preserving stdout on the terminal.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kns='kubectl config set-context --current --namespace'",
        "lfcs_aliases": "alias nullerr='2>/dev/null'",
        "checklist": [
            ("CKA", "Can you test DNS resolution from within a cluster using busybox?", "kubectl run dns-test --image=busybox:1.36 --rm -it -- nslookup <svc>"),
            ("CKA", "Can you resolve services across different namespaces?", "<svc-name>.<namespace>.svc.cluster.local"),
            ("LFCS", "Can you separate stdout and stderr into two distinct files?", "cmd > out.txt 2> err.txt"),
            ("LFCS", "Can you write privileged files using sudo tee?", "echo 'data' | sudo tee /etc/privileged.conf"),
        ]
    }

def get_day_5():
    # Day 5: Kubectl Explain | Archiving & Compression
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBECTL EXPLAIN SCHEMA RECURSION ENGINE", "Offline API Specification Navigator", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">RECURSIVE DRILLDOWN</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">k explain pod.spec.containers</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.8" font-family="monospace">k explain pod.spec.containers.livenessProbe</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.8" font-family="monospace">k explain deploy.spec.strategy.rollingUpdate</text>
    <text x="65" y="200" fill="#fde047" font-size="8.5" font-family="monospace">k explain service.spec --recursive | grep -A5 type</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">EXAM USAGE TACTICS</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• When unsure of YAML casing or required subfields:</text>
    <text x="465" y="160" fill="#38bdf8" font-size="8.5" font-family="monospace">kubectl explain &lt;type&gt;.&lt;field&gt;</text>
    <text x="465" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Displays field type: <code>&lt;string&gt;</code>, <code>&lt;[]Object&gt;</code>, <code>&lt;boolean&gt;</code></text>
    <text x="465" y="200" fill="#34d399" font-size="8.5" font-family="sans-serif">• 100% available in offline / air-gapped exam terminals!</text>
    """, "Figure 5.1: Kubectl Explain Offline API Specification Navigation Tree")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX ARCHIVING, COMPRESSION & RSYNC DELTA PIPELINE", "Tar, Gzip, Bzip2, XZ & Remote Sync", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TAR ARCHIVING FLAGS</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">tar -czvf archive.tar.gz /dir</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">tar -xjvf archive.tar.bz2 /dir</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">tar -xJvf archive.tar.xz /dir</text>
    <text x="65" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">tar -tf archive.tar.gz  # List</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">COMPRESSION ALGORITHMS</text>
    <text x="325" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <strong>gzip (-z):</strong> Fastest, lowest CPU usage</text>
    <text x="325" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <strong>bzip2 (-j):</strong> Higher compression ratio</text>
    <text x="325" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <strong>xz (-J):</strong> Maximum compression</text>
    <text x="325" y="200" fill="#fde047" font-size="8.5" font-family="monospace">zcat, bzcat, xzcat (view without unpacking)</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">RSYNC DELTA SYNC</text>
    <text x="595" y="140" fill="#a7f3d0" font-size="8.5" font-family="monospace">rsync -avz --delete /src/ user@dest:/dst</text>
    <text x="595" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <code>-a</code> (archive): preserves perms, symlinks, times</text>
    <text x="595" y="180" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• Trailing slash on <code>/src/</code> copies contents</text>
    <text x="595" y="200" fill="#fde047" font-size="8.5" font-family="monospace">rsync -e 'ssh -p 2222' ...</text>
    """, "Figure 5.2: Linux Compression Hierarchy & Rsync Delta-Transfer Engine")

    cka_theory = """
    <p>
      <code>kubectl explain</code> is your built-in offline reference. Use it to check manifest schemas without leaving the shell:
    </p>
    <ul>
      <li>Check required fields: <code>kubectl explain pod.spec</code></li>
      <li>Examine probe configurations: <code>kubectl explain pod.spec.containers.livenessProbe.httpGet</code></li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Archiving preserves permissions and directory structure during migrations and backups.
    </p>
    <ul>
      <li>Create gzip tarball: <code>tar -czvf /backup/app.tar.gz /srv/app</code></li>
      <li>Extract to specific target: <code>tar -xzvf /backup/app.tar.gz -C /opt/restore</code></li>
      <li>Delta backup with Rsync: <code>rsync -avh --progress /var/www/ /backup/www/</code></li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kexp='kubectl explain'",
        "lfcs_aliases": "alias untar='tar -xvf'",
        "checklist": [
            ("CKA", "Can you use kubectl explain to locate field names and types quickly?", "kubectl explain pod.spec.tolerations"),
            ("CKA", "Can you query a deeply nested subfield with recursive explain?", "kubectl explain deployment.spec.strategy --recursive"),
            ("LFCS", "Can you create a compressed bzip2 archive preserving permissions?", "tar -cjvf backup.tar.bz2 /path"),
            ("LFCS", "Can you sync directories locally or remotely using rsync?", "rsync -avz --delete src/ dst/"),
        ]
    }

def get_day_6():
    # Day 6: Week 2 Speed Drills | Git Version Control
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "WEEK 2 CONTROLLER TRIATHLON WORKFLOW", "Deployment -> ReplicaSet -> Pods -> Service -> Ingress", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="60" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="140" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Deployment</text>
    <text x="140" y="135" fill="#93c5fd" font-size="8.5" text-anchor="middle" font-family="monospace">Rollout &amp; Spec</text>

    <rect x="260" y="90" width="180" height="60" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="350" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">ReplicaSet</text>
    <text x="350" y="135" fill="#a7f3d0" font-size="8.5" text-anchor="middle" font-family="monospace">Replicas Count (3)</text>

    <rect x="470" y="90" width="180" height="60" rx="6" fill="#78350f" stroke="#fbbf24"/>
    <text x="560" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Pods (x3)</text>
    <text x="560" y="135" fill="#fef3c7" font-size="8.5" text-anchor="middle" font-family="monospace">app=web, env=prod</text>

    <rect x="680" y="90" width="170" height="60" rx="6" fill="#881337" stroke="#f43f5e"/>
    <text x="765" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Service &amp; Endpoints</text>
    <text x="765" y="135" fill="#fca5a5" font-size="8.5" text-anchor="middle" font-family="monospace">VIP &amp; TargetPort</text>

    {code_box(50, 160, 800, 65, "Triathlon Rapid Sequence:\n1. k create deploy web --image=nginx:alpine --replicas=3 $do > web.yaml\n2. k expose deploy web --port=80 --target-port=80 --type=NodePort $do > svc.yaml\n3. k apply -f web.yaml -f svc.yaml && k get pods,svc,endpoints -l app=web")}
    """, "Figure 6.1: Week 2 Workload Triathlon Execution Sequence")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "GIT ARCHITECTURE & VERSION CONTROL STATE MACHINE", "Working Directory, Staging Index & Local Repository", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">WORKING DIRECTORY</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Untracked &amp; modified files</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">git status</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">git diff</text>
    <text x="65" y="200" fill="#fca5a5" font-size="8.5" font-family="monospace">git checkout -- file</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">STAGING INDEX (CACHE)</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">git add file / git add -A</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">git diff --staged</text>
    <text x="325" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Prepares snapshot for commit</text>
    <text x="325" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">git reset HEAD file</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">LOCAL REPOSITORY (.git)</text>
    <text x="595" y="140" fill="#34d399" font-size="8.5" font-family="monospace">git commit -m "commit message"</text>
    <text x="595" y="160" fill="#34d399" font-size="8.5" font-family="monospace">git log --oneline --graph</text>
    <text x="595" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">git branch -M main</text>
    <text x="595" y="200" fill="#a7f3d0" font-size="8.5" font-family="monospace">git checkout -b feature</text>
    """, "Figure 6.2: Git Three-State Architecture (Working Tree, Index, Repository)")

    cka_theory = """
    <p>
      Week 2 integration requires synthesizing deployments, service routing, CoreDNS resolution, and declarative management into a fast, repeatable exam routine.
    </p>
    """

    lfcs_theory = """
    <p>
      Week 2 consolidation tests advanced stream editing (<code>sed</code>, <code>awk</code>), stream redirection, tar/compression, and git version control fundamentals for infrastructure as code.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kall='kubectl get deploy,rs,po,svc,ep'",
        "lfcs_aliases": "alias glog='git log --oneline --graph --all'",
        "checklist": [
            ("CKA", "Can you create a Deployment, expose it as NodePort, and test it in under 4 minutes?", "kubectl create deploy && kubectl expose"),
            ("CKA", "Can you perform a rolling update and immediate rollback?", "kubectl rollout undo deploy/<name>"),
            ("LFCS", "Can you initialize a git repository, commit changes, and switch branches?", "git init && git add . && git commit -m 'init'"),
            ("LFCS", "Can you archive a directory with tar and send it over SSH or rsync?", "tar -czf - /dir | ssh user@remote 'tar -xzf - -C /dst'"),
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
