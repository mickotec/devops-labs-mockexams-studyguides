"""
CKA Curriculum Content: Week 4 (Days 1 to 6)
Day 1: Commands & Arguments (Docker vs K8s)
Day 2: ConfigMaps & App Configuration
Day 3: Secrets Management & Encryption at Rest
Day 4: Autoscaling: HPA, VPA & In-Place Resize
Day 5: Admission Controllers & Validating Webhooks
Day 6: Week 4 App Lifecycle & Secret Security Drill
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <p>
      In Kubernetes manifests, <code>command</code> overrides the image's <code>ENTRYPOINT</code>, and <code>args</code> overrides the image's <code>CMD</code>.
    </p>
    <ul>
      <li>Passing a shell command with pipe: <code>command: ["/bin/sh", "-c", "echo hello && sleep 3600"]</code></li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 1.1: Container Execution Mapping: Dockerfile vs Kubernetes PodSpec</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">CONTAINER COMMAND & ARGUMENTS: DOCKER VS KUBERNETES</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Precedence & Parameter Override Mapping</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias krun_cmd='kubectl run test --image=busybox --command -- sh -c'"""
    checklist = [('CKA', 'Can you override both ENTRYPOINT and CMD in a pod YAML?', 'command: [...] and args: [...]')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
    }

def get_day_2():
    theory = """
    <p>
      ConfigMaps decouple configuration artifacts from container image content.
    </p>
    <ul>
      <li>Create from literal: <code>kubectl create configmap app-cfg --from-literal=APP_MODE=prod</code></li>
      <li>Create from file: <code>kubectl create configmap nginx-cfg --from-file=nginx.conf</code></li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 2.1: Kubernetes ConfigMap Consumption Patterns: Env vs Volumes</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">CONFIGMAP INJECTION MECHANISMS</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Environment Variables vs Volume Projections</text>
    </g>
    
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">METHOD 1: ENV VARIABLES (envFrom / valueFrom)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">env:</text>
    <text x="75" y="155" fill="#4ade80" font-size="8.5" font-family="monospace">- name: DB_HOST</text>
    <text x="85" y="170" fill="#4ade80" font-size="8.5" font-family="monospace">  valueFrom: {configMapKeyRef: {name: app-cm, key: host}}</text>
    <text x="65" y="190" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• ⚠️ Static snapshot: CM updates do NOT update env vars in running pod!</text>
    <text x="65" y="205" fill="#94a3b8" font-size="8" font-family="sans-serif">Pod must be restarted to consume new environment values.</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">METHOD 2: VOLUME MOUNTS (Auto-Reloadable)</text>
    <text x="465" y="140" fill="#34d399" font-size="8.5" font-family="monospace">volumes:</text>
    <text x="475" y="155" fill="#34d399" font-size="8.5" font-family="monospace">- name: cfg-vol, configMap: {name: app-cm}</text>
    <text x="465" y="170" fill="#34d399" font-size="8.5" font-family="monospace">volumeMounts: [{name: cfg-vol, mountPath: /etc/config}]</text>
    <text x="465" y="190" fill="#4ade80" font-size="8.5" font-family="sans-serif">• Automatically updated by kubelet via symlink swap!</text>
    <text x="465" y="205" fill="#fde047" font-size="8.5" font-family="sans-serif">• SubPath mounts do NOT auto-update!</text>
    
</svg>"""
    aliases = """alias kcm='kubectl create configmap'"""
    checklist = [('CKA', 'Can you inject a ConfigMap into a Pod as environment variables?', 'envFrom.configMapRef'), ('CKA', 'Can you mount a ConfigMap as a volume directory?', 'volumes.configMap and volumeMounts')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
    }

def get_day_3():
    theory = """
    <p>
      Kubernetes Secrets store sensitive data (passwords, tokens, keys). By default, etcd stores secrets in plaintext unless EncryptionConfiguration is configured.
    </p>
    <ul>
      <li>Create generic secret: <code>kubectl create secret generic db-pass --from-literal=password=secret123</code></li>
      <li>Create TLS secret: <code>kubectl create secret tls cert-sec --cert=tls.crt --key=tls.key</code></li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 3.1: Kubernetes Secret Security Architecture & ETCD Encryption</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">KUBERNETES SECRETS MANAGEMENT & ENCRYPTION AT REST</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Base64 Encoding vs EncryptionConfiguration in ETCD</text>
    </g>
    
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="235" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SECRET ENCODING (base64)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">echo -n "pass123" | base64</text>
    <text x="65" y="160" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• ⚠️ Base64 is ENCODING, NOT ENCRYPTION!</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Anyone with API read access can decode:</text>
    <text x="65" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">echo "cGFzczEyMw==" | base64 -d</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">ENCRYPTION AT REST (ETCD)</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">kind: EncryptionConfiguration</text>
    <text x="465" y="155" fill="#34d399" font-size="8.5" font-family="monospace">providers: [{aescbc: {keys: [{name: key1, secret: ...}]}}]</text>
    <text x="465" y="175" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Passed to kube-apiserver:</text>
    <text x="465" y="195" fill="#fbbf24" font-size="8.5" font-family="monospace">--encryption-provider-config=/etc/k8s/enc.yaml</text>
    <text x="465" y="210" fill="#4ade80" font-size="8" font-family="sans-serif">Re-encrypt: <code>kubectl get secrets -A -o json | kubectl replace -f -</code></text>
    
</svg>"""
    aliases = """alias ksec='kubectl get secret'"""
    checklist = [('CKA', 'Can you create a Secret from literal and decode it with base64?', 'kubectl create secret generic && base64 -d'), ('CKA', 'Can you mount a secret into a pod as read-only files?', 'volumes.secret in pod spec')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
    }

def get_day_4():
    theory = """
    <p>
      The Horizontal Pod Autoscaler (HPA) adjusts the number of pod replicas automatically based on observed CPU/memory metrics.
    </p>
    <ul>
      <li>Crucial requirement: Pods <strong>must have resource requests configured</strong>, otherwise HPA cannot compute percentage utilization and remains in <code>&lt;unknown&gt;</code> state!</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 4.1: Kubernetes HPA Autoscaling Control Loop</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">HORIZONTAL POD AUTOSCALER (HPA) FEEDBACK LOOP</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Metrics Server -> HPA Controller -> Deployment Scale</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias khpa='kubectl get hpa'"""
    checklist = [('CKA', 'Can you configure an HPA to scale a deployment from 2 to 8 replicas at 75% CPU?', 'kubectl autoscale deploy <name> --min=2 --max=8 --cpu-percent=75'), ('CKA', 'Do you understand why HPA shows <unknown> when requests are missing?', 'HPA computes percentage against spec.containers.resources.requests')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
    }

def get_day_5():
    theory = """
    <p>
      Admission Controllers intercept requests to the Kubernetes API server prior to persistence in etcd, but after authentication and authorization.
    </p>
    <ul>
      <li>Enable admission plugin: In <code>/etc/kubernetes/manifests/kube-apiserver.yaml</code>, modify <code>--enable-admission-plugins=NodeRestriction,LimitRanger,...</code></li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 5.1: Kubernetes Admission Controller Mutating & Validating Webhook Pipeline</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">KUBERNETES ADMISSION CONTROLLER PIPELINE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Mutating Webhook -> Schema Validation -> Validating Webhook</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias kapiflags='ps aux | grep kube-apiserver | tr " " "\n" | grep enable-admission'"""
    checklist = [('CKA', 'Can you inspect enabled admission plugins on kube-apiserver?', 'grep enable-admission-plugins /etc/kubernetes/manifests/kube-apiserver.yaml')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
    }

def get_day_6():
    theory = """
    <p>
      Week 4 consolidation brings together config injection, secrets, command overrides, and metrics-based horizontal autoscaling.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 6.1: Application Lifecycle & Configuration Architecture Pipeline</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">APPLICATION LIFECYCLE PIPELINE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Secrets, ConfigMaps, Scaling & Rollouts</text>
    </g>
    
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

    
    <rect x="50" y="160" width="800" height="65" rx="5" fill="#030712" stroke="#334155" stroke-width="1"/>
    <text x="60" y="176" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">End-to-End Flow:</text><text x="60" y="190" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">1. k create secret generic db-sec --from-literal=pass=secret</text><text x="60" y="204" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">2. Inject into Deployment with cpu/mem requests</text><text x="60" y="218" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">3. k autoscale deploy web --min=2 --max=6 --cpu-percent=80</text>
    
    
</svg>"""
    aliases = """alias kapp='kubectl get deploy,po,cm,secret,hpa'"""
    checklist = [('CKA', 'Can you build an end-to-end application with ConfigMap, Secret, and HPA in under 5 minutes?', 'Fast YAML synthesis')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
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
