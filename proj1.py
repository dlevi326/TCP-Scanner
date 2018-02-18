#!/usr/bin/env python
import socket
import subprocess
import sys
from tqdm import tqdm

from datetime import datetime

if(len(sys.argv)<2):
	print("Error: Usage <./proj1.py> <hostname> [<-p> <port1:port2>]")
	print("Exiting")
	sys.exit()

# Get the desired server
serverName = sys.argv[1]
serverNameIP = socket.gethostbyname(serverName)

print("Scanning remote host "+str(serverNameIP)+"...")

# Start timer
t1 = datetime.now()


if(len(sys.argv)>2):
	if(sys.argv[2] == "-p"):
		if(len(sys.argv)!=4):
			print("Error: Usage <./proj1.py> <hostname> [<-p> <port1:port2>]")
			print("Exiting")
			sys.exit()
		else:
			ports = sys.argv[3].split(":")
			port1 = ports[0]
			port2 = ports[1]
	else:
		port1 = "1"
		port2 = "1024" 
else:
	port1 = "1"
	port2 = "1024"

if(int(port2)<=int(port1)):
	print("Error, port2 cannot be less than port1, exiting")
	sys.exit()



try:
	print ("Scanning Port: "+port1+" to Port: "+port2)
	for port in tqdm(range(int(port1),int(port2)+1)):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((serverNameIP, port))
		if result == 0:
			print("Port {}: 	 Open".format(port))
		sock.close()
		#else:
			# print "Port {}:		Closed".format(port)
		# sock.close()
	
		
except KeyboardInterrupt:
	print("You pressed Ctrl+C")
	sys.exit()

except socket.gaierror:
	print("Hostname error, exiting")
	sys.exit()

except socket.error:
	print("Error, could not connect to server, exiting")
	sys.exit()

# End timer
t2 = datetime.now()

# Calculates time
time = t2-t1
print("Scanning took: "+str(time)+" seconds")

