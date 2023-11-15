import socket
from _thread import *
import sys


#Local IPv4 address
#THIS IS HARDCODED RN AND WILL NEED TO BE CHANGED TO WORK 
SERVER = "192.168.210.227"
PORT = 5050
#increase this to increase number of bits sent
BITMOD = 1

#Create our socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
except socket.error as e:
    str(e)
    
#opens up the port for communication
#to allow for unlimited connections get rid of the 2    
s.listen()
print("Waiting for a connection, server started")

#This can run in the background while other things r going, cuz threads n stuff
def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            #Number in function is number of bits we are trying to receive
            data = conn.recv(2048*BITMOD)
            #Decode the information so we can read it   
            reply = data.decode("utf-8")
            
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            #Ecode our reply so it can be sent
            conn.sendall(str.encode(reply))
        except:
            print("THREADED SHIT HIT THE FAN")
            break
    print("Lost connection")
    conn.close()
        

#Continuously look for connection
while True:
    #Accepts any incoming connection
    #conn is stored in conn, what is connected
    #addr is the ip address
    conn, addr = s.accept()
    print("Connected to: ", addr)
    
    start_new_thread(threaded_client, (conn,))