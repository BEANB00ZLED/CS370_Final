import socket
import pickle
import globals
import sys

class Network:
    def __init__(self):
        #Creating the same socket that the server has
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = globals.SERVER
        self.port = globals.PORT
        try:
            #Connecting
            self.client.connect((self.server, self.port))
            print(f"Connecting to server - {self.server}:{self.port}")
        except Exception as e:
            print(f"NETWORK CONNECT SHIT HIT THE FAN: {e}")
        
    def receive(self):
        try:
            print("Receiving data from server")
            #It is going to try and receive the game data
            data_received = self.client.recv(2048 * globals.BITMOD)
            #Deserialize the data into the object
            game = pickle.loads(data_received)
            print(f"Recieved: {type(game)} size {sys.getsizeof(game)}")
            return game
        except Exception as e:
            print(f"NETWORK SEND SHIT HIT THE FAN: {e}")
    
    def send(self, data):
        try:
            print("Sending data to server")
            #Serialize the objet
            serialized_object = pickle.dumps(data)
            #Send the object to the server
            self.client.sendall(serialized_object)
        except Exception as e:
            print(f"NETWORK SEND SHIT HIT THE FAN {e}")