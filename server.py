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
game = Game()
#Send it out initially

conn, addr = s.accept()
print(f"Accepted connection from {addr}")

try:
    #Serialize and send the object so that the game can startup
    print("Sending initial obejct to client")
    game = pickle.dumps(game)
    conn.sendall(game)
    while True:
        #Receive data from the client, this will still be serialized
        print("Server received object from client")
        game = conn.recv(2048 * globals.BITMOD)
        #Make sure we received data from the client
        if not game:
            print("Client disconnected")
            break

        #Deserialize the object
        game = pickle.loads(game)
        #Insert any changes you want to make to the game object here
        print(f"Game object contains")
        print(f"Deck: {len(game.game_deck.game_deck)} tiles left")
        print(f"Tiles in play {len(game.tile_list)}")
        print(f"Meeples in play {len(game.meeple_list)}")
        #Serialize and send the object back
        print("Server sending object to client")
        game = pickle.dumps(game)
        conn.sendall(game)
except Exception as e:
    print(f"SERVER SHIT HIT THE FAN: {e}")
finally:
    conn.close()