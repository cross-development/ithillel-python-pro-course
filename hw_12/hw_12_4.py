"""
Simple Multithreaded HTTP Server.

This module starts an HTTP server in a separate thread and serves basic GET requests.
"""

from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleRequestHandler(BaseHTTPRequestHandler):
    """
    Handles HTTP GET requests.
    """

    def do_GET(self) -> None:
        """
        Handles a GET request by responding with a simple message.
        """

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, world!")


def serve_forever(server: HTTPServer) -> None:
    """
    Runs the HTTP server indefinitely.

    Args:
        server (HTTPServer): The HTTP server instance.
    """

    server.serve_forever()


def start_server(host: str = "localhost", port: int = 8080) -> HTTPServer:
    """
    Starts the HTTP server on a separate thread.

    Args:
        host (str, optional): The server host. Defaults to "localhost".
        port (int, optional): The server port. Defaults to 8080.

    Returns:
        HTTPServer: The running HTTP server instance.
    """

    server = HTTPServer((host, port), SimpleRequestHandler)
    thread = Thread(target=serve_forever, args=(server,), daemon=True)
    thread.start()

    print(f"Server is running on http://{host}:{port}")

    return server


if __name__ == "__main__":
    new_server = start_server()
    input("Press Enter to stop the server...\n")
    new_server.shutdown()
    print("Server stopped.")
