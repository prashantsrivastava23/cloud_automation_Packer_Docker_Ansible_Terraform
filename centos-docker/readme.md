# Automated script to create a docker image of "centos:latest" using packer.
* The image has a apache webserver installed and running.
* This is a basic script for introduction to autoation using ansible.

* After the docker image is created , it is pushed to hub.docker.com to your repository taking your credentials.
* After the image is pushed is can downloaded on any system from anywhere using the tag [username]/[image-name]:[version]

# The testing of the Image is also automated using a python script.
* Test 1: IP address of the OS Container.
* Test 2: Container is connected to the base system and internet connectivity is present. (Done using ping)
* Test 3: SSH into container and print the date.
* Test 4: Curl to check if the web-server is up and running.
