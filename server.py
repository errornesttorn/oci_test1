# Import the http.server and os modules
import http.server
import os

# Define a handler class that inherits from BaseHTTPRequestHandler
class MyHandler(http.server.BaseHTTPRequestHandler):

    # Override the do_GET method to handle GET requests
    def do_GET(self):
        # Get the path of the index.html file
        index_path = os.path.join(os.path.dirname(__file__), "index.html")
        # Check if the file exists
        if os.path.exists(index_path):
            # Send a 200 OK response
            self.send_response(200)
            # Send the headers
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Open the file and read its content
            with open(index_path, "rb") as f:
                content = f.read()
            # Write the content to the body
            self.wfile.write(content)
        else:
            # Send a 404 Not Found response
            self.send_error(404, "File not found")

# Create a server object using the handler class and a port number
server = http.server.HTTPServer(("", 8000), MyHandler)

# Start the server and print a message
print("Server running on port 8000")
server.serve_forever()
