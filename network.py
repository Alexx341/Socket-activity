import socket

class Network:
    def __init__(this):
        this.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        this.server = "192.168.100.18"
        this.port = 5555
        this.addr = (this.server, this.port)
        this.pos = this.connect()
    
    def getPos(this):
        return this.pos
    def connect(this):
            this.client.connect(this.addr)
            return this.client.recv(2048).decode()
    def send(this, data):
            this.client.send(str.encode(data))
            return this.client.recv(2048).decode()


