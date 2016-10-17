!/usr/bin/python
import os
os.system('yum install samba-client cifs-utils -y')
os.system('mkdir /file1')
var="//server12/share   /file1  cifs    username=sai,password=sai 0 0"
file=open("/etc/fstab","a")
file.write(var)
file.close()
os.system('mount -a')

