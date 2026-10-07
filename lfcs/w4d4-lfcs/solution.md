# [LFCS W4D4-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Extract:
`mkdir -p /var/tmp/src-build`
`tar -xzf /var/tmp/hello-c.tar.gz -C /var/tmp/src-build`

2. Compile:
`sudo gcc -O2 /var/tmp/src-build/hello.c -o /usr/local/bin/hello-app`
`sudo chmod 755 /usr/local/bin/hello-app`

3. Verify:
`/usr/local/bin/hello-app > /var/tmp/hello_output.txt`
