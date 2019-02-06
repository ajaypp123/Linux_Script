#!/usr/bin/python

import os
import sys

def usage():
        return "nfs-client.py <shared-dir-path> <nfs-server-hostname>"

if sys.argv[1] == "-h":
        print usage()
        sys.exit(1)
else:
        a=sys.argv[1]

os.system('yum install -y nfs-utils nfs-utils-lib')
os.system('mkdir '+ a)
file=open("/etc/fstab",'a')
file.write("\n" + sys.argv[2] + ":/var/data\t"+a+"\tnfs\tdefaults\t0\t0")
file.close()
os.system('mount -a')
