import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_NAME = "Dual CI/CD Demo App"
APP_ENV = os.getenv("APP_ENV", "development")
PORT = int(os.getenv("APP_PORT"))


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        response = (
            f"Application: {APP_NAME}\n"
            f"Environment: {APP_ENV}\n"
            f"Status: Running Successfully\n"
        )

        self.wfile.write(response.encode())


def start_server():
    server = HTTPServer(("0.0.0.0", PORT), SimpleHandler)
    print("===================================")
    print(f"Starting {APP_NAME}")
    print(f"Environment : {APP_ENV}")
    print(f"Listening on port {PORT}")
    print("===================================")
    server.serve_forever()


if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nShutting down application gracefully...")
        time.sleep(1)
