import http.server
import urllib.parse


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type:','text-html')
        self.end_headers()
        parsed = urllib.parse.urlparse(self.path)
        query = parsed.query
        print("query: ",query)
        query_components = urllib.parse.parse_qsl(query)
        print("query_components",query_components)

        a = []
        for k, v in query_components:
            a.append(int(v))  # to_int_array

        if a[0] > a[-1]:
            e = "Error! Startwert muss kleiner als Endwert sein"
            self.wfile.write(e.encode("utf-8"))
        else:
            t_start = """
            <html>
                <head><title>Quadratzahlen</title></head>
                <body>
                    <style> table,td { border: 1px solid black;}</style>
                <table>
            """
        self.wfile.write(t_start.encode('utf-8'))

        for i in range(a[0], a[-1] + 1):
            msg = "<tr>" \
                    "<td>" + str(i) + "</td>" \
                    "<td>" + str(i * i) + "</td>" \
                  "</tr>"
            self.wfile.write(msg.encode("utf-8"))

        t_end = "</table></body></html>"
        self.wfile.write(t_end.encode("utf-8"))


port = 1234
handler = Handler
adr = ('', port)  # (path,port)

server = http.server.HTTPServer(adr, handler)
server.serve_forever()
