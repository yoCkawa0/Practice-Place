from http.server import BaseHTTPRequestHandler, HTTPServer

with open('index.html', mode='r')as f:
    index = f.read()


class HelloServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        # self.wfile.write(b'Sample web server!!')
        # self.wfile.write(index.encode('utf-8'))
        html = index.format(
            title="Hello World",
            message="Welcome to HTTPServer!!"
        )
        self.wfile.write(html.encode('utf-8'))
        return


server = HTTPServer(('', 8080), HelloServerHandler).serve_forever()
