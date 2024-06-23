import http.server
import socketserver
import os
import subprocess

# Set the directory you want to serve
directory_to_serve = os.path.abspath('.')

# Change to the specified directory
os.chdir(directory_to_serve)

# Define the handler to use for serving files
Handler = http.server.SimpleHTTPRequestHandler

# Choose a port to serve on
PORT = 8000

# Get the local IP address
local_ip = subprocess.check_output('ipconfig').decode().split('Wireless LAN adapter Wi-Fi:')[1].split('IPv4 Address')[1].split(': ')[1].split('\n')[0]

# Create the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving directory {directory_to_serve} at http://{local_ip}:{PORT}")
    # Start the server
    httpd.serve_forever()
