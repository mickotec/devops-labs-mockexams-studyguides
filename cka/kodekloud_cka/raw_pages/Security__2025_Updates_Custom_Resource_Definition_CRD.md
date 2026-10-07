> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 2025 Updates Custom Resource Definition CRD

> This guide explores Custom Resource Definitions in Kubernetes, detailing standard resources, custom resources like FlightTicket, and the need for custom controllers.

In this guide, we dive into Custom Resource Definitions (CRDs) in Kubernetes, beginning with an overview of standard Kubernetes resources and controllers before extending these principles to custom resources like our FlightTicket example.

***

## Understanding Standard Kubernetes Resources and Controllers

Kubernetes relies on built-in controllers to manage standard resources. For instance, when you create a Deployment, Kubernetes stores the desired state in its etcd data store and automatically manages related ReplicaSets and Pods. The deployment controller continuously monitors the Deployment and ensures that the cluster state matches the desired configuration. Creating a Deployment with three replicas will result in three Pods being deployed.

Below is an example YAML file defining a Deployment:

```yaml theme={null}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      type: front-end
  template:
    metadata:
      name: myapp-pod
      labels:
        type: front-end
    spec:
      containers:
        - image: nginx
```

After saving the above content as `deployment.yml`, run the following commands to create, view, and delete the Deployment:

```bash theme={null}
kubectl create -f deployment.yml
# Output:
kubectl get deployments
# Output:
# NAME              DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
kubectl delete -f deployment.yml
# Output:
# deployment "myapp-deployment" deleted
```

The deployment controller (implemented in Go within the Kubernetes source code) handles the creation of a ReplicaSet when a new Deployment is detected. The ReplicaSet then creates the required Pods based on the Deployment's specification. This dynamic process ensures that the actual state of the cluster continuously converges with the desired state.

***

## Custom Resources and Controllers: The Flight Ticket Example

Building on the standard resource management, you can extend Kubernetes by defining custom resources. Imagine a scenario where you want to manage flight ticket bookings directly in Kubernetes. With a custom resource called FlightTicket, you can create objects representing flight ticket bookings, list them, and delete them as needed.

### FlightTicket Object Definition

Below is an example YAML file that defines a FlightTicket object:

```yaml theme={null}
apiVersion: flights.com/v1
kind: FlightTicket
metadata:
  name: my-flight-ticket
spec:
  from: Mumbai
  to: London
  number: 2
```

To create and manage this custom resource, execute the following commands:

```bash theme={null}
kubectl create -f flightticket.yml
# Output:
kubectl get flightticket
# Output:
# NAME              STATUS
kubectl delete -f flightticket.yml
# Output:
# flightticket "my-flight-ticket" deleted
```

At this stage, the FlightTicket object is stored in etcd; however, it does not trigger any actions. To automate operations—such as interfacing with an external API (e.g., bookflight.com/API) to book or cancel a ticket—you need a custom controller.

### Custom Controller for FlightTicket

A custom controller, typically written in Go, monitors FlightTicket objects. When a FlightTicket is created, updated, or deleted, the controller calls an external API to perform actions such as booking or canceling a flight. Below is a streamlined Go snippet to illustrate the controller's logic:

```go theme={null}
package flightticket

import (
	// Imports omitted for brevity
)

var controllerKind = apps.SchemeGroupVersion.WithKind("FlightTicket")

// Run begins watching and syncing FlightTicket resources.
func (dc *FlightTicketController) Run(workers int, stopCh <-chan struct{}) {
	// Controller loop implementation here
}

// callBookFlightAPI books a flight ticket when a FlightTicket resource is created.
func (dc *FlightTicketController) callBookFlightAPI(obj interface{}) {
	// API calling logic here
}
```

<Callout icon="lightbulb" color="#1CB2FE">
  Without this custom controller, FlightTicket objects remain static data in etcd, and no automated flight booking actions are performed.
</Callout>

### Handling Resource Creation Errors

If you create a FlightTicket object before Kubernetes is aware of its type, you will encounter an error similar to:

```bash theme={null}
kubectl create -f flightticket.yml
# Output:
# no matches for kind "FlightTicket" in version "flights.com/v1"
```

This error appears because Kubernetes does not recognize the FlightTicket resource type. To resolve this, you must first establish a Custom Resource Definition (CRD) for FlightTicket.

***

## Defining a Custom Resource with a CRD

A Custom Resource Definition (CRD) informs Kubernetes about a new resource type, detailing its metadata, scope (namespaced or cluster-scoped), API group, naming conventions (singular, plural, and short names), supported versions, and a validation schema using OpenAPI v3.

Below is a sample CRD for the FlightTicket resource:

```yaml theme={null}
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: flighttickets.flights.com
spec:
  group: flights.com
  scope: Namespaced
  names:
    plural: flighttickets
    singular: flightticket
    kind: FlightTicket
    shortNames:
      - ft
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                from:
                  type: string
                to:
                  type: string
                number:
                  type: integer
                  minimum: 1
```

Save this content as `flightticket-custom-definition.yml` and apply it to your Kubernetes cluster using:

```bash theme={null}
kubectl create -f flightticket-custom-definition.yml
# Output:
# customresourcedefinition "flighttickets.flights.com" created
```

Once the CRD is successfully created, Kubernetes can recognize and store FlightTicket objects. However, remember that without the corresponding custom controller, FlightTicket objects will remain as passive data entries.

***

## Summary

In this guide, we:

• Explored how standard Kubernetes resources, such as Deployments, are managed using built-in controllers.\
• Demonstrated the creation, listing, and deletion of a Deployment using a YAML file and kubectl commands.\
• Introduced custom resources with a FlightTicket example, emphasizing the need for a Custom Resource Definition (CRD) and a custom controller to automate actions.

Future articles will cover the implementation of a custom controller to automatically process FlightTicket events and integrate with external APIs.

For more details on Kubernetes resources and controllers, check out the [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/77826599-d456-4cb5-8cbc-b713cc077b45/lesson/79472710-6891-42a4-a483-fa6db0d2e890" />
</CardGroup>
