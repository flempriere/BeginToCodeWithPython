"""
Example 14.2 Sender

Send packets to specified port on another machine
"""

import socket
import time

target_ip = "127.0.1.1"  # set this to whatever the target ip is from Receiver.py
port = 10002

send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination_address = (target_ip, 10002)

while True:
    print("Sending")
    send_socket.sendto(b"Hello from me", destination_address)
    time.sleep(1)
