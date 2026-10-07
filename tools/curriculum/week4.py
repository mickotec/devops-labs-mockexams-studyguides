"""
Curriculum Content: Week 4 (Days 1 to 6)
Day 1: Commands & Arguments (Docker vs K8s) | Journald & System Log File Analysis
Day 2: ConfigMaps & App Configuration | Task Scheduling with Cron & At
Day 3: Secrets Management & Encryption at Rest | Package Managers (APT, DNF/YUM & RPM)
Day 4: Autoscaling: HPA, VPA & In-Place Resize | Compiling Software from Source Code
Day 5: Admission Controllers & Validating Webhooks | Bash Automation & Scripting
Day 6: Week 4 App Lifecycle & Secret Security Drill | Week 4 Automation Triathlon
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    # Day 1: Commands/Args & Journald
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "CONTAINER COMMAND & ARGUMENTS: DOCKER VS KUBERNETES", "Precedence & Parameter Override Mapping", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">DOCKERFILE FIELDS</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">ENTRYPOINT ["/bin/app"]</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">CMD ["--port", "8080"]</text>
    <text x="65" y="185" fill="#fde047" font-size="8.5" font-family="sans-serif">• <code>ENTRYPOINT</code> is the primary executable.</text>
    <text x="65" y="205" fill="#fde047" font-size="8.5" font-family="sans-serif">• <code>CMD</code> provides default arguments that can be overridden.</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">KUBERNETES POD FIELDS (Overrides)</text>
    <text x="465" y="140" fill="#34d399" font-size="8.5" font-family="monospace">command: ["/bin/custom-app"]   # Overrides ENTRYPOINT!</text>
    <text x="465" y="160" fill="#34d399" font-size="8.5" font-family="monospace">args: ["--port", "9090"]       # Overrides CMD!</text>
    <text x="465" y="185" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• ⚠️ CKA Trap: <code>command</code> in K8s overrides Docker <code>ENTRYPOINT</code>!</text>
    <text x="465" y="205" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• ⚠️ <code>args</code> in K8s overrides Docker <code>CMD</code>!</text>
    """, "Figure 1.1: Container Execution Mapping: Dockerfile vs Kubernetes PodSpec")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "SYSTEMD-JOURNALD BINARY LOGGING ARCHITECTURE", "High-Performance Querying & Filter Combinations", "cardDark", "#0f172a", "#10b981")}
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
    """, "Figure 1.2: Systemd Journal Architecture & Query Optimization Engine")

    cka_theory = """
    <p>
      In Kubernetes manifests, <code>command</code> overrides the image's <code>ENTRYPOINT</code>, and <code>args</code> overrides the image's <code>CMD</code>.
    </p>
    <ul>
      <li>Passing a shell command with pipe: <code>command: ["/bin/sh", "-c", "echo hello && sleep 3600"]</code></li>
    </ul>
    """

    lfcs_theory = """
    <p>
      <code>journalctl</code> inspects binary logs managed by <code>systemd-journald</code>.
    </p>
    <ul>
      <li>Filter by unit: <code>journalctl -u sshd -e</code></li>
      <li>Filter by priority level: <code>journalctl -p 3</code> (Errors and worse).</li>
      <li>To persist logs across reboots, create <code>/var/log/journal</code> and restart the daemon.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias krun_cmd='kubectl run test --image=busybox --command -- sh -c'",
        "lfcs_aliases": "alias jerr='journalctl -p err -b --no-pager'",
        "checklist": [
            ("CKA", "Can you override both ENTRYPOINT and CMD in a pod YAML?", "command: [...] and args: [...]"),
            ("LFCS", "Can you configure journald for persistent disk storage?", "Storage=persistent in /etc/systemd/journald.conf"),
            ("LFCS", "Can you filter journal logs for specific service errors in the last 30 minutes?", "journalctl -u <svc> -p err --since '-30m'"),
        ]
    }

def get_day_2():
    # Day 2: ConfigMaps & Cron/At
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "CONFIGMAP INJECTION MECHANISMS", "Environment Variables vs Volume Projections", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">METHOD 1: ENV VARIABLES (envFrom / valueFrom)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">env:</text>
    <text x="75" y="155" fill="#4ade80" font-size="8.5" font-family="monospace">- name: DB_HOST</text>
    <text x="85" y="170" fill="#4ade80" font-size="8.5" font-family="monospace">  valueFrom: {{configMapKeyRef: {{name: app-cm, key: host}}}}</text>
    <text x="65" y="190" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• ⚠️ Static snapshot: CM updates do NOT update env vars in running pod!</text>
    <text x="65" y="205" fill="#94a3b8" font-size="8" font-family="sans-serif">Pod must be restarted to consume new environment values.</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">METHOD 2: VOLUME MOUNTS (Auto-Reloadable)</text>
    <text x="465" y="140" fill="#34d399" font-size="8.5" font-family="monospace">volumes:</text>
    <text x="475" y="155" fill="#34d399" font-size="8.5" font-family="monospace">- name: cfg-vol, configMap: {{name: app-cm}}</text>
    <text x="465" y="170" fill="#34d399" font-size="8.5" font-family="monospace">volumeMounts: [{{name: cfg-vol, mountPath: /etc/config}}]</text>
    <text x="465" y="190" fill="#4ade80" font-size="8.5" font-family="sans-serif">• Automatically updated by kubelet via symlink swap!</text>
    <text x="465" y="205" fill="#fde047" font-size="8.5" font-family="sans-serif">• SubPath mounts do NOT auto-update!</text>
    """, "Figure 2.1: Kubernetes ConfigMap Consumption Patterns: Env vs Volumes")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX TASK SCHEDULING: CRON & AT DAEMONS", "Recurring Crontab Syntax & One-Shot At Queue", "cardDark", "#0f172a", "#10b981")}
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
    """, "Figure 2.2: Linux Automated Task Scheduling: Cron vs At Queue")

    cka_theory = """
    <p>
      ConfigMaps decouple configuration artifacts from container image content.
    </p>
    <ul>
      <li>Create from literal: <code>kubectl create configmap app-cfg --from-literal=APP_MODE=prod</code></li>
      <li>Create from file: <code>kubectl create configmap nginx-cfg --from-file=nginx.conf</code></li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Recurring task scheduling with <code>cron</code> is an LFCS core requirement.
    </p>
    <ul>
      <li>Edit user crontab: <code>crontab -e</code> (never edit <code>/var/spool/cron/crontabs</code> directly).</li>
      <li>System crontab: <code>/etc/crontab</code> contains an extra <code>user</code> column before the command!</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kcm='kubectl create configmap'",
        "lfcs_aliases": "alias mycron='crontab -l'",
        "checklist": [
            ("CKA", "Can you inject a ConfigMap into a Pod as environment variables?", "envFrom.configMapRef"),
            ("CKA", "Can you mount a ConfigMap as a volume directory?", "volumes.configMap and volumeMounts"),
            ("LFCS", "Can you schedule a cron job to run every 15 minutes on weekdays?", "*/15 * * * 1-5 /path/to/cmd"),
            ("LFCS", "Can you queue a one-off task using at?", "at now + 5 minutes"),
        ]
    }

def get_day_3():
    # Day 3: Secrets & Package Managers
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES SECRETS MANAGEMENT & ENCRYPTION AT REST", "Base64 Encoding vs EncryptionConfiguration in ETCD", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="235" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SECRET ENCODING (base64)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">echo -n "pass123" | base64</text>
    <text x="65" y="160" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• ⚠️ Base64 is ENCODING, NOT ENCRYPTION!</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Anyone with API read access can decode:</text>
    <text x="65" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">echo "cGFzczEyMw==" | base64 -d</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">ENCRYPTION AT REST (ETCD)</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">kind: EncryptionConfiguration</text>
    <text x="465" y="155" fill="#34d399" font-size="8.5" font-family="monospace">providers: [{{aescbc: {{keys: [{{name: key1, secret: ...}}]}}}}]</text>
    <text x="465" y="175" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Passed to kube-apiserver:</text>
    <text x="465" y="195" fill="#fbbf24" font-size="8.5" font-family="monospace">--encryption-provider-config=/etc/k8s/enc.yaml</text>
    <text x="465" y="210" fill="#4ade80" font-size="8" font-family="sans-serif">Re-encrypt: <code>kubectl get secrets -A -o json | kubectl replace -f -</code></text>
    """, "Figure 3.1: Kubernetes Secret Security Architecture & ETCD Encryption")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX PACKAGE MANAGEMENT: APT (DEBIAN) VS DNF/YUM (RHEL)", "Repository Architecture & Package Operations", "cardDark", "#0f172a", "#10b981")}
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
    """, "Figure 3.2: Linux Package Management Architecture (APT vs DNF/RPM)")

    cka_theory = """
    <p>
      Kubernetes Secrets store sensitive data (passwords, tokens, keys). By default, etcd stores secrets in plaintext unless EncryptionConfiguration is configured.
    </p>
    <ul>
      <li>Create generic secret: <code>kubectl create secret generic db-pass --from-literal=password=secret123</code></li>
      <li>Create TLS secret: <code>kubectl create secret tls cert-sec --cert=tls.crt --key=tls.key</code></li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Package managers resolve dependencies and track installed files on Linux systems.
    </p>
    <ul>
      <li>Determine which package owns a binary: <code>dpkg -S /usr/bin/git</code> or <code>rpm -qf /usr/bin/git</code>.</li>
      <li>List all files in an installed package: <code>dpkg -L nginx</code> or <code>rpm -ql nginx</code>.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias ksec='kubectl get secret'",
        "lfcs_aliases": "alias owns='dpkg -S'",
        "checklist": [
            ("CKA", "Can you create a Secret from literal and decode it with base64?", "kubectl create secret generic && base64 -d"),
            ("CKA", "Can you mount a secret into a pod as read-only files?", "volumes.secret in pod spec"),
            ("LFCS", "Can you find which package installed a specific command?", "dpkg -S /path/file or rpm -qf /path/file"),
            ("LFCS", "Can you install and query an RPM or DEB package file locally?", "dpkg -i or rpm -ivh"),
        ]
    }

def get_day_4():
    # Day 4: Autoscaling & Source Compilation
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "HORIZONTAL POD AUTOSCALER (HPA) FEEDBACK LOOP", "Metrics Server -> HPA Controller -> Deployment Scale", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="230" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="165" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. METRICS SERVER</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Scrapes kubelet <code>/stats/summary</code></text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">kubectl top nodes</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">kubectl top pods</text>
    <text x="65" y="205" fill="#94a3b8" font-size="8" font-family="sans-serif">Requires resource requests in Pod!</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="435" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. HPA CONTROLLER</text>
    <text x="325" y="140" fill="#34d399" font-size="8.5" font-family="monospace">k autoscale deploy web \</text>
    <text x="325" y="155" fill="#34d399" font-size="8.5" font-family="monospace">  --min=2 --max=10 --cpu-percent=70</text>
    <text x="325" y="175" fill="#fde047" font-size="8" font-family="monospace">Desired = ceil[Current * (Cur% / Tgt%)]</text>
    <text x="325" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">kubectl get hpa</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="715" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. WORKLOAD SCALING</text>
    <text x="595" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Scales Deployment replicas</text>
    <text x="595" y="160" fill="#4ade80" font-size="8.5" font-family="sans-serif">• Pods scale out across cluster</text>
    <text x="595" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Stabilization windows prevent thrashing</text>
    <text x="595" y="205" fill="#38bdf8" font-size="8.5" font-family="monospace">scaleTargetRef: Deployment/web</text>
    """, "Figure 4.1: Kubernetes HPA Autoscaling Control Loop")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "C/C++ SOURCE COMPILATION TOOLCHAIN PIPELINE", "Preprocessing -> Compiling -> Assembling -> Linking", "cardDark", "#0f172a", "#10b981")}
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
    """, "Figure 4.2: Software Compilation Toolchain & Shared Library Management")

    cka_theory = """
    <p>
      The Horizontal Pod Autoscaler (HPA) adjusts the number of pod replicas automatically based on observed CPU/memory metrics.
    </p>
    <ul>
      <li>Crucial requirement: Pods <strong>must have resource requests configured</strong>, otherwise HPA cannot compute percentage utilization and remains in <code>&lt;unknown&gt;</code> state!</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Compiling software from source requires the standard build toolchain (<code>gcc</code>, <code>make</code>, <code>libc-dev</code>).
    </p>
    <ul>
      <li>Inspect binary library dependencies with <code>ldd &lt;binary&gt;</code>.</li>
      <li>Update the dynamic linker library cache with <code>ldconfig</code>.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias khpa='kubectl get hpa'",
        "lfcs_aliases": "alias lddcheck='ldd'",
        "checklist": [
            ("CKA", "Can you configure an HPA to scale a deployment from 2 to 8 replicas at 75% CPU?", "kubectl autoscale deploy <name> --min=2 --max=8 --cpu-percent=75"),
            ("CKA", "Do you understand why HPA shows <unknown> when requests are missing?", "HPA computes percentage against spec.containers.resources.requests"),
            ("LFCS", "Can you compile a C program and inspect shared library linkage?", "gcc -o app app.c && ldd app"),
            ("LFCS", "Can you update shared library paths with ldconfig?", "/etc/ld.so.conf and sudo ldconfig"),
        ]
    }

def get_day_5():
    # Day 5: Admission Controllers & Bash Scripting
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES ADMISSION CONTROLLER PIPELINE", "Mutating Webhook -> Schema Validation -> Validating Webhook", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. AUTH &amp; AUTHZ</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Authentication (x509, SA)</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Authorization (RBAC, Node)</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="sans-serif">Passes valid identity</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="340" y="115" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. MUTATING PHASE</text>
    <text x="265" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Injects sidecars (Istio)</text>
    <text x="265" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Sets default storage class</text>
    <text x="265" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Modifies incoming object</text>
    <text x="265" y="200" fill="#fde047" font-size="8.5" font-family="monospace">MutatingWebhookConfig</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="540" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. VALIDATING PHASE</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Enforces organizational policies</text>
    <text x="465" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Blocks privileged pods</text>
    <text x="465" y="180" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• Can REJECT creation</text>
    <text x="465" y="200" fill="#fde047" font-size="8.5" font-family="monospace">ValidatingWebhookConfig</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="750" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. PERSIST TO ETCD</text>
    <text x="665" y="140" fill="#4ade80" font-size="8.5" font-family="sans-serif">• Written to /registry/</text>
    <text x="665" y="160" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Watchers notified (Kubelet)</text>
    <text x="665" y="180" fill="#38bdf8" font-size="8.5" font-family="monospace">--enable-admission-plugins=...</text>
    <text x="665" y="200" fill="#94a3b8" font-size="8" font-family="sans-serif">Configured in apiserver manifest</text>
    """, "Figure 5.1: Kubernetes Admission Controller Mutating & Validating Webhook Pipeline")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "PRODUCTION BASH AUTOMATION ARCHITECTURE", "Robust Error Trapping, Parameter Expansion & Functions", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="180" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">DEFENSIVE PREAMBLE</text>
    <text x="65" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">#!/bin/bash</text>
    <text x="65" y="160" fill="#fca5a5" font-size="8.5" font-family="monospace">set -euo pipefail</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8" font-family="sans-serif">-e: exit on error | -u: error on unset var</text>
    <text x="65" y="195" fill="#e2e8f0" font-size="8" font-family="sans-serif">-o pipefail: fail if ANY pipe element fails</text>
    <text x="65" y="210" fill="#38bdf8" font-size="8" font-family="monospace">trap 'echo "Error on line $LINENO"' ERR</text>

    <rect x="330" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="455" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">PARAMETER EXPANSION</text>
    <text x="345" y="140" fill="#fde047" font-size="8.5" font-family="monospace">${{VAR:-default}}  # Default if unset</text>
    <text x="345" y="160" fill="#fde047" font-size="8.5" font-family="monospace">${{VAR:?error}}    # Error if unset</text>
    <text x="345" y="180" fill="#fde047" font-size="8.5" font-family="monospace">${{#VAR}}          # String length</text>
    <text x="345" y="200" fill="#fde047" font-size="8.5" font-family="monospace">${{VAR%/*}}        # Strip dirname</text>

    <rect x="600" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="725" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TEST OPERATORS</text>
    <text x="615" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">[[ -f $FILE ]]  # Regular file</text>
    <text x="615" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">[[ -d $DIR ]]   # Directory</text>
    <text x="615" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">[[ -z $STR ]]   # Empty string</text>
    <text x="615" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">[[ $A =~ ^[0-9]+$ ]]  # Regex</text>
    """, "Figure 5.2: Production Bash Scripting Patterns & Defensive Standards")

    cka_theory = """
    <p>
      Admission Controllers intercept requests to the Kubernetes API server prior to persistence in etcd, but after authentication and authorization.
    </p>
    <ul>
      <li>Enable admission plugin: In <code>/etc/kubernetes/manifests/kube-apiserver.yaml</code>, modify <code>--enable-admission-plugins=NodeRestriction,LimitRanger,...</code></li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Reliable sysadmin automation requires robust Bash standards.
    </p>
    <ul>
      <li>Always use <code>set -euo pipefail</code> at the start of every script.</li>
      <li>Clean up temporary files with <code>trap 'rm -rf "$TMPDIR"' EXIT</code>.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kapiflags='ps aux | grep kube-apiserver | tr \" \" \"\\n\" | grep enable-admission'",
        "lfcs_aliases": "alias bashstrict='set -euo pipefail'",
        "checklist": [
            ("CKA", "Can you inspect enabled admission plugins on kube-apiserver?", "grep enable-admission-plugins /etc/kubernetes/manifests/kube-apiserver.yaml"),
            ("LFCS", "Can you write a bash script with proper exit traps and error handling?", "trap on EXIT and ERR"),
            ("LFCS", "Can you evaluate regex patterns within bash [[ ... ]] test conditions?", "[[ $var =~ ^[0-9]+$ ]]"),
        ]
    }

def get_day_6():
    # Day 6: Week 4 App Lifecycle & Automation Triathlon
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "APPLICATION LIFECYCLE PIPELINE", "Secrets, ConfigMaps, Scaling & Rollouts", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="60" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="140" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Config &amp; Secrets</text>
    <text x="140" y="135" fill="#93c5fd" font-size="8.5" text-anchor="middle" font-family="monospace">ConfigMap &amp; Secret</text>

    <rect x="260" y="90" width="180" height="60" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="350" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Deployment</text>
    <text x="350" y="135" fill="#a7f3d0" font-size="8.5" text-anchor="middle" font-family="monospace">Requests/Limits set</text>

    <rect x="470" y="90" width="180" height="60" rx="6" fill="#78350f" stroke="#fbbf24"/>
    <text x="560" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">HPA Controller</text>
    <text x="560" y="135" fill="#fef3c7" font-size="8.5" text-anchor="middle" font-family="monospace">Auto-scaling 2..10</text>

    <rect x="680" y="90" width="170" height="60" rx="6" fill="#881337" stroke="#f43f5e"/>
    <text x="765" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Rolling Rollout</text>
    <text x="765" y="135" fill="#fca5a5" font-size="8.5" text-anchor="middle" font-family="monospace">Zero-downtime updates</text>

    {code_box(50, 160, 800, 65, "End-to-End Flow:\n1. k create secret generic db-sec --from-literal=pass=secret\n2. Inject into Deployment with cpu/mem requests\n3. k autoscale deploy web --min=2 --max=6 --cpu-percent=80")}
    """, "Figure 6.1: Application Lifecycle & Configuration Architecture Pipeline")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "SYSTEM MAINTENANCE TRIATHLON WORKFLOW", "Crontab -> Automated Bash Script -> Journald Logging", "cardDark", "#0f172a", "#10b981")}
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
    """, "Figure 6.2: Automated System Maintenance & Verification Pipeline")

    cka_theory = """
    <p>
      Week 4 consolidation brings together config injection, secrets, command overrides, and metrics-based horizontal autoscaling.
    </p>
    """

    lfcs_theory = """
    <p>
      Week 4 consolidation validates practical maintenance scripting, cron scheduling, journald inspection, and package installation.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kapp='kubectl get deploy,po,cm,secret,hpa'",
        "lfcs_aliases": "alias bkp='tar -czvf backup-$(date +%Y%m%d).tar.gz'",
        "checklist": [
            ("CKA", "Can you build an end-to-end application with ConfigMap, Secret, and HPA in under 5 minutes?", "Fast YAML synthesis"),
            ("LFCS", "Can you create an automated backup script triggered by cron with journal logging?", "Cron + bash + logger"),
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
