import os
import socket
import socketserver
import webbrowser
from functools import partial
import pyqrcode
import Authentication
import Create_zip


class Server:

    def __init__(self):
        self.PORT = 8080
        self.IP = socket.gethostbyname(socket.gethostname())
        self.hostname = socket.gethostname()
        self.link = "http://" + self.IP + ":" + str(self.PORT)

    def run(self, user, passwd, drctory):
            httpd = socketserver.TCPServer((self.IP, self.PORT), partial(
            Authentication.AuthHTTPRequestHandler,
            username=user,
            password=passwd,
            directory=drctory))
            print("Server Started")
            print("Server IP: ", self.IP)
            print("Server Hostname: ", self.hostname)
            print("Server Port: ", self.PORT)
            print("Server Link: ", self.link)
            httpd.serve_forever()

    def qr(self):
        url = pyqrcode.create(self.link)
        url.svg("myqr.svg", scale=8)
        webbrowser.open('myqr.svg')



def main():
    # desktop path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                           'Desktop')
    os.chdir(desktop)


    server = Server()
    server.run('user', 'passwd', desktop)

    server.qr()


if __name__ == '__main__':
    Create_zip.creation()
    main()


