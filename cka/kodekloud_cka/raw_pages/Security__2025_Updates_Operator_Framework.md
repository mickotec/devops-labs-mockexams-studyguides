> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 2025 Updates Operator Framework

> This article explores the operator framework, highlighting its role in simplifying Kubernetes resource deployment and management.

In this article, we dive into the operator framework and explore how it simplifies the deployment and management of Kubernetes resources. Previously, we discussed creating a Custom Resource Definition (CRD) and a custom controller to handle resource-specific logic. Traditionally, these components are deployed separately: you first create the CRD and its related resources, and then deploy the controller as a pod or as part of a deployment. With the operator framework, you can package both components into a single deployable entity.

When you deploy the flight operator, it automatically creates the Custom Resource Definition, provisions the required resources, and deploys the custom controller as a Deployment. Consider the following example:

```yaml theme={null}
# flightticket-custom-definition.yml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: flighttickets.flights.com
spec:
  scope: Namespaced
  group: flights.com
  names:
    kind: FlightTicket
    singular: flightticket
    plural: flighttickets
    shortnames:
      - ft
  versions:
    - name: v1
      served: true
      storage: true
```

Below is an example of the custom controller written in Go. This controller monitors and synchronizes the state of FlightTicket resources within your Kubernetes cluster:

```go theme={null}
package flightticket

import "k8s.io/api/apps/v1"

var controllerKind = v1.SchemeGroupVersion.WithKind("Flightticket")

// Run begins watching and syncing.
func (dc *FlightTicketController) Run(workers int, stopCh <-chan struct{}) {}

// callBookFlightAPI invokes the Book Flight API for a ReplicaSet.
func (dc *FlightTicketController) callBookFlightAPI(obj interface{}) {}
```

To deploy the operator, simply run:

```bash theme={null}
# Deploy the operator
kubectl create -f flight-operator.yaml
```

<Callout icon="lightbulb" color="#1CB2FE">
  The operator framework not only streamlines resource deployment but also simplifies ongoing management tasks such as application updates, backups, and recovery.
</Callout>

One of the most popular examples is the etcd operator. It deploys and manages an etcd cluster within Kubernetes using a dedicated CRD and a custom controller that observes changes in the etcd cluster resource. Additionally, it supports extended functionalities such as taking backups and executing restores, simply by creating supplementary CRDs. Backup and Restore operators enhance these capabilities further.

<Frame>
  ![The image illustrates an Operator Framework with Custom Resource Definitions (CRD) and Custom Controllers, including EtcdCluster, EtcdBackup, EtcdRestore, ETCD Controller, and Backup Operator.](https://kodekloud.com/kk-media/image/upload/v1752869918/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-2025-Updates-Operator-Framework/frame_80.jpg)
</Frame>

Kubernetes operators handle tasks that would typically require manual intervention by system administrators. These tasks include application installation, routine maintenance, backup operations, disaster recovery through data restoration, and troubleshooting.

For a comprehensive list of available operators, visit the [Operator Hub](https://operatorhub.io/). Many popular applications—such as etcd, MySQL, Prometheus, Grafana, Argo CD, and Istio—have dedicated operators with detailed installation instructions accessible via an install button.

## How to Deploy an Application Using an Operator

Deploying an application with an operator is an easy process that typically involves:

1. Installing the Operator Lifecycle Manager.
2. Deploying the operator.
3. Enjoying streamlined application management.

The following commands show you how to install the Operator Lifecycle Manager and deploy the etcd operator for hands-on practice:

```bash theme={null}
# Install the Operator Lifecycle Manager
curl -sL https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.19.1/install.sh | bash -s v0.19.1

# Deploy the etcd operator
kubectl create -f https://operatorhub.io/install/etcd.yaml

# Retrieve the installed Cluster Service Version in the "my-etcd" namespace
kubectl get csv -n my-etcd
```

<Callout icon="lightbulb" color="#1CB2FE">
  This overview provides a high-level understanding of how operators simplify application management. A deep dive into operators will be explored in a dedicated future lesson. For exam preparation, note that most content primarily focuses on CRDs, making this article a valuable supplemental resource.
</Callout>

Thank you for reading, and we'll see you in the next lesson.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/77826599-d456-4cb5-8cbc-b713cc077b45/lesson/925da760-b102-43b4-a13d-6645f57e4bd1" />
</CardGroup>
