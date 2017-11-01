# ref: https://pastebin.com/5a34b1iw
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import grovepi
import time

Rpin = 3
Gpin = 5
Bpin = 9
Rvalue = 0
Gvalue = 0
Bvalue = 0

class Server(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global Rvalue, Gvalue, Bvalue
        global Rpin, Gpin, Bpin
        print 'Get path:', self.path
        cmd = self.path.strip().split('/')
        flag = 0
        try:
            if cmd[1] == "status":
                flag = 1
                print "RBG Value of LED"
                print "R: ",
                print Rvalue
                print "G: ",
                print Gvalue
                print "B: ",
                print Bvalue
            elif cmd[1] == "set":
                flag = 1
                if cmd[2] == 'R' or cmd[2] == 'r':
                    Rvalue = int(cmd[3])
                elif cmd[2] == 'G' or cmd[2] == 'g':
                    Gvalue = int(cmd[3])
                elif cmd[2] == 'B' or cmd[2] == 'b':
                    Bvalue = int(cmd[3])
                else:
                    flag = 0
                    print "INVALID COMMAND"
            else:
                print "INVALID COMMAND"
        except:
            print "INVALID COMMAND"
        grovepi.analogWrite(Rpin, Rvalue)
        grovepi.analogWrite(Gpin, Gvalue)
        grovepi.analogWrite(Bpin, Bvalue)
        if flag == 1:
            self._set_headers()
            sent = "R: "
            sent = sent + str(Rvalue)
            sent = sent + ", G: "
            sent = sent + str(Gvalue)
            sent = sent + ", B: "
            sent = sent + str(Bvalue)
            self.wfile.write(sent)
        else: 
            self._set_headers()
            self.wfile.write("INVALID COMMAMD")

def run(server_class=HTTPServer, handler_class=Server, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Server start on:', port
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
