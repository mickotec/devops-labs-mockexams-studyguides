# [CKAD W5D6-CKAD] Solution & Technical Walkthrough

### Tasks & Official Solution
### Official Solution: Jobs & CronJobs
```bash
ssh controlplane 'cat << "EOF_ALL" | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: db-indexer
  namespace: ckad-w5d6
spec:
  completions: 3
  parallelism: 2
  backoffLimit: 3
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: indexer
        image: busybox:1.36
        command: ["sh", "-c", "echo Indexing complete; exit 0"]
---
apiVersion: batch/v1
kind: CronJob
metadata:
  name: log-archiver
  namespace: ckad-w5d6
spec:
  schedule: "*/5 * * * *"
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 3
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
          - name: archiver
            image: busybox:1.36
            command: ["echo", "Archive completed"]
EOF_ALL
'
```
