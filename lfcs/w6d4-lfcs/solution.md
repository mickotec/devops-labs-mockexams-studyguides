# [LFCS W6D4-LFCS] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Extend LV:
`sudo lvextend -L +100M /dev/vg_expand/lv_store`

2. Resize filesystem:
`sudo resize2fs /dev/vg_expand/lv_store`
