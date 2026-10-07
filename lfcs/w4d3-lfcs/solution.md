# [LFCS W4D3-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Query tar:
`dpkg -S /usr/bin/tar > /var/tmp/tar_package.txt`
`dpkg -l tar >> /var/tmp/tar_package.txt`

2. Hold tar:
`sudo apt-mark hold tar`

3. Download deb:
`cd /var/tmp/pkg_cache && apt-get download tree`
