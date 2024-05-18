from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Parse the query parameters
        query_components = parse_qs(urlparse(self.path).query)
        name = query_components.get('name', ['world'])[0]

        # Create the response message
        message = f'Hello, {name}!'

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
