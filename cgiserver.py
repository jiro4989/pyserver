import http.server

server_address = ("", 8080)
handler = http.server.CGIHTTPRequestHandler
server = http.server.HTTPServer(server_address, handler)
server.serve_forever()

