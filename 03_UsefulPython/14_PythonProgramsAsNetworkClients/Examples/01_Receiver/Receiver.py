"""
Example 14.1 Receiver

Receive packets on a specified port from another machine
"""

import socket

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("The IP address of this computer is:", host_ip)
port = 10002

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listen_address = (host_ip, port)

listen_socket.bind(listen_address)

print("Listening...")
while True:
    reply = listen_socket.recvfrom(4096)
    print(reply)
