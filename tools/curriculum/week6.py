"""
Curriculum Content: Week 6 (Days 1 to 6)
Day 1: Certificates API & KubeConfig Management | Storage Partitions (MBR vs GPT) & Swap
Day 2: RBAC (Roles, RoleBindings & ClusterRoles) | Filesystems & Boot Mounting (/etc/fstab)
Day 3: ServiceAccounts & SecurityContexts | Logical Volume Management (LVM) Architecture
Day 4: Storage: Volumes, PV, PVC & StorageClasses | Dynamic LVM Volume Expansion
Day 5: Helm & Kustomize (2025 Updates) | Remote Filesystems: NFS & Storage Monitoring
Day 6: Security & Storage Lab Triathlon | Week 6 Storage Mastery & LVM Drill
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    # Day 1: Certificates API & Partitions/Swap
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "CERTIFICATES API & KUBECONFIG CONTEXT ARCHITECTURE", "CertificateSigningRequest (CSR) Flow & Multi-Cluster Contexts", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">CSR LIFECYCLE</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">1. openssl genrsa -out user.key 2048</text>
    <text x="65" y="155" fill="#4ade80" font-size="8.5" font-family="monospace">2. openssl req -new -key user.key -subj "/CN=user/O=devs"</text>
    <text x="65" y="170" fill="#fde047" font-size="8.5" font-family="monospace">3. kubectl apply -f csr.yaml (base64 request)</text>
    <text x="65" y="188" fill="#38bdf8" font-size="8.5" font-family="monospace">4. kubectl certificate approve user-csr</text>
    <text x="65" y="205" fill="#34d399" font-size="8.5" font-family="monospace">5. kubectl get csr user-csr -o jsonpath='{{.status.certificate}}' | base64 -d</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">KUBECONFIG CONTEXT SWITCHING</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">kubectl config set-credentials user --client-cert=... --client-key=...</text>
    <text x="465" y="160" fill="#fde047" font-size="8.5" font-family="monospace">kubectl config set-context dev-ctx --cluster=k8s --user=user</text>
    <text x="465" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">kubectl config use-context dev-ctx</text>
    <text x="465" y="205" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Triad: <strong>Clusters</strong> + <strong>Users</strong> = <strong>Contexts</strong></text>
    """, "Figure 1.1: Kubernetes CSR Signing Pipeline & Kubeconfig Context Switcher")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "STORAGE PARTITIONING: MBR VS GPT & SWAP MANAGEMENT", "Partition Tables, Fdisk, Parted & Swap Activation", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">MBR (DOS) VS GPT</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <strong>MBR:</strong> Max 2TB disk size, max 4 primary partitions.</text>
    <text x="65" y="160" fill="#34d399" font-size="8.5" font-family="sans-serif">• <strong>GPT:</strong> Up to 9.4 ZB, 128 primary partitions, CRC32 checks.</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">fdisk /dev/sdb   # Standard MBR / GPT tool</text>
    <text x="65" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">parted /dev/sdb mklabel gpt</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SWAP CREATION &amp; ACTIVATION</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">mkswap /dev/sdb2         # Format partition as swap</text>
    <text x="465" y="160" fill="#fde047" font-size="8.5" font-family="monospace">swapon /dev/sdb2         # Activate immediately</text>
    <text x="465" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">swapon --show / free -h  # Verify swap capacity</text>
    <text x="465" y="205" fill="#fca5a5" font-size="8.5" font-family="monospace">/etc/fstab: /dev/sdb2 none swap sw 0 0</text>
    """, "Figure 1.2: Linux Storage Partitioning Architecture & Swap Space")

    cka_theory = """
    <p>
      Users in Kubernetes are external identities managed via x509 certificates. The <code>CertificateSigningRequest</code> (CSR) resource allows submitting and approving certificates via the Kubernetes API.
    </p>
    <ul>
      <li>Approve CSR: <code>kubectl certificate approve &lt;csr-name&gt;</code></li>
      <li>Deny CSR: <code>kubectl certificate deny &lt;csr-name&gt;</code></li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Storage management begins with partition table creation.
    </p>
    <ul>
      <li>Use <code>fdisk</code> or <code>parted</code> to manage partition tables.</li>
      <li>To initialize swap: <code>mkswap &lt;partition&gt;</code> followed by <code>swapon &lt;partition&gt;</code>.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kctx='kubectl config current-context'",
        "lfcs_aliases": "alias lsblk='lsblk -f'",
        "checklist": [
            ("CKA", "Can you submit a CSR, approve it, and configure KubeConfig for a new user?", "kubectl certificate approve && kubectl config set-credentials"),
            ("LFCS", "Can you create a partition with fdisk/parted and configure it as swap?", "mkswap && swapon"),
        ]
    }

def get_day_2():
    # Day 2: RBAC & /etc/fstab
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES RBAC ARCHITECTURE", "Role vs ClusterRole & RoleBinding vs ClusterRoleBinding", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SUBJECTS</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Users (x509 CN)</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Groups (x509 O)</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="sans-serif">• ServiceAccounts</text>
    <text x="65" y="205" fill="#fde047" font-size="8.5" font-family="monospace">kubectl auth can-i create pod</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="440" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">BINDING LAYER</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">RoleBinding (Namespace)</text>
    <text x="325" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Binds Subject to Role in one NS</text>
    <text x="325" y="180" fill="#fbbf24" font-size="8.5" font-family="monospace">ClusterRoleBinding (Cluster)</text>
    <text x="325" y="200" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Binds Subject cluster-wide</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">ROLES (Rules)</text>
    <text x="605" y="140" fill="#34d399" font-size="8.5" font-family="monospace">apiGroups: ["", "apps"]</text>
    <text x="605" y="160" fill="#34d399" font-size="8.5" font-family="monospace">resources: ["pods", "deployments"]</text>
    <text x="605" y="180" fill="#34d399" font-size="8.5" font-family="monospace">verbs: ["get", "list", "watch"]</text>
    <text x="605" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">ClusterRole: nodes, PVs, or all NS</text>
    """, "Figure 2.1: Kubernetes Role-Based Access Control (RBAC) Mechanics")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX FILESYSTEM MOUNTING & /ETC/FSTAB FIELDS", "Persistent Mount Configuration & Recovery Options", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="800" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="450" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">/etc/fstab SIX COLUMN STRUCTURE</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">UUID=4f92... /data        ext4    defaults,noatime    0       2</text>
    <text x="65" y="155" fill="#fde047" font-size="8.8" font-family="monospace">  Column 1     Column 2     Col 3   Column 4            Col 5   Col 6</text>
    <text x="65" y="172" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">1: Device / UUID (blkid) | 2: Mount Point | 3: Filesystem Type (ext4, xfs)</text>
    <text x="65" y="188" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">4: Mount Options (rw, nosuid, nodev, noexec, defaults) | 5: Dump (0=skip)</text>
    <text x="65" y="206" fill="#34d399" font-size="8.5" font-family="monospace">6: Fsck Order (1=root /, 2=other disks, 0=skip) | Test: mount -a (NEVER REBOOT BEFORE mount -a!)</text>
    """, "Figure 2.2: Linux /etc/fstab Column Specification & Mount Verification")

    cka_theory = """
    <p>
      RBAC regulates access to Kubernetes resources based on roles assigned to users or ServiceAccounts.
    </p>
    <ul>
      <li>Check permissions: <code>kubectl auth can-i create deployments --as=developer -n dev</code></li>
      <li>ClusterRole is required for cluster-scoped resources like Nodes, PersistentVolumes, and Namespaces.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Persistent filesystem mounting requires valid entries in <code>/etc/fstab</code>.
    </p>
    <ul>
      <li>Always use <code>UUID=</code> from <code>blkid</code> rather than device paths (<code>/dev/sdb1</code>) because drive letters can swap on reboot.</li>
      <li><strong>Golden Rule:</strong> Always test changes with <code>mount -a</code> before rebooting! A syntax error in <code>/etc/fstab</code> triggers Emergency Mode boot!</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kcani='kubectl auth can-i'",
        "lfcs_aliases": "alias mntest='sudo mount -a'",
        "checklist": [
            ("CKA", "Can you create a Role and RoleBinding with kubectl create imperatively?", "kubectl create role <r> --verb=get,list --resource=pods"),
            ("CKA", "Can you verify permissions using kubectl auth can-i?", "kubectl auth can-i <verb> <res> --as=<user>"),
            ("LFCS", "Can you mount a filesystem by UUID permanently in /etc/fstab?", "blkid && entry in /etc/fstab && mount -a"),
        ]
    }

def get_day_3():
    # Day 3: ServiceAccounts & LVM Architecture
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "SERVICEACCOUNT TOKENS & SECURITYCONTEXT ENFORCEMENT", "Workload Identity & Host Isolation Parameters", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SERVICEACCOUNT &amp; PROJECTED TOKEN</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">spec.serviceAccountName: backend-sa</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• K8s 1.24+: Bound token projected into Pod at:</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">/var/run/secrets/kubernetes.io/serviceaccount</text>
    <text x="65" y="200" fill="#a7f3d0" font-size="8" font-family="monospace">automountServiceAccountToken: false (Disables token)</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="650" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SECURITYCONTEXT CONSTRAINTS</text>
    <text x="465" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">securityContext:</text>
    <text x="475" y="155" fill="#fca5a5" font-size="8.5" font-family="monospace">  runAsUser: 10001        # Non-root user ID</text>
    <text x="475" y="170" fill="#fca5a5" font-size="8.5" font-family="monospace">  runAsNonRoot: true      # Fails if image is root</text>
    <text x="475" y="185" fill="#fca5a5" font-size="8.5" font-family="monospace">  readOnlyRootFilesystem: true</text>
    <text x="475" y="200" fill="#fde047" font-size="8.5" font-family="monospace">  capabilities: {{drop: ["ALL"], add: ["NET_BIND_SERVICE"]}}</text>
    """, "Figure 3.1: Kubernetes ServiceAccount Tokens & SecurityContext Hardening")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LOGICAL VOLUME MANAGEMENT (LVM) ARCHITECTURE", "Physical Volumes (PV) -> Volume Groups (VG) -> Logical Volumes (LV)", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. PHYSICAL VOLUMES (PV)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">pvcreate /dev/sdb1 /dev/sdc1</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">pvs / pvdisplay</text>
    <text x="65" y="185" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Initializes raw disks or partitions</text>
    <text x="65" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Allocates Physical Extents (PE: 4MB)</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="440" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. VOLUME GROUPS (VG)</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">vgcreate data_vg /dev/sdb1</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">vgs / vgdisplay</text>
    <text x="325" y="185" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Pools storage capacity together</text>
    <text x="325" y="205" fill="#34d399" font-size="8.5" font-family="monospace">vgextend data_vg /dev/sdc1</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. LOGICAL VOLUMES (LV)</text>
    <text x="605" y="140" fill="#34d399" font-size="8.5" font-family="monospace">lvcreate -n web_lv -L 10G data_vg</text>
    <text x="605" y="160" fill="#34d399" font-size="8.5" font-family="monospace">lvs / lvdisplay</text>
    <text x="605" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">mkfs.ext4 /dev/data_vg/web_lv</text>
    <text x="605" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Formatted and mounted like a normal disk</text>
    """, "Figure 3.2: LVM Three-Tier Architecture: PV -> VG -> LV")

    cka_theory = """
    <p>
      ServiceAccounts provide machine identity for Pod processes to authenticate against the Kubernetes API.
    </p>
    <ul>
      <li>SecurityContext: Can be set at Pod-level or Container-level. Container-level overrides Pod-level.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Logical Volume Management (LVM) abstracts physical storage into flexible, dynamically resizable virtual partitions.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias ksa='kubectl get sa'",
        "lfcs_aliases": "alias lvms='pvs && vgs && lvs'",
        "checklist": [
            ("CKA", "Can you configure runAsUser and add capabilities in a Pod securityContext?", "securityContext.capabilities.add"),
            ("LFCS", "Can you create an LVM Logical Volume from physical partitions?", "pvcreate -> vgcreate -> lvcreate"),
        ]
    }

def get_day_4():
    # Day 4: PV/PVC & Dynamic LVM Resize
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES STORAGE BINDING PIPELINE", "Pod -> PVC (Claim) -> PV (Storage Volume) -> StorageClass", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">PERSISTENTVOLUME (PV)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Cluster-wide storage resource</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">capacity: {{storage: 10Gi}}</text>
    <text x="65" y="178" fill="#4ade80" font-size="8.5" font-family="monospace">accessModes: [ReadWriteOnce]</text>
    <text x="65" y="196" fill="#fde047" font-size="8.5" font-family="monospace">persistentVolumeReclaimPolicy: Retain</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="440" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">PVC (User Claim)</text>
    <text x="325" y="140" fill="#34d399" font-size="8.5" font-family="monospace">kind: PersistentVolumeClaim</text>
    <text x="325" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Requests capacity &amp; accessMode</text>
    <text x="325" y="180" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Automatically binds to matching PV</text>
    <text x="325" y="205" fill="#4ade80" font-size="8.5" font-family="monospace">Status: Bound</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="720" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">POD CONSUMPTION</text>
    <text x="605" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">volumes:</text>
    <text x="615" y="155" fill="#e2e8f0" font-size="8.5" font-family="monospace">- name: data-vol</text>
    <text x="625" y="170" fill="#fde047" font-size="8.5" font-family="monospace">  persistentVolumeClaim:</text>
    <text x="635" y="185" fill="#fde047" font-size="8.5" font-family="monospace">    claimName: my-pvc</text>
    <text x="605" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">volumeMounts: mountPath: /var/data</text>
    """, "Figure 4.1: Kubernetes Persistent Volume Binding Architecture")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "DYNAMIC LVM VOLUME EXPANSION & FILESYSTEM RESIZING", "Online Filesystem Extension: ext4 vs XFS", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">STEP 1: EXPAND LOGICAL VOLUME</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">lvextend -L +5G /dev/data_vg/web_lv</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">lvextend -l +100%FREE /dev/data_vg/web_lv</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Expands block device in-place without unmounting!</text>
    <text x="65" y="200" fill="#fde047" font-size="8.5" font-family="monospace">lvextend -r ...  # -r resizes filesystem automatically!</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">STEP 2: RESIZE FILESYSTEM (ext4 vs XFS)</text>
    <text x="465" y="140" fill="#38bdf8" font-size="8.5" font-family="monospace">resize2fs /dev/data_vg/web_lv   # ext4 online expand</text>
    <text x="465" y="160" fill="#fbbf24" font-size="8.5" font-family="monospace">xfs_growfs /mountpoint          # XFS (uses mountpoint!)</text>
    <text x="465" y="185" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• ⚠️ XFS cannot be shrunk (only grown)!</text>
    <text x="465" y="205" fill="#a7f3d0" font-size="8.5" font-family="monospace">df -h /mountpoint  # Verify new capacity</text>
    """, "Figure 4.2: Dynamic LVM Online Expansion & Filesystem Resize Pipeline")

    cka_theory = """
    <p>
      PVs decouple physical storage implementation from Pod specs.
    </p>
    <ul>
      <li>Access Modes: <code>ReadWriteOnce</code> (RWO - single node), <code>ReadOnlyMany</code> (ROX), <code>ReadWriteMany</code> (RWX - NFS).</li>
      <li>Reclaim Policies: <code>Retain</code> (keeps data after PVC delete), <code>Delete</code> (wipes volume).</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Online volume expansion allows growing storage without taking production services offline.
    </p>
    <ul>
      <li>For <strong>ext4</strong>: Run <code>resize2fs /dev/vg/lv</code>.</li>
      <li>For <strong>xfs</strong>: Run <code>xfs_growfs /mount/path</code> (takes the mount path, not the device!).</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kpv='kubectl get pv,pvc'",
        "lfcs_aliases": "alias lve='sudo lvextend -r -l +100%FREE'",
        "checklist": [
            ("CKA", "Can you create a PV and PVC and bind them successfully?", "PV capacity and accessModes match PVC"),
            ("LFCS", "Can you expand an LVM volume and resize an ext4 or XFS filesystem online?", "lvextend followed by resize2fs or xfs_growfs"),
        ]
    }

def get_day_5():
    # Day 5: Helm & NFS
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "HELM PACKAGE MANAGER & KUSTOMIZE OVERLAY ARCHITECTURE", "Templating vs Declarative Parameterized Kustomization", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">HELM PACKAGE MANAGER</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">helm repo add bitnami https://...</text>
    <text x="65" y="158" fill="#4ade80" font-size="8.5" font-family="monospace">helm install my-app bitnami/nginx -f values.yaml</text>
    <text x="65" y="176" fill="#4ade80" font-size="8.5" font-family="monospace">helm upgrade my-app bitnami/nginx --set replicas=3</text>
    <text x="65" y="194" fill="#fca5a5" font-size="8.5" font-family="monospace">helm rollback my-app 1</text>
    <text x="65" y="210" fill="#38bdf8" font-size="8.5" font-family="monospace">helm list -A</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">KUSTOMIZE OVERLAYS (kubectl -k)</text>
    <text x="465" y="140" fill="#34d399" font-size="8.5" font-family="monospace">base/ (kustomization.yaml, deployment.yaml)</text>
    <text x="465" y="160" fill="#fde047" font-size="8.5" font-family="monospace">overlays/prod/ (patches, replicas=5)</text>
    <text x="465" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">kubectl apply -k overlays/prod/</text>
    <text x="465" y="205" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Template-free customization built into kubectl!</text>
    """, "Figure 5.1: Helm Packaging Lifecycle & Kustomize Overlay Hierarchy")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "NETWORK FILE SYSTEM (NFS) ARCHITECTURE & EXPORTS", "NFS Server RPC Daemon Configuration & Client Mounting", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">NFS SERVER (/etc/exports)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">/srv/nfs 192.168.1.0/24(rw,sync,no_root_squash)</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <code>rw</code>: Read-write access | <code>sync</code>: Flush writes</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">sudo exportfs -rav  # Reload exports</text>
    <text x="65" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">sudo systemctl restart nfs-server</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">NFS CLIENT MOUNTING</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">showmount -e 192.168.1.100  # Query remote exports</text>
    <text x="465" y="160" fill="#fde047" font-size="8.5" font-family="monospace">mount -t nfs 192.168.1.100:/srv/nfs /mnt/nfs</text>
    <text x="465" y="185" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">/etc/fstab entry:</text>
    <text x="465" y="205" fill="#34d399" font-size="8.5" font-family="monospace">192.168.1.100:/srv/nfs /mnt/nfs nfs defaults 0 0</text>
    """, "Figure 5.2: NFS Remote Filesystem Server Export & Client Mount Architecture")

    cka_theory = """
    <p>
      Helm manages packaged Kubernetes applications. Kustomize provides declarative customization without templates via <code>kustomization.yaml</code>.
    </p>
    """

    lfcs_theory = """
    <p>
      NFS provides shared network storage across multiple Linux servers.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias hls='helm list'",
        "lfcs_aliases": "alias expreload='sudo exportfs -rav'",
        "checklist": [
            ("CKA", "Can you install and upgrade a release with Helm and values override?", "helm install -f values.yaml"),
            ("LFCS", "Can you export an NFS share and mount it on a client with /etc/fstab?", "exportfs -rav && mount -t nfs"),
        ]
    }

def get_day_6():
    # Day 6: Security & Storage Triathlon
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "SECURITY & STORAGE TRIATHLON TOPOLOGY", "Restricted ServiceAccount + Bound PVC on Encrypted Volume", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="60" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="140" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">RBAC Security</text>
    <text x="140" y="135" fill="#93c5fd" font-size="8.5" text-anchor="middle" font-family="monospace">Role &amp; SA Binding</text>

    <rect x="260" y="90" width="180" height="60" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="350" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Storage Binding</text>
    <text x="350" y="135" fill="#a7f3d0" font-size="8.5" text-anchor="middle" font-family="monospace">PVC bound to PV</text>

    <rect x="470" y="90" width="180" height="60" rx="6" fill="#78350f" stroke="#fbbf24"/>
    <text x="560" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SecurityContext</text>
    <text x="560" y="135" fill="#fef3c7" font-size="8.5" text-anchor="middle" font-family="monospace">runAsNonRoot: true</text>

    <rect x="680" y="90" width="170" height="60" rx="6" fill="#881337" stroke="#f43f5e"/>
    <text x="765" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Production Pod</text>
    <text x="765" y="135" fill="#fca5a5" font-size="8.5" text-anchor="middle" font-family="monospace">Running securely</text>

    {code_box(50, 160, 800, 65, "Combined Workflow:\n1. Create Role & RoleBinding for ServiceAccount 'app-sa'\n2. Create 5Gi PV and PVC 'app-pvc'\n3. Launch Pod using 'app-sa' and mounting 'app-pvc' with securityContext runAsUser=1000")}
    """, "Figure 6.1: Security & Storage Triathlon Topology")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "STORAGE DISASTER RECOVERY & LVM DRILL", "Corrupted Mount Repair, Fsck & Volume Snapshot Restore", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="170" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. CORRUPTED MOUNT</text>
    <text x="65" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">fsck -y /dev/data_vg/web_lv</text>
    <text x="65" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Always unmount before running fsck!</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">umount /mnt/corrupted</text>
    <text x="65" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">e2fsck -f /dev/data_vg/web_lv</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. LVM SNAPSHOTS</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">lvcreate -s -n web_snap -L 2G \</text>
    <text x="325" y="155" fill="#fde047" font-size="8.5" font-family="monospace">  /dev/data_vg/web_lv</text>
    <text x="325" y="175" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Point-in-time copy-on-write snapshot</text>
    <text x="325" y="195" fill="#34d399" font-size="8.5" font-family="monospace">lvconvert --merge /dev/.../web_snap</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. RE-MOUNT &amp; AUDIT</text>
    <text x="595" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">mount -a</text>
    <text x="595" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">df -hT</text>
    <text x="595" y="180" fill="#38bdf8" font-size="8.5" font-family="monospace">ls -la /mountpoint</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Filesystem verified and restored</text>
    """, "Figure 6.2: Linux Storage Disaster Recovery & LVM Snapshot Rollback")

    cka_theory = """
    <p>
      Week 6 consolidation combines RBAC, ServiceAccounts, SecurityContexts, and Persistent Volumes into a unified secure application topology.
    </p>
    """

    lfcs_theory = """
    <p>
      Week 6 consolidation tests storage administration: MBR/GPT partitioning, swap activation, ext4/XFS filesystems, LVM expansion, and NFS exports.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kstorage='kubectl get pv,pvc,sc'",
        "lfcs_aliases": "alias fscheck='sudo fsck -N'",
        "checklist": [
            ("CKA", "Can you configure RBAC, PVC, and securityContext together in 5 minutes?", "Unified manifest deployment"),
            ("LFCS", "Can you create and merge an LVM snapshot after an administrative test?", "lvcreate -s and lvconvert --merge"),
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
