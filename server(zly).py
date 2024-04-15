# Python Server
import socket
import threading 

IP = socket.gethostbyname(socket.gethostname())
print(IP)
PORT = 5566
ADDR = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "/disc"
connected_clients = []
def handle_client(conn, addr):

    connected_clients.append(conn)
    if threading.active_count() - 1 == 1:
        msg = "You're the first one connected, wait for the second player"
        conn.send(msg.encode(FORMAT))    

    
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    name1 = ""
    name2 = ""
    while connected:
        if threading.active_count() - 1 != 1:
            msg1 = "both players connected"
            conn.send(msg1.encode(FORMAT))    
            if name1 == "":
                Namemsg = "Please input your name: "
                conn.send(Namemsg.encode(FORMAT))
                name1 = conn.recv(SIZE).decode(FORMAT)
                Namemsg = f"hello {name1}"
                conn.send(Namemsg.encode(FORMAT))
        if msg == DISCONNECT_MSG:
            connected = False
        

    conn.close()
    connected_clients.remove(conn)
def main():
    print("[STARTING] server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(2)
    print(f"[LISTENING] server is listening on {IP}:{PORT}")

    while True:
        if threading.active_count() - 1<2:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn,addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")



if __name__ == "__main__":
    main()

