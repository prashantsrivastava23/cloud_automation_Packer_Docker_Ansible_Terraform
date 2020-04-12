#!/usr/bin/python36

import os
import subprocess as sp
import getpass

print("Validating Image...")
s1 = sp.getstatusoutput("packer validate packer_centos.json")
print(s1[1])	
if(s1[0] == 0):
	print("\nCreating Image...")
	print("\nLogin to Docker Hub..")
	unm = input("Enter username for hub.docker.com: ")
	pwd = getpass.getpass("Enter username for hub.docker.com: ")
	s2 = sp.getoutput("docker login --username " + unm + " --password " + pwd + " ")
	print(s2)
	print("\nBuilding Image...")	
	s3 = sp.getstatusoutput("packer build packer_centos.json")
	print(s3[1])
	if(s3[0] == 0):
		print("\nImage successfully created and pushed to DockerHub.")
	sp.getoutput("docker logout")		
