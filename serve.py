#!/usr/bin/env python3
"""Servidor local para testar o site. Uso: python3 serve.py [porta]"""
import http.server
import socketserver
import sys
import webbrowser

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Sem cache, pra sempre ver a versao mais recente ao dar F5
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}/"
    print(f"Servindo Arrombados Anonimos em {url}")
    print("Ctrl+C para parar.")
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor parado.")
