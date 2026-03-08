"""
Example 15.3 Python File Server

A python web server that returns a file
"""

import http.server


class WebServerHandler(http.server.BaseHTTPRequestHandler):
    """
    A simple web handler that can serve pages in response to a `GET` request
    """

    def do_GET(self):
        """
        Handle a `GET` request

        This method is called when the server receives a `GET`
        request from the client. It opens a file with the requested
        path and sends back the contents
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        file_path = self.path[1:]
        with open(file_path, "r") as input_file:
            message_text = input_file.read()

        message_bytes = message_text.encode()
        self.wfile.write(message_bytes)

        return


host_socket = 8080
host_ip = "localhost"

host_address = (host_ip, host_socket)

my_server = http.server.HTTPServer(host_address, WebServerHandler)
print("Starting server on http://{0}:{1}".format(host_ip, host_socket))
my_server.serve_forever()
