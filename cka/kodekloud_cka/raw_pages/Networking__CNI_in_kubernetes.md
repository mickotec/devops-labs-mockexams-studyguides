> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CNI in kubernetes

> This lesson explores how Kubernetes uses the Container Network Interface to manage container networking and configure network plugins.

In this lesson, we explore how Kubernetes leverages the Container Network Interface (CNI) to manage container networking. You will gain an understanding of how network plugins are configured and used in a Kubernetes environment.

Earlier, we reviewed:

* The basics of networking and namespaces
* Docker networking fundamentals
* The evolution and rationale behind CNI
* A list of supported CNI plugins

<Frame>
  ![The image lists prerequisites for a topic, including network namespaces in Linux, Docker networking, Container Network Interface (CNI), and CNI plugins.](https://kodekloud.com/kk-media/image/upload/v1752869838/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-CNI-in-kubernetes/frame_10.jpg)
</Frame>

Now, we focus on how Kubernetes configures the use of these network plugins.

As discussed in previous lessons, the CNI specifies the responsibilities of the container runtime. In Kubernetes, container runtimes such as Containerd or CRI-O create the container network namespaces and attach them to the correct network by invoking the appropriate network plugin. Although Docker was initially the primary container runtime, it has largely been replaced by Containerd as an abstraction layer.

<Frame>
  ![The image explains the Container Network Interface, highlighting the need for creating a network namespace and identifying the network for container attachment, with a Kubernetes logo.](https://kodekloud.com/kk-media/image/upload/v1752869838/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-CNI-in-kubernetes/frame_40.jpg)
</Frame>

## Configuring CNI Plugins in Kubernetes

When a container is created, the container runtime invokes the necessary CNI plugin to attach the container to the network. Two common runtimes that demonstrate how this process works are Containerd and CRI-O.

<Callout icon="lightbulb" color="#1CB2FE">
  Container runtimes look for CNI plugin executables in the `/opt/cni/bin` directory, while network configuration files are read from the `/etc/cni/net.d` directory.
</Callout>

### Directory Structure for CNI Plugins and Configuration

The network plugins reside in `/opt/cni/bin`, and the configuration files that dictate which plugin to use are stored in `/etc/cni/net.d`. Typically, the container runtime selects the configuration file that appears first in alphabetical order.

For example, you might see the following directories:

```bash theme={null}
ls /opt/cni/bin
```

```bash theme={null}
bridge  dhcp  flannel  host-local  ipvlan  loopback  macvlan  portmap  ptp  sample  tuning  vlan  weave-ipam  weave-net  weave-plugin-2.2.1
```

```bash theme={null}
ls /etc/cni/net.d
```

```bash theme={null}
10-bridge.conflist
```

In this case, the container runtime chooses the "bridge" configuration file.

<Frame>
  ![The image illustrates configuring CNI with container runtimes containerd and cri-o, showing directories for plugins and configuration files like flannel and bridge.](https://kodekloud.com/kk-media/image/upload/v1752869839/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-CNI-in-kubernetes/frame_100.jpg)
</Frame>

### Understanding a CNI Bridge Configuration File

A typical CNI bridge configuration file, adhering to the CNI standard, might look like this:

```bash theme={null}
cat /etc/cni/net.d/10-bridge.conf
```

```json theme={null}
{
  "cniVersion": "0.2.0",
  "name": "mynet",
  "type": "bridge",
  "bridge": "cni0",
  "isGateway": true,
  "ipMasq": true,
  "ipam": {
    "type": "host-local",
    "subnet": "10.22.0.0/16",
    "routes": [
      { "dst": "0.0.0.0/0" }
    ]
  }
}
```

In this configuration:

* The `"name"` field (e.g., `"mynet"`) represents the network name.
* The `"type"` field set to `"bridge"` indicates the use of a bridge plugin.
* The `"bridge"` field (e.g., `"cni0"`) specifies the network bridge's name.
* The `"isGateway"` flag designates whether the bridge interface should have an IP address to function as a gateway.
* The `"ipMasq"` option enables network address translation (NAT) through IP masquerading.
* The `"ipam"` (IP Address Management) section uses `"host-local"` to allocate IP addresses from the specified subnet (`"10.22.0.0/16"`) and defines a default route.

<Callout icon="lightbulb" color="#1CB2FE">
  Understanding these configuration fields is crucial for troubleshooting and optimizing Kubernetes networking. The settings in this bridge configuration align with fundamental networking concepts such as bridging, routing, and NAT masquerading.
</Callout>

This concludes our lesson on configuring CNI plugins with Kubernetes. We encourage you to apply these concepts through practical exercises to strengthen your Kubernetes networking skills.

For more information on related topics, consider reviewing:

* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Docker Hub](https://hub.docker.com/)

Happy networking!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/44bc9a9f-319c-40ee-babd-0f7b53a70de7/lesson/3ac358fa-3aab-4876-8f27-f2d7c3474164" />
</CardGroup>
