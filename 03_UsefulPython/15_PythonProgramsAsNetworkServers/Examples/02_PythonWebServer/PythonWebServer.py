"""
Example 15.2 Python Web Server

A small python web server implementation using the html library
"""

import http.server


class WebServerHandler(http.server.BaseHTTPRequestHandler):
    """
    A basic example Web Server Handler to accept and serve requests
    """

    def do_GET(self):
        """
        Respond to a `GET` request

        This method is called when the server receives a GET request from
        the client. It sends back a fixed message back to the client
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message_text = """<html>
<body>
<p>hello from the Python server</p>
</body>
</html>
"""

        message_bytes = message_text.encode()
        self.wfile.write(message_bytes)
        return


host_socket = 8080
host_ip = "localhost"
host_address = (host_ip, host_socket)

my_server = http.server.HTTPServer(host_address, WebServerHandler)
print("Starting server of http://{0}:{1}".format(host_ip, host_socket))
my_server.serve_forever()
