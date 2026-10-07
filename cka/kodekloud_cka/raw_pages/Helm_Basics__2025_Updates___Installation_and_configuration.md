> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation and configuration

> This lesson explains the steps required to install Helm, a package manager for Kubernetes, on Linux systems.

This lesson explains the steps required to install Helm, a package manager for Kubernetes. Before starting, ensure you have a functioning Kubernetes cluster and that kubectl is properly configured. Verify that your kubeconfig file contains the correct credentials to access your Kubernetes cluster.

<Callout icon="lightbulb" color="#1CB2FE">
  Make sure your system has access to a working Kubernetes cluster and that
  `kubectl` is set up correctly. A valid kubeconfig file is essential for Helm
  to connect to your cluster.
</Callout>

Helm is compatible with Linux, Windows, and macOS. This guide focuses on installing Helm on Linux systems.

## Installing Helm on Linux

### Using Snap

If your system supports Snap, you can install Helm using the command below. The `--classic` option offers a more relaxed sandbox environment, enabling Helm to easily locate your kubeconfig file in your home directory and connect to your Kubernetes cluster:

```bash theme={null}
sudo snap install helm --classic
```

### Using APT (Debian/Ubuntu)

For apt-based systems such as Debian or Ubuntu, follow these steps to add the Helm package repository and its signing key, then install Helm:

```bash theme={null}
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt-get install apt-transport-https --yes
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

### Using PKG

On systems that support PKG, you can install Helm with the following command:

```bash theme={null}
pkg install helm
```

<Callout icon="lightbulb" color="#1CB2FE">
  For the most current installation procedures, always refer to the official
  Helm documentation.
</Callout>

## Conclusion

With Helm installed, you are now ready to explore its capabilities in your lab environment. This guide provided step-by-step instructions for various Linux distributions to help streamline your Helm installation process.

Happy Helming!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/10d7440b-907c-46da-ac5c-d833e7022375/lesson/c51c3be3-4f45-4e06-b304-7b38d66e076d" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/10d7440b-907c-46da-ac5c-d833e7022375/lesson/8443e601-9fef-4eec-999b-484482325bf0" />
</CardGroup>
