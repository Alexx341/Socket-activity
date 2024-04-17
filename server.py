import socket
from  _thread import *

server = "192.168.100.18"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)
print("Serwer stoi, czeka na polaczenie")

def read_pos(pos):
    pos = pos.split(",")
    return int(pos[0]), int(pos[1])

def make_pos(data):
    return str(data[0]) + "," + str(data[1])

pos = [(0,0),(100,100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
    
        data = read_pos(conn.recv(2048).decode())
        pos[player] = data

        if not data:
            print("Koniec polaczenia")
            break
        else:
            if player == 1:
                reply = pos[0]
            else:
                reply = pos[1]
            print("Received: ", data)
            print("Sending ", reply)
            
            conn.sendall(str.encode(make_pos(reply)))
    print("Polaczenie utracone")
    conn.close()

PlayerCount = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn, PlayerCount))
    PlayerCount += 1
