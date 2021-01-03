import http.server
import urllib.parse

class Quadrat(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        components = urllib.parse.parse_qsl(parsed.query)
        von_param = 1
        bis_param = 10
        for c in components:
            if c[0] == "von":
                von_param = int(c[1])
            if c[0] == "bis":
                bis_param = int(c[1])
        self.send_response(200)
        self.send_header("content-type: ", "html-text")
        self.end_headers()
        msg1 = """
        <html>
            <head>
                <title>Quadratzahlen</title>
            </head>
            <body>
                <table border="2">
        """
        msg2 = """
                </table>
            </body>
        </html>
        """

        msg = msg1

        for i in range(von_param,bis_param+1):
            msg = msg + "<tr><td>" + str(i) + "</td><td>" + str(i*i) +"</td></tr>"

        msg = msg + msg2

        self.wfile.write(msg.encode("utf-8"))

port = 1234
adr = ("",port)
handler = Quadrat
server = http.server.HTTPServer(adr,handler)
server.serve_forever()