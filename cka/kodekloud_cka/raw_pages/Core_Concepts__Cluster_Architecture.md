> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cluster Architecture

> This article provides an overview of Kubernetes cluster architecture, detailing the roles and components of master and worker nodes in managing containerized applications.

Hello and welcome to our comprehensive guide on Kubernetes cluster architecture. In this article, we provide a high-level overview of how Kubernetes organizes and manages containerized applications. You will learn about each component’s roles, responsibilities, and configurations, as well as practical insights into examining an existing cluster.

Kubernetes simplifies the deployment, scaling, and management of containerized applications through automation. To help explain this concept, imagine two kinds of ships: cargo ships (worker nodes) that carry containers, and control ships (master nodes) that monitor and manage the cargo ships. In Kubernetes, the cluster consists of nodes—whether physical or virtual, on-premises or cloud-hosted—that host your containerized applications.

## Master Node Components

The master node contains several control plane components that manage the entire Kubernetes cluster. It keeps track of all nodes, decides where applications should run, and continuously monitors the cluster. Think of the master node as the central command center coordinating the fleet.

<Frame>
  ![The image illustrates a Kubernetes concept with a person explaining, featuring a ship labeled "Master" and smaller ships labeled "Worker Nodes" amidst clouds.](https://kodekloud.com/kk-media/image/upload/v1752869701/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Cluster-Architecture/frame_140.jpg)
</Frame>

In a busy harbor, many containers are loaded and unloaded daily. Kubernetes maintains detailed information about each container and its corresponding node in a highly available key-value store called etcd. Etcd uses a simple key-value format along with a quorum mechanism, ensuring reliable and consistent data storage across the cluster.

When a new container (or "ship cargo") is ready, the Kubernetes scheduler—similar to port cranes—determines which worker node (or "ship") should host it. The scheduler takes into account current load, resource requirements, and specific constraints like taints, tolerations, or node affinity rules. This scheduling process is vital for efficient cluster operation.

<Callout icon="lightbulb" color="#1CB2FE">
  The Kubernetes replication controller and other controllers work like dock office staff, ensuring that the desired number of containers are running and managing node operations.
</Callout>

Other key master node components include:

* **ETCD Cluster:** Stores cluster-wide configuration and state data.
* **Kube Scheduler:** Determines the best node for new container deployments.
* **Controllers:** Manage node lifecycle, container replication, and system stability.
* **Kube API Server:** Acts as the central hub for cluster communication and management.

<Frame>
  ![The image illustrates Kubernetes architecture, showing master and worker nodes, with components like ETCD cluster, controllers, and kube-scheduler, alongside a person explaining.](https://kodekloud.com/kk-media/image/upload/v1752869703/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Cluster-Architecture/frame_270.jpg)
</Frame>

## Worker Node Components

Worker nodes, which can be compared to cargo ships, are responsible for running the containerized applications. Each node is managed by the Kubelet, the node’s “captain,” which ensures that containers are running as instructed.

* **Kubelet:** Manages container lifecycle on an individual node. It receives instructions from the Kube API server to create, update, or delete containers, and regularly reports the node's status.
* **Kube Proxy:** Configures networking rules on worker nodes, thus enabling smooth inter-container communication across nodes. For instance, it allows a web server on one node to interact with a database on another.

<Callout icon="lightbulb" color="#1CB2FE">
  The entire control system is containerized. Whether you are using Docker, Containerd, or CRI-O, every node (including master nodes with containerized components) requires a compatible container runtime engine.
</Callout>

The high-level worker node architecture ensures that applications remain available and responsive, even as they communicate across a distributed network.

<Frame>
  ![The image illustrates Kubernetes architecture, showing components like Master and Worker Nodes, with a person explaining the diagram.](https://kodekloud.com/kk-media/image/upload/v1752869704/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Cluster-Architecture/frame_510.jpg)
</Frame>

## Summary of Kubernetes Architecture

The Kubernetes cluster architecture is divided into two main segments:

| Component Category | Key Components                                     | Description                                                                                                 |
| ------------------ | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Master Node**    | etcd, Kube Scheduler, Controllers, Kube API Server | Centralized control and management of the entire cluster.                                                   |
| **Worker Node**    | Kubelet, Kube Proxy                                | Responsible for the lifecycle management of containers and ensuring network communication between services. |

This clear separation and coordination between master and worker nodes is fundamental to Kubernetes' ability to automate and streamline container orchestration.

We hope this detailed overview of Kubernetes cluster architecture has provided valuable insights. In upcoming articles, we will explore each component in depth, offering practical examples and exercises to further enhance your understanding of Kubernetes systems.

Happy learning and stay tuned for more Kubernetes content!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/c6d2ac7d-8192-4cff-aa54-e36d888c5bd9/lesson/e32de035-0ed3-4e4c-a260-0218b7a2e971" />
</CardGroup>
