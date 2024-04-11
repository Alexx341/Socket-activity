# Python Client
import socket
IP = "192.168.100.18"
PORT = 5566
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "/disc"
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] client connected to server at {IP}:{PORT}")
    connected = True
    while connected:
        msg = client.recv(SIZE).decode(FORMAT)
        if msg == "You're the first one connected, wait for the second player":
            print(f"[SERVER] {msg}")
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")
        else:
            print(f"[SERVER] {msg}")
        
        
        msg = input("> ")
        if msg == DISCONNECT_MSG:
            connected = False
        else:
            client.send(msg.encode(FORMAT))



if __name__ == "__main__":
    main()