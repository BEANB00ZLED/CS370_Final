import socket
import pickle
import globals

class Network:
    def __init__(self):
        #Creating the same socket that the server has
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = globals.SERVER
        self.port = globals.PORT
        #Connecting
        self.client.connect((self.server, self.port))
        
    def receive(self):
        try:
            #It is going to try and receive the game data
            data_received = self.client.recv(2048 * globals.BITMOD)
            #Deserialize the data into the object
            game = pickle.loads(data_received)
            return game
        except Exception as e:
            print(f"NETWORK SEND SHIT HIT THE FAN: {e}")
    
    def send(self, data):
        try:
            #Serialize the objet
            serialized_object = pickle.dumps(data)
            #Send the object to the server
            self.client.sendall(serialized_object)
        except Exception as e:
            print(f"NETWORK SEND SHIT HIT THE FAN {e}")