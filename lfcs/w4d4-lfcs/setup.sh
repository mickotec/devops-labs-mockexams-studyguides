#!/usr/bin/env bash
set -euo pipefail
echo "[*] Setting up w4d4-lfcs (Compiling Software from Source Code)..."
sudo rm -rf /var/tmp/src-build /var/tmp/hello-c.tar.gz /usr/local/bin/hello-app /var/tmp/hello_output.txt
mkdir -p /tmp/pkg-source
cat << "EOF" > /tmp/pkg-source/hello.c
#include <stdio.h>
int main() {
    printf("LFCS Source Compilation Successful: v1.0.0\n");
    return 0;
}
EOF
tar -czf /var/tmp/hello-c.tar.gz -C /tmp/pkg-source hello.c
rm -rf /tmp/pkg-source
echo "[✓] Environment ready. Review tasks with: ./lab show w4d4-lfcs"
