> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi Container Pods

> This article explores multi-container pods in Kubernetes, highlighting their benefits for deploying and managing closely linked services together.

In this article, we explore the concept and benefits of multi-container pods in Kubernetes. By breaking down a monolithic application into smaller, independent microservices, you can deploy, manage, and scale each service individually. However, certain scenarios require two closely linked services to run together. For example, a web server might need to be paired with a dedicated logging agent. In this configuration, each web server instance is automatically associated with its own logging service, allowing both services to scale concurrently while keeping their codebases distinct.

Multi-container pods are designed to group containers that share the same lifecycle. This means they are created and terminated together, share a common network namespace (allowing seamless communication via localhost), and have access to shared storage volumes. This design simplifies configurations by eliminating the complexities of volume sharing and networking between separate pods.

<Frame>
  ![The image illustrates a diagram of multi-container pods, highlighting components like lifecycle, network, pod, and storage.](https://kodekloud.com/kk-media/image/upload/v1752869666/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Multi-Container-Pods/frame_90.jpg)
</Frame>

To create a multi-container pod, add the configuration for the new container under the `containers` array in your pod definition file. For instance, you can incorporate a container named "log-agent" alongside an existing web application container. The following YAML snippet demonstrates how to configure a pod that contains both a web application and its corresponding logging agent:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp
  labels:
    name: simple-webapp
spec:
  containers:
    - name: simple-webapp
      image: simple-webapp
      ports:
        - containerPort: 8080
    - name: log-agent
      image: log-agent
```

This configuration ensures that both containers share the same lifecycle, network, and storage resources, allowing them to work together seamlessly.

<Callout icon="lightbulb" color="#1CB2FE">
  Remember that the `containers` field is an array in the pod specification, which enables you to define and manage multiple containers under a single pod.
</Callout>

That concludes our discussion on multi-container pods. Next, proceed to the coding exercises section to practice configuring multi-container pods and reinforce your understanding of the concepts discussed here. Happy coding, and see you in the next article!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/2ddcf79b-abb0-4aeb-ad0c-3d54c7b4fc64/lesson/837b612e-ec6e-4bdc-ace5-cf259aa87da9" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/2ddcf79b-abb0-4aeb-ad0c-3d54c7b4fc64/lesson/2544dd45-d85b-44c7-9c49-06673ab37b19" />
</CardGroup>
