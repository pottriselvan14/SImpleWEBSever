from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
    <title>Simple Web Server</title>
</head>

<body>
    <h1>Simple Web Server</h1>

    <h2>Student Details</h2>

    <p><b>Register Number:</b> 26011881pyt </p>
    <p><b>Name:</b> POTTRISELVAN M</p>

    <h2>TCP/IP Protocol Suite</h2>

    <ul>
        <li>HTTP</li>
        <li>HTTPS</li>
        <li>FTP</li>
        <li>TCP</li>
        <li>IP</li>
        <li>DNS</li>
    </ul>

</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header("content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ("", 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()