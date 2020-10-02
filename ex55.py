# Write a Python to find local IP addresses using Python's stdlib

import socket

ip = socket.gethostbyname(socket.gethostname())
print("Local IP address:", ip)
