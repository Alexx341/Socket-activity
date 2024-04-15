import pygame
from network import Network
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self,win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel
            
        self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(win,player):

    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    startPos = n.getPos() 
    p = Player(50,50,100,100,(0,255,0))
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p)
main()
# Python Client
# import socket
# IP = "192.168.100.18"
# PORT = 5566
# ADDR = (IP,PORT)
# SIZE = 1024
# FORMAT = "utf-8"
# DISCONNECT_MSG = "/disc"
# def main():
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect(ADDR)
#     print(f"[CONNECTED] client connected to server at {IP}:{PORT}")
#     connected = True
#     while connected:
#         msg = client.recv(SIZE).decode(FORMAT)
#         if msg == "You're the first one connected, wait for the second player":
#             print(f"[SERVER] {msg}")
#             msg = client.recv(SIZE).decode(FORMAT)
#             print(f"[SERVER] {msg}")
#         else:
#             print(f"[SERVER] {msg}")
        
        
#         msg = input("> ")
#         if msg == DISCONNECT_MSG:
#             connected = False
#         else:
#             client.send(msg.encode(FORMAT))



# if __name__ == "__main__":
#     main()