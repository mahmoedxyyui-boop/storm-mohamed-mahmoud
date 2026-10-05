# -*- coding: utf-8 -*-
"""
Local server runner for معارض محمد محمود دهب
"""
import http.server
import socketserver
import webbrowser
import os
import sys

# Change directory to this script's folder
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

PORT = 8080

class UTF8Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server():
    global PORT
    while PORT < 8100:
        try:
            handler = UTF8Handler
            with socketserver.TCPServer(("", PORT), handler) as httpd:
                url = f"http://localhost:{PORT}"
                print(f"=== Dahab Showroom Server Running at: {url} ===")
                # Open browser
                webbrowser.open(url)
                httpd.serve_forever()
        except OSError as e:
            if "Address already in use" in str(e) or e.errno == 10048:
                PORT += 1
            else:
                raise e

if __name__ == '__main__':
    run_server()
