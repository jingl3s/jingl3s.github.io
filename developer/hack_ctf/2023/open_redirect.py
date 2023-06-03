import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "::"
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

class HTTPServerV6(HTTPServer):
  address_family = socket.AF_INET6

if __name__ == "__main__":
    webServer = HTTPServerV6((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")