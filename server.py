import socket
from _thread import *
import sys
import pickle
from game import Game
import globals

server = globals.SERVER
port = globals.PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(f"SOCKET BIND SHIT HIT THE FAN: {e}")

s.listen(1)  # Allow up to # connections at a time
print(f"Waiting for a connection, Server Started - {server}:{port}")

#Create a serialized game object
game = pickle.dumps(Game())

while True:
    try:
        conn, addr = s.accept()
        print(f"Accepted connection from {addr}")
        
        #Receive data from the client, this will still be serialized
        game = s.recv(2048 * globals.BITMOD)
        #Deserialize the object
        game = pickle.loads(game)

        print(f"Received object from client: {game}")
    except Exception as e:
        print(f"SERVER SHIT HIT THE FAN: {e}")
    
    finally:
        s.close()