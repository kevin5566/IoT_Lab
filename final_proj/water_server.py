## Central Pi as Watering Routing Control Server ##
## http://127.0.0.1:8080/1/2/3

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import time
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

## Variable ##
id=[]
x=[0]
y=[0]
l_bound=-1.0
h_bound=10.0

class Server(BaseHTTPRequestHandler):
    global id, x, y
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    
    def moving(self):
        time.sleep(5)   # delays 5 seconds
    
    def do_GET(self):
        ## http Cmd Processing ##
        cmd = self.path.strip().split('/')    # self.path
        del cmd[0]
        
        ## Moving Coordination ##
        x.append(int(cmd[0]))   # idx: i
        y.append(y[-1])         # idx: i
        x.append(x[-1])         # idx: i+1
        y.append(int(cmd[1]))   # idx: i+1
        
        ## Plot a Routing Graph ##
        routing_fig = plt.figure()
        ax=routing_fig.add_subplot(111)
        line=Line2D(x, y)
        ax.add_line(line)
        ax.set_xlim(l_bound, h_bound)
        ax.set_ylim(l_bound, h_bound)
        plt.show()
        
        ## Moving Function ##
        #self.moving()

        self._set_headers()
        self.wfile.write("hi!")

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

##  Referenece  ##
'''
https://stackoverflow.com/questions/28688210/use-line2d-to-plot-line-in-python
'''