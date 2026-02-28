from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# HTTP Status Codes
class HttpStatus:
    OK = 200
    CREATED = 201
    NOT_FOUND = 404
    BAD_REQUEST = 400


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status_code):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers(HttpStatus.OK)
            response = {
                "message": "Server running successfully without Flask",
                "status": HttpStatus.OK
            }
            self.wfile.write(json.dumps(response).encode())

        elif self.path == "/about":
            self._set_headers(HttpStatus.OK)
            response = {
                "project": "Simple Python API",
                "version": "Python 3.13"
            }
            self.wfile.write(json.dumps(response).encode())

        else:
            self._set_headers(HttpStatus.NOT_FOUND)
            response = {
                "error": "Route not found"
            }
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == "/data":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data)

                self._set_headers(HttpStatus.CREATED)
                response = {
                    "message": "Data received successfully",
                    "received_data": data
                }
                self.wfile.write(json.dumps(response).encode())

            except json.JSONDecodeError:
                self._set_headers(HttpStatus.BAD_REQUEST)
                response = {"error": "Invalid JSON format"}
                self.wfile.write(json.dumps(response).encode())
        else:
            self._set_headers(HttpStatus.NOT_FOUND)
            response = {"error": "Route not found"}
            self.wfile.write(json.dumps(response).encode())


def run_server():
    server_address = ("localhost", 5000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server running at http://localhost:5000")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()