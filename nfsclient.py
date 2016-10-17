#!/usr/bin/python
import os
a=raw_input('enter the path and file name at client side\n')
os.system('mkdir '+a)
file=open("/etc/fstab",'a')
file.write("\nserver14:/nfsfile\t"+a+"\tnfs\tdefaults\t0\t0")
file.close()
os.system('mount -a')

