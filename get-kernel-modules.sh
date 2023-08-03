mkdir -p challenge
# on container: mkdir -p /lib/modules/$(uname -r)/kernel/fs/

cp /lib/modules/$(uname -r)/kernel/fs/binfmt_misc.ko challenge