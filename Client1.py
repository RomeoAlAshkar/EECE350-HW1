# EECE 350 
# Assignment 1
# Romeo Al Ashkar
# 202000058
# Client

import socket
import time

server = "127.0.0.1"
port = 7
request_string = str.encode("Any string")
receive_buffer_size = 1000

# Create socket:
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# We do not establish a connection with the server since we are using UDP

# We need a list to store the RTT for each request/reply pair:
L = []

# 5 echo requests:
for i in range(0,5):
	# Time at start:
	start = (time.time()*1000)       # ms
	# Send echo request:
	client_socket.sendto(request_string,(server,port))
	# Receive echo response:
	r = client_socket.recvfrom(receive_buffer_size)
	# Time at end:
	end = (time.time()*1000)         # ms
	# Subtract to find time elapsed:
	L.append(end-start)
	# Display the RTT for each echo:
	print("RTT number " + str(i+1) + " is " + str(L[i]) + " ms")


# To find the avg RTT:
x = sum(L)
# We have 5 elements in L:
RTT_avg = x/5

# Close socket:
client_socket.close

# Print avg:
print("RTT average is: " + str(RTT_avg) + " ms")

# Make sure the echo works properly:
rs = r[0].decode()
print("Message echoed is: " + rs)