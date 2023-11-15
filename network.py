import socket
from server import SERVER
from server import PORT
from server import BITMOD

class Network:
    def __init__(self):
        #Creating the same socket that the server has
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER
        self.port = PORT
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048 * BITMOD).decode()
        except:
            "NETWORK CONNECT SHIT HIT THE FAN"
            pass
        
n = Network()
