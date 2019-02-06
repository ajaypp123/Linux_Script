#!/usr/bin/python

import os
import sys

a=sys.argv[1]
#a=raw_input('enter the path and file name at client side\n')
os.system('yum install -y nfs-utils nfs-utils-lib')
os.system('mkdir '+a)
file=open("/etc/fstab",'a')
file.write("\nnfsserver:/var/data\t"+a+"\tnfs\tdefaults\t0\t0")
file.close()
os.system('mount -a')
