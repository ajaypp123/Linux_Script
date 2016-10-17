#!/usr/bin/python
import os
os.system('yum install samba samba-client -y')
os.system('mkdir /test1')
os.system('touch /test1/test{1..10}.txt')
os.system('chcon -t samba_share_t /test1/')
os.system('chcon -t samba_share_t /test1/*')
os.system('useradd sai')
os.system('smbpasswd -a sai')
file=open("/etc/samba/smb.conf","a")
var="[share]\ncomment=Public Stuff\npath=/test1\npublic=yes\nwritable=yes\nbrowsable=yes\nvalid users=sai\nhosts allow=172.25.12."
file.write(var)
file.close()
os.system('testparm -t')
os.system('systemctl restart smb nmb')
os.system('systemctl enable smb nmb')
os.system('firewall-cmd --permanent --add-service=samba')
os.system('firewall-cmd --reload')

