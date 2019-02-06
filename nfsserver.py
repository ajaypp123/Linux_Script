#!/usr/bin/python
import os
import sys

a=sys.argv[1]
#a=raw_input("Enter the path name of folder to be shared")
os.system('mkdir '+a)
data=a+"\t*(rw,sync)"
file=open("/etc/exports",'w')
file.write(data)
file.close()
os.system('yum install nfs-utils rpcbind nfs-utils-lib -y')
os.system('systemctl restart nfs')
os.system('systemctl restart nfs-server.service')
os.system('showmount -e')
os.system('firewall-cmd --permanent --add-service=nfs')
os.system('firewall-cmd --reload')
os.system('chmod 777 '+a)
