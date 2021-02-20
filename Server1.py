# EECE 350 
# Assignment 1
# Romeo Al Ashkar
# 202000058
# Server

import socket
import datetime

port = 7
receive_buffer_size = 1000

s = ""

# Create socket:
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Bind socket:
server_socket.bind(("127.0.0.1",port))

# We do not need to listen or accept requests in UDP

# Receive echo request:
while True:
    m = server_socket.recvfrom(receive_buffer_size)
    s = m[0]
    if (s != ""):                        # Meaning the server received a request to echo           
      d = datetime.datetime.now()        # This is better than checking if the server received a certain request sent by the client
      print("Current date and time: " + str(d))   # As the server could be receiving different requests from different clients
    # Send echo response:
    server_socket.sendto(s,m[1])
    s = ""