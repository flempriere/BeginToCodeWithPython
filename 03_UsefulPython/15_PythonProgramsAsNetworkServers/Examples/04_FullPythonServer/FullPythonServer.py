"""
Example 15.4 Full Python Server

A small python web server utilising the inbuilt simple request handler
"""

import http.server

host_socket = 8080
host_ip = "localhost"

host_address = (host_ip, host_socket)
my_server = http.server.HTTPServer(host_address, http.server.SimpleHTTPRequestHandler)
print("Starting server on http://{0}:{1}".format(host_ip, host_socket))
my_server.serve_forever()
