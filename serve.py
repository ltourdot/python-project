#!/usr/bin/env python3
"""Simple HTTP server to serve the Wolf3D+ game."""
import http.server
import socketserver
import os
import webbrowser
import socket

PORT = 8080
GAME_DIR = os.path.join(os.path.dirname(__file__), "game")


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "localhost"


class GameHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=GAME_DIR, **kwargs)

    def log_message(self, format, *args):
        pass  # suppress request logs


if __name__ == "__main__":
    ip = get_local_ip()
    with socketserver.TCPServer(("", PORT), GameHandler) as httpd:
        print("=" * 50)
        print("  Wolf3D+ Game Server Running")
        print("=" * 50)
        print(f"\n  Local:   http://localhost:{PORT}")
        print(f"  Network: http://{ip}:{PORT}")
        print("\n  Open the Network URL on your phone")
        print("  (must be on same Wi-Fi network)")
        print("\n  Press Ctrl+C to stop\n")
        try:
            webbrowser.open(f"http://localhost:{PORT}")
        except Exception:
            pass
        httpd.serve_forever()
