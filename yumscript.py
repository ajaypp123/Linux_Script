#!/usr/bin/python
import os
b=raw_input("Enter file name without extension")
a="["+b+"]\ngpgcheck = 0\nenabled = 1\nbaseurl = http://content.example.com/rhel7.0/x86_64/dvd\nname = Sai Devkar"
os.system('rm /etc/yum.repos.d/*.repo')
file=open("/etc/yum.repos.d/"+b+".repo",'w')
file.write(a)
