import pygame
import pygame.locals
from matrix import Etrx

movs=(pygame.K_ESCAPE, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_SPACE, pygame.K_q)

def get_textures(filename):
    m = pygame.image.load("textures/" + filename + ".png")
    mw, mh = m.get_size()
    textures = []
    for i in range(0, mh, 32):
        for j in range(0, mw, 32):
            textures.append(m.subsurface(j, i, 32, 32))
    return textures

def render_axes(s,axis,ry,rx):
    m=axis.rot('y',ry).rot('x',rx).mov(90,90,0).scl(3)
    for i in range(0,len(m.m),8):
        pygame.draw.line(s,(255,255,255),(m.m[i],m.m[i+1]),(m.m[i+4],m.m[i+5]),1)
if __name__ == '__main__':
    axis=Etrx()
    axis.e((-50,50,-50),(-50,50,50))
    axis.e((-50,-50,-50),(-50,50,-50))
    axis.e((-50,50,-50),(50,50,-50))
    pygame.init()
    screen = pygame.display.set_mode((672, 672))
    screen.fill((0,0,0))
    clock = pygame.time.Clock()
    playin=True
    ry=0
    rx=0
    m1 = False
    while playin:
        screen.fill((0,0,0))
        render_axes(screen,axis,ry,rx)
        pygame.display.flip()
        clock.tick(15)
        UI = UserInterface()
        UI.draw()
        for e in pygame.event.get():
            if e.type == pygame.locals.QUIT:
                playin = False
        if(pygame.mouse.get_pressed()[0]):
            dryrx=pygame.mouse.get_rel()
            ry+=dryrx[0]
            rx+=dryrx[1]
        else:
            pygame.mouse.get_rel()
        pr = pygame.key.get_pressed()
        for k in (ke for ke in movs if pr[ke]):
                print(k)
