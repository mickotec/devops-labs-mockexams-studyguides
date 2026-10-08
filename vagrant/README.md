# VirtualBox Kubernetes Cluster & LFCS Lab Environment

Based on KodeKloud's <a href="https://github.com/kodekloudhub/certified-kubernetes-administrator-course/tree/master/kubeadm-clusters/virtualbox" target="_blank" rel="noopener noreferrer">Certified Kubernetes Administrator Course (VirtualBox Kubeadm)</a>.

This Vagrant configuration provisions a multi-node Kubernetes cluster (1 control plane + 2 worker nodes) along with an Ubuntu Linux Foundation Certified System Administrator (LFCS) practice machine on Oracle VirtualBox.

---

## 🖥 Virtual Machine Topology

| VM Name | Hostname | Role | CPUs | RAM | Default NAT IP | SSH Forward Port |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `controlplane` | `controlplane` | K8s Master / Control Plane | 2 | 2048 MB | `192.168.56.11` | `2710` |
| `node01` | `node01` | K8s Worker Node 1 | 1 | 1024 MB | `192.168.56.21` | `2721` |
| `node02` | `node02` | K8s Worker Node 2 | 1 | 1024 MB | `192.168.56.22` | `2722` |
| `LFCS` | `LFCS` | LFCS System Administration | 2 | 2048 MB | `192.168.56.30` | `2730` |

---

## 🚀 Quick Start

### 1. Prerequisites
- **VirtualBox** (>= 6.1 or 7.0)
- **Vagrant** (>= 2.3)
- Sufficient host resources: >= 4 CPUs, >= 8 GB RAM

### 2. Networking Mode
By default, the `Vagrantfile` supports two networking modes (configured via `BUILD_MODE` in `Vagrantfile`):
- `BRIDGE` (default): Connects VMs directly to your LAN with routable IPs (ideal for accessing NodePort services from host browser).
- `NAT`: Uses private host-only networking (`192.168.56.0/24`) with port forwarding.

### 3. Spin Up the Environment
```bash
# Bring up all VMs (controlplane, node01, node02, LFCS)
vagrant up

# Or bring up only Kubernetes CKA cluster:
vagrant up controlplane node01 node02

# Or bring up only LFCS VM:
vagrant up LFCS
```

### 4. SSH Access
```bash
# Connect using vagrant ssh:
vagrant ssh controlplane
vagrant ssh node01
vagrant ssh node02
vagrant ssh LFCS

# Or connect using the lab CLI runner from repository root:
./lab ssh controlplane
./lab ssh node01
./lab ssh node02
./lab ssh lfcs
```

---

## ☸ Initializing the Kubernetes Cluster

Once the nodes are provisioned, complete the cluster initialization on `controlplane`:

1. SSH into the control plane:
   ```bash
   vagrant ssh controlplane
   ```

2. Initialize kubeadm:
   ```bash
   sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=$(cat /usr/local/bin/public-ip)
   ```

3. Configure `kubectl` for the vagrant / regular user:
   ```bash
   mkdir -p $HOME/.kube
   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   sudo chown $(id -u):$(id -g) $HOME/.kube/config
   ```

4. Install CNI (Project Calico):
   ```bash
   # Calico provides NetworkPolicy enforcement required for CKA objectives
   kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.2/manifests/calico.yaml
   ```

5. Join worker nodes (`node01`, `node02`) using the `kubeadm join` command printed during init.

---

## 📚 References & Docs
- [01-prerequisites.md](./docs/01-prerequisites.md)
- [02-compute-resources.md](./docs/02-compute-resources.md)
- [03-connectivity.md](./docs/03-connectivity.md)
- Upstream: <a href="https://github.com/kodekloudhub/certified-kubernetes-administrator-course" target="_blank" rel="noopener noreferrer">KodeKloud Certified Kubernetes Administrator Course</a>
