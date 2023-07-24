#!/bin/bash

# send stdout/stderr to logfile
exec >.initlog 2>&1

# Add binfmt kernel module
sudo insmod /lib/modules/$(uname -r)/kernel/fs/binfmt_misc.ko
