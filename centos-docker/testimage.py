#!/usr/bin/python36

import os
import subprocess as sp
import time

print(".....Testing an Image.....")
name = input("Input the tag of the Image to test: ")
time.sleep(2)
print("Test image is being created...")
s1 = sp.getstatusoutput("docker run -itd --name test " + name + " ")
print(s1[1])
if s1[0] == 0:
	print("Test Image Created.\nID: "+ s1[1])
	num = 0

	print("\nTest 1: Finding the IP Address of the Container...")
	ip = sp.getstatusoutput("docker exec test ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'")
	if ip[0] == 0: 
		print(ip[1])
		num = num + 1 
	else: print("\nError in finding the IP Address.")

	print("\nTest 2: Check for connectivity with base system. This is present by default in Docker.")
	s2 = sp.getstatusoutput("docker exec test ping -c 5 " + ip[1] + " ")
	if s2[0] == 0:
		print(s2[1])
		num = num + 1
	else: print("\nError in pinging from the base system to the container.")

	print("\nTest 3: SSH into the container and print date")
	s3 = sp.getstatusoutput('docker exec test date')
	if s3[0] == 0:
		print(s3[1])
		num = num + 1
	else: print("\nError in executing date command from the container.")

	print("\nTest 4: Check if the Webserver is up and runnning")
	s4 = sp.getstatusoutput("docker exec test curl " + ip[1] + " ")
	if s4[0] == 0:
		print(s4[1])
		num = num + 1
	else: print("\nError in the Web Server.")

	print("\nDestroying Image")
	sp.getoutput("docker stop test")
	sp.getoutput("docker rm -f test")
	sp.getoutput("docker rmi -f " + name + " ")

	if(ip[0] == s2[0] == s3[0] == s4[0] == 0):
		print("Testing of Image Successful.")
	else:
		print(num,"/ 4 tests were successful.") 
else:
	print("The Image was not found.")
