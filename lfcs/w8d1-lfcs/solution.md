# [LFCS W8D1-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Run web container:
`podman run -d --name web-container -p 8085:80 docker.io/library/nginx:alpine`

2. Run data worker with volume:
```bash
sudo mkdir -p /var/data/worker && sudo chmod 777 /var/data/worker
podman run -d --name data-worker -v /var/data/worker:/data:Z docker.io/library/busybox:1.36 sh -c "while true; do date >> /data/timestamp.log; sleep 2; done"
```

3. Extract IP:
`podman inspect web-container --format '{{.NetworkSettings.IPAddress}}' > /var/tmp/container_ip.txt`
If empty (host networking / rootless), extract container ID:
`podman inspect web-container --format '{{.Id}}' > /var/tmp/container_ip.txt`
