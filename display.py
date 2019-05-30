from math import atan2,sqrt,pi

import pygame
import pygame.locals

from matrix import Etrx
from interface import UserInterface

movs=(pygame.K_ESCAPE, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_SPACE, pygame.K_q)

def get_textures(filename):
    m = pygame.image.load("textures/" + filename + ".png")
    mw, mh = m.get_size()
    textures = []
    for i in range(0, mh, 32):
        for j in range(0, mw, 32):
            textures.append(m.subsurface(j, i, 32, 32))
    return textures

def render_axes(s,axis,ry,rx,clr=(255,255,255)):
    m=axis.rot('y',ry).rot('x',rx).mov(90,90,0).scl(3)
    for i in range(0,len(m.m),8):
        pygame.draw.line(s,clr,(m.m[i],m.m[i+1]),(m.m[i+4],m.m[i+5]),1)

        
def render_arrows(s,axia,ry,rx,clr=(255,255,255)):
    m=axia.rot('y',ry).rot('x',rx).mov(90,90,0).scl(3)
    for i in range(0,len(m.m),28):
        for j in range(4,28,4):
            pygame.draw.polygon(s,clr,((m.m[i],m.m[i+1]),(m.m[i+j],m.m[i+j+1]),(m.m[i+(j+4)%28],m.m[i+(j+5)%28]) ))
        pygame.draw.polygon(s,clr,[(m.m[i+j],m.m[i+j+1])for j in range(4,28,4)])

def get_arrow_head(b,e,pogm,scl):
    a=Etrx()
    a.p(0,0,0)
    a.p(-scl,0,-scl/4)
    a.p(-scl,-scl*sqrt(3)/8,-scl/8)
    a.p(-scl,-scl*sqrt(3)/8,scl/8)
    a.p(-scl,0,scl/4)
    a.p(-scl,scl*sqrt(3)/8,scl/8)
    a.p(-scl,scl*sqrt(3)/8,-scl/8)
    d=[e[i]-b[i]for i in(0,1,2)]
    rz=atan2(d[1],d[0])*180/pi
    ry=atan2(d[2],d[0])*-180/pi
    pogm.m+=a.rot('z',rz).rot('y',ry).mov(*e).m
def dtp(u,v):
    return sum(u[i]*v[i] for i in range(len(u)))
def crs(p,vi):
    return(p[1]*vi[2]-p[2]*vi[1],p[2]*vi[0]-p[0]*vi[2],p[0]*vi[1]-p[1]*vi[0])
def nrml(x):
    f=sqrt(dtp(x,x))
    return[i/f for i in x]if f else[0]*3

def db(I,b,e,p):
    l=[e[i]-b[i]for i in(0,1,2)]
    r=[p[i]-(e[i]+b[i])/2 for i in(0,1,2)]
    crspr=crs(l,nrml(r))
    return[I*i/self.dtp(r,r)for i in crspr]
def b(p,w,s,t):
    dbs=[db()for i in w]


if __name__ == '__main__':
    axis=Etrx()
    axis.e((-50,50,-50),(-50,50,50))
    axis.e((-50,50,-50),(-50,-50,-50))
    axis.e((-50,50,-50),(50,50,-50))
    axia=Etrx()
    for e in axis.edgs():
        get_arrow_head(*e,axia,10)
    pygame.init()
    screen = pygame.display.set_mode((672, 672))
    screen.fill((0,0,0))
    clock = pygame.time.Clock()
    playin=True
    ry=0
    rx=0
    m1 = False
    UI = UserInterface()
    while playin:
        screen.fill((0,0,0))
        render_axes(screen,axis,ry,rx)
        render_arrows(screen,axia,ry,rx)
        UI.draw(screen)
        pygame.display.flip()
        clock.tick(15)
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
