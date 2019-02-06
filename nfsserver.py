#!/usr/bin/python
import os
import sys

def usage():
        return "nfs-server.py <shared-dir-path>"

if sys.argv[1] == "-h":
        print usage()
        sys.exit(1)
else:
        a=sys.argv[1]

a=sys.argv[1]
os.system('mkdir '+ a)
data=a+"\t*(rw,sync)"
file=open("/etc/exports",'w')
file.write(data)
file.close()
os.system('yum install nfs-utils nfs-utils-lib rpcbind -y')
os.system('systemctl restart nfs')
os.system('systemctl restart nfs-server.service')
os.system('systemctl enable nfs')
os.system('systemctl enable nfs-server.service')
os.system('showmount -e')
os.system('firewall-cmd --permanent --add-service=nfs')
os.system('firewall-cmd --reload')
os.system('chmod 777 '+ a)
