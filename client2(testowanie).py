import pygame
from network import Network
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(this, x, y, width, height, color):
        this.x = x
        this.y = y
        this.width = width
        this.height = height
        this.color = color
        this.rect = (x,y,width,height)
        this.vel = 3

    def draw(this,win):
        pygame.draw.rect(win, this.color, this.rect)

    def move(this):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            this.x -= this.vel

        if keys[pygame.K_RIGHT]:
            this.x += this.vel

        if keys[pygame.K_UP]:
            this.y -= this.vel

        if keys[pygame.K_DOWN]:
            this.y += this.vel
        this.update()
    def update(this):
        this.rect = (this.x, this.y, this.width, this.height)
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])
def make_pos(pos):
    return str(pos[0]) + "," + str(pos[1])

def GraUpdate(win, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,0,0))
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        GraUpdate(win, p, p2)
main()
