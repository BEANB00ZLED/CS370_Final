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
    print(str(e))

s.listen(5)  # Allow up to 5 connections at a time
print("Waiting for a connection, Server Started")

#Create a serialized game object
game = pickle.dumps(Game())

while True:
    conn, addr = s.accept()
    print(f"Accepted connection from {addr}")
    
    try:
        #Serialize the object using pickle and send it to the client
        s.sendall(game)

        #Receive data from the client, this will still be serialized
        game = s.recv(2048 * globals.BITMOD)

        print(f"Received object from client: {game}")
    except Exception as e:
        print(f"SERVER SHIT HIT THE FAN: {e}")
    
    finally:
        s.close()