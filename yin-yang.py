import http.server

class yy_handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type:','text-html')
        self.end_headers()

        ying = """
        <html>
            <head>
                <title>YING</title>
            </head>
            <body>
                 <div align="center">
                    <h3>
                        Ying <a href="/yang"> zu Yang</a>
                    </h3>
                </div>
            </body>
        </html>
        """

        yang = """
        <html>
            <head>
                <title>YANG</title>
            </head>
            <body>
                 <div align="center">
                    <h3>
                        Yang <a href="/ying"> zu Ying</a>
                    </h3>
                </div>
            </body>
        </html>
        """

        if self.path == "/yang":
            self.wfile.write(yang.encode('utf-8'))
        else:
            self.wfile.write(ying.encode('utf-8'))

port = 1234
handler = yy_handler
adr = ('', port)

server = http.server.HTTPServer(adr,handler)
server.serve_forever()