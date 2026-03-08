"""
Example 15.5 Message Board

Demonstrates receiving information from the user with a very basic
message board
"""

import http.server
import urllib
import urllib.parse

messages = []


class WebServerHandler(http.server.BaseHTTPRequestHandler):
    """
    Web handler for a message board
    """

    def make_page(self):
        """
        Generates the HTML page for a message board containing all messages

        Returns
        -------
        str
            the webpage as an html string
        """
        all_messages = "<br>\n".join(messages)
        page = """<html>
<body>
    <h1>Tiny Message Board</h1>
    <h2>Messages</h2>
    <p> {0} </p>
    <h2>New Messages</h2>
    <form method="post">
        <textarea name="message"></textarea>
        <button id="save" type="submit">Save Message</button>
    </form>
    <form method="post">
        <button name="clear" type="submit">Clear Messages</button>
    </form>
</body>
</html>"""
        return page.format(all_messages)

    def do_GET(self):
        """
        Handle a `GET` request

        Returns
        -------
        None
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message_text = self.make_page()
        print(message_text)

        message_bytes = message_text.encode()
        self.wfile.write(message_bytes)
        return

    def do_POST(self):
        """
        Handle a `POST` request

        Returns
        -------
        None
        """
        length = int(self.headers["Content-Length"])
        post_body_bytes = self.rfile.read(length)
        post_body_text = post_body_bytes.decode()
        query_strings = urllib.parse.parse_qs(post_body_text, keep_blank_values=True)

        if "clear" in query_strings:
            messages.clear()
        elif "message" in query_strings:
            message = query_strings["message"][0]
            messages.append(message)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message_text = self.make_page()
        message_bytes = message_text.encode()

        self.wfile.write(message_bytes)


host_socket = 8080
host_ip = "localhost"

host_address = (host_ip, host_socket)
server = http.server.HTTPServer(host_address, WebServerHandler)
print("Server now running on http://{0}:{1}".format(*host_address))
server.serve_forever()
