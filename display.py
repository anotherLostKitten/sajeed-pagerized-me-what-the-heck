from math import atan2,sqrt,pi,cos,sin,floor

import pygame
import pygame.locals

from matrix import Etrx
from interface import UserInterface, TextBox

movs=(pygame.K_ESCAPE, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_SPACE, pygame.K_q,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_0,pygame.K_RETURN)

def get_textures(filename):
    m = pygame.image.load("textures/" + filename + ".png")
    mw, mh = m.get_size()
    textures = []
    for i in range(0, mh, 32):
        for j in range(0, mw, 32):
            textures.append(m.subsurface(j, i, 32, 32))
    return textures

def render_axes(s,axis,ry,rx,clr=(255,255,255)):
    m=axis.x(axis.ident().scla(1,-1,1).rot('y',ry).rot('x',rx).mov(90,90,0).scl(3).m)
    for i in range(0,len(m.m),8):
        pygame.draw.line(s,clr,(m.m[i],m.m[i+1]),(m.m[i+4],m.m[i+5]),1)

        
def render_arrows(s,axia,ry,rx,clr=(255,255,255)):
    m=axia.x(axia.ident().scla(1,-1,1).rot('y',ry).rot('x',rx).mov(90,90,0).scl(3).m)
    for i in range(0,len(m.m),28):
        for j in range(0,24,4):
            pygame.draw.polygon(s,clr,((m.m[i],m.m[i+1]),(m.m[i+j],m.m[i+j+1]),(m.m[i+(j+4)%28],m.m[i+(j+5)%28]) ))
            pygame.draw.polygon(s,clr,((m.m[i],m.m[i+1]),(m.m[i+24],m.m[i+25]),(m.m[i+4],m.m[i+5]) ))
def render_arrows_color(s,axia,axis,ry,rx,clr1,clr2,vlenmax):
    m=axia.x(axia.ident().scla(1,-1,1).rot('y',ry).rot('x',rx).mov(90,90,0).scl(3).m)
    for i in range(0,len(m.m),28):
        vleni=vlen([bis.m[2*i//7+j]-bis.m[2*i//7+j+4]for j in(0,1,2)])
        clr=[round(clr1[j]+vleni/vlenmax*(clr2[j]-clr1[j]))for j in(0,1,2)]
        for j in range(0,24,4):
            pygame.draw.polygon(s,clr,((m.m[i],m.m[i+1]),(m.m[i+j],m.m[i+j+1]),(m.m[i+(j+4)%28],m.m[i+(j+5)%28]) ))
        pygame.draw.polygon(s,clr,((m.m[i],m.m[i+1]),(m.m[i+24],m.m[i+25]),(m.m[i+4],m.m[i+5]) ))
        
def get_arrow_head(b,e,pogm,scl,move=True):
    d=[e[i]-b[i]for i in(0,1,2)]
    if vlen(d)<0.000001:
        return
    a=Etrx()
    a.p(0,0,0)
    a.p(-scl,0,-scl/4)
    a.p(-scl,-scl*sqrt(3)/8,-scl/8)
    a.p(-scl,-scl*sqrt(3)/8,scl/8)
    a.p(-scl,0,scl/4)
    a.p(-scl,scl*sqrt(3)/8,scl/8)
    a.p(-scl,scl*sqrt(3)/8,-scl/8)
    rz=atan2(d[1],d[0])*180/pi
    ry=atan2(d[2],d[0])*-180/pi
    if(b[0]>e[0]):
        ry+=180
    pogm.m+=a.rot('z',rz).rot('y',ry).mov(*e).m if move else a.rot('z',rz).rot('y',ry).mov(*b).m

def dtp(u,v):
    return sum(u[i]*v[i] for i in range(len(u)))
def crs(p,vi):
    return(p[1]*vi[2]-p[2]*vi[1],p[2]*vi[0]-p[0]*vi[2],p[0]*vi[1]-p[1]*vi[0])
def nrml(x):
    f=vlen(x)
    return[i/f for i in x]if f else[0]*3
def vlen(x):
    return sqrt(dtp(x,x))
def db(I,b,e,p):
    l=[e[i]-b[i]for i in(0,1,2)]
    r=[p[i]-(e[i]+b[i])/2 for i in(0,1,2)]
    crspr=crs(l,nrml(r))
    return[I*i/dtp(r,r)for i in crspr]

def wire(p,w,rndrwrsgmr):
    b=[0,0,0]
    k=100
    for i in range(k):
        deeb=db(w[0],[w[1][j]+(i/k)*(w[2][j]-w[1][j])for j in(0,1,2)],[w[1][j]+(i+1)/k*(w[2][j]-w[1][j])for j in(0,1,2)],p)
        b=[b[j]+deeb[j]for j in(0,1,2)]
    rndrwrsgmr.e([w[1][j]for j in(0,1,2)],[w[2][j]for j in(0,1,2)])
    return b
def sol(p,s,rndrwrsgmr): #[current,start,end,num_turns,radius]
    b=[0,0,0]
    k=round(20*s[3])
    for i in range(k):
        a=Etrx()
        a.p(0,s[4]*cos(2*pi*i/k*s[3]),s[4]*sin(2*pi*i/k*s[3]))
        d=[s[2][i]-s[1][i]for i in(0,1,2)]
        a.p(0,s[4]*cos(2*pi*(i+1)/k*s[3]),s[4]*sin(2*pi*(i+1)/k*s[3]))
        rz=atan2(d[1],d[0])*180/pi
        ry=atan2(d[2],d[0])*-180/pi
        if(s[1][0]>s[2][0]):
            ry+=180
        pts=a.rot('z',rz).rot('y',ry).mov(*[s[1][j]+(i/k)*(s[2][j]-s[1][j])for j in(0,1,2)])
        pts2=pts.mov(*[(s[2][j]-s[1][j])/k for j in(0,1,2)])
        deeb=db(s[0],pts.m[0:3],pts2.m[4:7],p)
        b=[b[j]+deeb[j]for j in(0,1,2)]
    k=round(s[3]*(s[4]/13+4))
    for i in range(k):
        a=Etrx()
        a.p(0,s[4]*cos(2*pi*i/k*s[3]),s[4]*sin(2*pi*i/k*s[3]))
        d=[s[2][i]-s[1][i]for i in(0,1,2)]
        a.p(0,s[4]*cos(2*pi*(i+1)/k*s[3]),s[4]*sin(2*pi*(i+1)/k*s[3]))
        rz=atan2(d[1],d[0])*180/pi
        ry=atan2(d[2],d[0])*-180/pi
        if(s[1][0]>s[2][0]):
            ry+=180
        pts=a.rot('z',rz).rot('y',ry).mov(*[s[1][j]+(i/k)*(s[2][j]-s[1][j])for j in(0,1,2)])
        pts2=pts.mov(*[(s[2][j]-s[1][j])/k for j in(0,1,2)])
        rndrwrsgmr.e(pts.m[0:3],pts2.m[4:7])
    return b

def tyl(p,t,rndrwrsgmr):
    pass

def bf(things):
    wr = [i[1]for i in things if i[0]=='wire']
    sl = [i[1]for i in things if i[0]=='sol']
    tl = [i[1]for i in things if i[0]=='tyl']
    bis=Etrx()
    bia=Etrx()
    rndrwrsgmr=Etrx()
    vlenmax=0
    for x in range(-45,50,18):
        for y in range(-45,50,18):
            for z in range(-45,50,18):
                bd=[wire((x,y,z),w,rndrwrsgmr)for w in wr]
                bw=[sum(e[j]for e in bd)for j in(0,1,2)]

                bd=[sol((x,y,z),w,rndrwrsgmr)for w in sl]
                bs=[sum(e[j]for e in bd)for j in(0,1,2)]

                bd=[tyl((x,y,z),w,rndrwrsgmr)for w in tl]
                bt=[sum(e[j]for e in bd)for j in(0,1,2)]

                bbb=[bw[i]+bs[i]+bt[i]for i in(0,1,2)]
                if vlenmax<vlen(bbb):
                    vlenmax=vlen(bbb)
                bv=(x,y,z),[(x,y,z)[i]+bbb[i]for i in(0,1,2)]
                bis.e(*bv)
                get_arrow_head(*bv,bia,4,False)
    return(bis,bia,rndrwrsgmr,vlenmax)

def localbf(things,x, y, z):
    wr = [i[1]for i in things if i[0]=='wire']
    sl = [i[1]for i in things if i[0]=='sol']
    tl = [i[1]for i in things if i[0]=='tyl']
    bis=Etrx()
    bia=Etrx()
    rndrwrsgmr=Etrx()
    vlenmax=0
    bd=[wire((x,y,z),w,rndrwrsgmr)for w in wr]
    bw=[sum(e[j]for e in bd)for j in(0,1,2)]

    bd=[sol((x,y,z),w,rndrwrsgmr)for w in sl]
    bs=[sum(e[j]for e in bd)for j in(0,1,2)]

    bd=[tyl((x,y,z),w,rndrwrsgmr)for w in tl]
    bt=[sum(e[j]for e in bd)for j in(0,1,2)]

    bbb=[bw[i]+bs[i]+bt[i]for i in(0,1,2)]
    return vlen(bbb)

def turnToClicker(minX, maxX, minY, maxY):#, clicked):
    if (minX <= pygame.mouse.get_pos()[0] <= maxX and minY <= pygame.mouse.get_pos()[1] <= maxY):
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        #if (pygame.mouse.get_pressed()[0] and not clicked):
            #clicked = True
        return True
    else:
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        return False

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
    ry=105
    rx=5
    m1 = False

    things=[['wire',[100,[0,0,-50],[0,0,50]]]] #[current,start,end] '''[100,[0,0,-50],[0,0,50]]'''

    UI = UserInterface(screen, localbf(things,5, 5, 5), 5, 5, 5)
    textBoxes = UI.returnTextBoxes()
    dragging = False
    
    bis,bia,rndrwrsgmr,vlenmax=bf(things)
    screen.fill((0,0,0))
    render_axes(screen,axis,ry,rx)
    render_arrows(screen,axia,ry,rx)

    render_axes(screen,rndrwrsgmr,ry,rx,(0,255,0))

    render_arrows_color(screen,bia,bis,ry,rx,(255,0,0),(0,0,255),vlenmax)
    print(vlenmax)
    typing = False
    typeClicked = False
    while playin:
        
        if (dragging):
            screen.fill((0,0,0))
            render_axes(screen,axis,ry,rx)
            render_arrows(screen,axia,ry,rx)
        else:
            render_arrows_color(screen,bia,bis,ry,rx,(255,0,0),(0,0,255),vlenmax)
            render_axes(screen,rndrwrsgmr,ry,rx,(0,255,0))

        UI.draw()
        pygame.display.flip()
        clock.tick(15)
        iasdf=False
        for e in pygame.event.get():
            if e.type == pygame.locals.QUIT:
                playin = False
            elif e.type == pygame.locals.KEYDOWN:
                #if (e.key == pygame.K_RETURN):
                    #typeClicked = False
                #print(chr(e.key))

                UI.key(chr(e.key))
                iasdf=True
        if iasdf:
            UI.setlocal(localbf(things,*UI.getlocal()))
        if(pygame.mouse.get_pressed()[0]):
            #value = value[0: len(value) - 1: 1]
            if (pygame.mouse.get_pos()[1] <= 509):
                if(clicked):
                    dragging = True
            elif(clicked):
                clicked = False
            #if (typeClicked):
                #typeClicked = False
                new_thing=UI.click(*pygame.mouse.get_pos())
                if new_thing!=None:
                    if new_thing[0]in("wire","sol","tyl"):
                        things.append(new_thing)
                    elif new_thing[0]=="del" and len(things)>0:
                        things.pop()
                    bis,bia,rndrwrsgmr,vlenmax=bf(things)
                    screen.fill((0,0,0))
                    render_axes(screen,axis,ry,rx)
                    render_arrows(screen,axia,ry,rx)

                    render_axes(screen,rndrwrsgmr,ry,rx,(0,255,0))
                    
                    render_arrows_color(screen,bia,bis,ry,rx,(255,0,0),(0,0,255),vlenmax)
        else:
            clicked = True
            dragging = False
            pygame.mouse.get_rel()
            
        if(dragging):
            dryrx=pygame.mouse.get_rel()
            ry+=-dryrx[0]
            rx+=dryrx[1]
            rx = -50 if rx < -50 else (50 if rx > 50 else rx)
        else:
            nextOne = turnToClicker(615, 645, 538, 548)
            if (not nextOne):
                nextOne = turnToClicker(615, 645, 586, 606) or nextOne
            if (not nextOne):
                nextOne = turnToClicker(620, 640, 620, 640) or nextOne
            i = 0
            if (not nextOne):
                while i < len(textBoxes):
                    nextOne = turnToClicker(len(textBoxes[i].label_text)*3.6 + textBoxes[i].centerX + 4, len(textBoxes[i].label_text)*3.6 + textBoxes[i].centerX + 34, textBoxes[i].centerY - 7, textBoxes[i].centerY + 7) or nextOne
                    if (not nextOne):
                        i += 1
                    else:
                        i = len(textBoxes)
        #if (typeClicked):
            #value = "7"
        #print(value)
        pr = pygame.key.get_pressed()
