"""
Exercise 15.1 Persistent Message Board

Improves on the Message board example by persisting messages between sessions
and adding a date-time to a message
"""

import datetime
import http.server
import pickle
import urllib
import urllib.parse

datafile = "messages.pkl"


def load_messages(file):
    """
    Load the messages database from a file

    Parameters
    ----------
    file : str
        path to a file storing the messages database

    Returns
    -------
    list[(message, time)]
        A list of time-stamped messages
    """
    try:
        with open(datafile, "rb") as f:
            messages = pickle.load(f)
    except:  # noqa: E722
        print("Datafile missing, creating new log")
        messages = []
    return messages


def save_messages(file):
    """
    Save the messages into the database

    Parameters
    ----------
    file : path
        path to the file

    Returns
    -------
    None
    """
    with open(file, "wb") as f:
        pickle.dump(messages, f)


messages = load_messages(datafile)


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
        all_messages = "<br>\n".join(
            map(lambda a: "Posted: {0}<br>\n{1}".format(a[1], a[0]), messages)
        )
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
            save_messages(datafile)
        elif "message" in query_strings:
            message = query_strings["message"][0]
            messages.append((message, datetime.datetime.now()))
            save_messages(datafile)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message_text = self.make_page()
        message_bytes = message_text.encode()

        self.wfile.write(message_bytes)


host_socket = 8091
host_ip = "localhost"

host_address = (host_ip, host_socket)
server = http.server.HTTPServer(host_address, WebServerHandler)
print("Server now running on http://{0}:{1}".format(*host_address))
server.serve_forever()
