#!/usr/bin/python
import os
data="<VirtualHost *:80>\nServerAdmin	webmaster@desktop6.example.com\nDocumentRoot	\"/var/www/html\"\nServerName	desktop6.example.com\n</VirtualHost>\n<Directory /var/www/html>\nrequire all granted\n</Directory>"

data1=raw_input("\nEnter Data you want to write in index file\n")

os.system('yum install httpd -y')
os.system('rm -f /var/www/html/*.html')
file=open("/var/www/html/index.html","w")
file.write(data1)
file.close()




file=open("/etc/httpd/conf.d/one.conf","w")
file.write(data)
file.close()

os.system('httpd -t')
os.system('systemctl restart httpd')
os.system('systemctl  enable httpd')
os.system('firewall-cmd --permanent --add-service=http')
os.system('firewall-cmd --reload')
