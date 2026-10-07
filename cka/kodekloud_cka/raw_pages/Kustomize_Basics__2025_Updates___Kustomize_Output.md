> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Kustomize Output

> This article explains how to deploy and delete Kubernetes resources using Kustomize in conjunction with the kubectl command.

In the previous lesson, we explored the Kustomize build command. Running this command processes all defined resources, applies the necessary transformations, and outputs the final configurations to your console. Remember, these configurations are not automatically deployed to your Kubernetes cluster. When you inspect your cluster using commands like `kubectl get pods`, `kubectl get deployments`, or `kubectl get services`, you'll notice that no resources have been created yet.

<Callout icon="lightbulb" color="#1CB2FE">
  Kustomize focuses on building configurations. To deploy these configurations, you must combine it with the `kubectl apply` command.
</Callout>

## Deploying Generated Configurations

To deploy your configurations, you can chain the Kustomize build command with the `kubectl apply` command using the Linux pipe (`|`). The command below demonstrates how to build and immediately apply the configurations from the `k8s/` directory:

```bash theme={null}
$ kustomize build k8s/ | kubectl apply -f -
service/nginx-loadbalancer-service created
deployment.apps/nginx-deployment created
```

The Linux pipe utility takes the output from `kustomize build k8s/` and supplies it as the input to `kubectl apply -f -`. This method leverages the familiar `kubectl apply` command to create resources like the nginx deployment and the nginx service.

Alternatively, the `kubectl` command includes native support for Kustomize. By using the `-k` flag, you can apply configurations directly from the directory containing your `kustomization.yaml` file:

```bash theme={null}
$ kubectl apply -k k8s/
service/nginx-loadbalancer-service created
deployment.apps/nginx-deployment created
```

## Deleting Resources Using Kustomize

Removing resources works in a similar way to deploying them. You simply replace the word `apply` with `delete`. This section demonstrates how to delete resources with both methods.

### Using the Pipe Method

The following command uses the pipe utility to delete the previously created resources:

```bash theme={null}
$ kustomize build k8s/ | kubectl delete -f -
service "nginx-loadbalancer-service" deleted
deployment.apps "nginx-deployment" deleted
```

### Using the Native kubectl Command

You can also use the `kubectl` command with the `-k` flag to delete the resources:

```bash theme={null}
$ kubectl delete -k k8s/
service "nginx-loadbalancer-service" deleted
deployment.apps "nginx-deployment" deleted
```

This article has demonstrated how to both apply and delete Kubernetes resources using Kustomize in combination with `kubectl`. For more details on using Kubernetes tools and best practices, refer to the [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/031e84b8-bcbc-4f39-94d6-66d93b05bddc/lesson/b2ed246e-9cf4-484f-b1e0-8fad82d87034" />
</CardGroup>
