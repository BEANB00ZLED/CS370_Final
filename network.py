import socket
import server

class Network:
    def __init__(self):
        #Creating the same socket that the server has
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server.SERVER
        self.port = server.PORT
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        
    def getPos(self):
        return self.pos
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048 * server.BITMOD).decode()
        except socket.error as e:
            print("NETWORK CONNECT SHIT HIT THE FAN: ", e)
            pass
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048*server.BITMOD).decode()
        except socket.error as e:
            print("NETWORK SEND SHIT HIT THE FAN: ", e)
        