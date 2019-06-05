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
    m=axis.scla(1,-1,1).rot('y',ry).rot('x',rx).mov(90,90,0).scl(3)
    for i in range(0,len(m.m),8):
        pygame.draw.line(s,clr,(m.m[i],m.m[i+1]),(m.m[i+4],m.m[i+5]),1)

        
def render_arrows(s,axia,ry,rx,clr=(255,255,255)):
    m=axia.scla(1,-1,1).rot('y',ry).rot('x',rx).mov(90,90,0).scl(3)
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
    if(b[0]>e[0]):
        ry+=180
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
    return[I*i/dtp(r,r)for i in crspr]

def wire(p,w,rndrwrsgmr):
    b=[0,0,0]
    for i in range(100):
        rndrwrsgmr.e([w[1][j]+(i/100)*(w[2][j]-w[1][j])for j in(0,1,2)],[w[1][j]+(i+1)/100*(w[2][j]-w[1][j])for j in(0,1,2)])
        deeb=db(w[0],[w[1][j]+(i/100)*(w[2][j]-w[1][j])for j in(0,1,2)],[w[1][j]+(i+1)/100*(w[2][j]-w[1][j])for j in(0,1,2)],p)
        b=[b[j]+deeb[j]for j in(0,1,2)]
    return b
def sol(p,s,rndrwrsgmr):
    pass

def tyl(p,t,rndrwrsgmr):
    pass

def bf(wr,sl,tl):
    bis=Etrx()
    bia=Etrx()
    rndrwrsgmr=Etrx()
    for x in range(-45,50,18):
        for y in range(-45,50,18):
            for z in range(-45,50,18):
                bd=[wire((x,y,z),w,rndrwrsgmr)for w in wr]
                bw=[sum(e[j]for e in bd)for j in(0,1,2)]

                bd=[sol((x,y,z),w,rndrwrsgmr)for w in sl]
                bs=[sum(e[j]for e in bd)for j in(0,1,2)]

                bd=[tyl((x,y,z),w,rndrwrsgmr)for w in tl]
                bt=[sum(e[j]for e in bd)for j in(0,1,2)]

                bv=(x,y,z),[(x,y,z)[i]+bw[i]+bs[i]+bt[i]for i in(0,1,2)]
                bis.e(*bv)
                get_arrow_head(*bv,bia,4)
    return(bis,bia,rndrwrsgmr)
if __name__ == '__main__':
    axis=Etrx()
    
    axis.e((-50,0,0),(50,0,0))
    axis.e((0,-50,0),(0,50,0))
    axis.e((0,0,-50),(0,0,50))

    axia=Etrx()
    for e in axis.edgs():
        get_arrow_head(*e,axia,10)
    pygame.init()
    screen = pygame.display.set_mode((672, 672))
    screen.fill((0,0,0))
    clock = pygame.time.Clock()
    playin=True
    ry=-15
    rx=5
    m1 = False
    UI = UserInterface()

    wr=[[100,[0,0,-50],[0,0,50]]]
    sl=[]
    tl=[]
    bis,bia,rndrwrsgmr=bf(wr,sl,tl)
    while playin:
        screen.fill((0,0,0))
        render_axes(screen,axis,ry,rx)
        render_arrows(screen,axia,ry,rx)

        render_axes(screen,rndrwrsgmr,ry,rx,(0,255,0))

        render_axes(screen,bis,ry,rx,(255,0,0))
        render_arrows(screen,bia,ry,rx,(255,0,0))
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
            rx = -50 if rx < -50 else (50 if rx > 50 else rx)
        else:
            pygame.mouse.get_rel()
        pr = pygame.key.get_pressed()
        for k in (ke for ke in movs if pr[ke]):
                print(k)
