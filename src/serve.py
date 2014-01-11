
import sys
import BaseHTTPServer, SimpleHTTPServer
import ssl

from os.path import expanduser
homedir = expanduser("~")
certfile = '%s/.server.pem' % homedir
#print certfile


if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

server_address = ('0.0.0.0',port)

httpd = BaseHTTPServer.HTTPServer(server_address, SimpleHTTPServer.SimpleHTTPRequestHandler)
sa = httpd.socket.getsockname()
print 'Serving HTTP on %s Port: %s' % (sa[0],sa[1])
httpd.socket = ssl.wrap_socket (httpd.socket, certfile=certfile , server_side=True)
httpd.serve_forever()
