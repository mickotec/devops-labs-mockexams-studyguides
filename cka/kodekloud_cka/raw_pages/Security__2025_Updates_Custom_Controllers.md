> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 2025 Updates Custom Controllers

> This lesson covers developing custom controllers for Kubernetes, focusing on monitoring FlightTicket objects and integrating with a flight booking API.

In this lesson, we delve into developing custom controllers for Kubernetes. Building on our previous work, we have already defined a custom resource and created FlightTicket objects with data stored in etcd. The next step is to continuously monitor these objects and perform corresponding actions—such as calling a flight booking API to book, modify, or cancel flight tickets. This process is the core function of a custom controller.

A controller is a process running in a loop that monitors the Kubernetes cluster and reacts to changes in specific objects (in this case, FlightTicket resources). Consider the following FlightTicket definition as a starting point:

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

You can create the resource using:

```bash theme={null}
kubectl create -f flightticket.yml
```

The command output confirms the creation:

```bash theme={null}
flightticket "my-flight-ticket" created
```

To check the status of your FlightTicket, run:

```bash theme={null}
kubectl get flightticket
```

Expected output:

```text theme={null}
NAME               STATUS
My-flight-ticket   Pending
```

<Callout icon="lightbulb" color="#1CB2FE">
  While it is possible to write a controller in a language like Python, challenges such as managing expensive API calls, and building your own queuing and caching mechanisms might arise.
</Callout>

Developing the controller in Go using the Kubernetes Go client offers a more efficient approach. It provides libraries like shared informers that include built-in queuing and caching support.

## Getting Started with the Custom Controller

To begin, clone the SampleController repository from GitHub. Ensure that the Go programming language is installed on your machine, then execute the following command in your terminal:

```bash theme={null}
git clone https://github.com/kubernetes/sample-controller.git
```

The terminal should display output similar to:

```text theme={null}
Cloning into 'sample-controller'...
Resolving deltas: 100% (15787/15787), done.
```

Change into the cloned directory:

```bash theme={null}
cd sample-controller
```

Customize the file `controller.go` with your specific business logic. One important function within your controller might involve making a call to the flight booking API after detecting changes in FlightTicket objects.

Once you’ve incorporated your custom logic, build the controller with the command:

```bash theme={null}
go build -o sample-controller .
```

During the build process, you may encounter messages such as:

```text theme={null}
go: downloading k8s.io/client-go v0.0.0-20211001003700-dbfa30b9d908
go: downloading golang.org/x/text v0.3.6
```

Run the controller by specifying the path to your kubeconfig file:

```bash theme={null}
./sample-controller -kubeconfig=$HOME/.kube/config
```

You should see log messages that confirm the event handlers are being set up and that the FlightTicket controller is starting:

```text theme={null}
I1013 02:11:07.489479  40117 controller.go:115] Setting up event handlers
I1013 02:11:07.489701  40117 controller.go:156] Starting FlightTicket controller
```

## Inside the Controller Code

Your controller code might include sections like the following:

```go theme={null}
package flightticket

var controllerKind = apps.SchemeGroupVersion.WithKind("Flightticket")

// Code hidden for brevity

// Run begins watching and syncing.
func (dc *FlightTicketController) Run(workers int, stopCh <-chan struct{}) {}

// Code hidden for brevity

// callBookFlightAPI triggers the flight booking process.
func (dc *FlightTicketController) callBookFlightAPI(obj interface{}) {}
```

The controller leverages the specified kubeconfig file to authenticate with the Kubernetes API server. It watches for changes to FlightTicket objects and, upon detecting a creation or modification, it executes your custom logic—such as interfacing with the flight booking API—to reconcile the desired state.

<Callout icon="triangle-alert" color="#FF6B6B">
  Ensure your API calls are handled efficiently to avoid timeouts and performance issues in production environments.
</Callout>

## Deploying Your Controller

Once your custom controller is fully verified and functional, you may want to package it as a Docker image and deploy it within your Kubernetes cluster as a pod or Deployment. This approach streamlines updates by avoiding the need for manual rebuilding and restarting of the controller with every change.

## Summary

This lesson provided a comprehensive overview of building a custom controller in Kubernetes. It discussed:

* How to define custom resources for FlightTickets.
* Monitoring and reacting to changes using controllers.
* Building the controller in Go with the built-in queuing and caching support provided by the Kubernetes Go client.
* Deploying your controller in a production environment.

Understanding how Custom Resource Definitions (CRDs) and controllers work together is fundamental, especially since exam questions may cover creating CRDs, managing CRD files, or interacting with existing controllers. Operators, which extend controller functionality further, are another exciting area to explore.

For more details on Kubernetes concepts, check out these resources:

* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [GitHub Repository for SampleController](https://github.com/kubernetes/sample-controller)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/77826599-d456-4cb5-8cbc-b713cc077b45/lesson/61045090-37ea-444c-9168-0fe993d8ffee" />
</CardGroup>
