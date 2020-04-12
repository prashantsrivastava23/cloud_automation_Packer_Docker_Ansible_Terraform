#!/bin/bash

yum clean all
yum install python3 -y
yum install python2 -y

#install httpd server
yum install httpd -y
yum install net-tools -y

#docker doesn't allow systemctl or service commands so working my way around
echo 'rm -f /var/run/httpd/httpd.pid' >> /root/.bashrc
echo 'rm -rf /var/run/httpd/*' >> /root/.bashrc
echo '/usr/sbin/httpd' >> /root/.bashrc
