from math import cos,sin,pi
class Etrx:
    def __init__(self,m=[]):
        self.m=list(m)
    def p(self,*p):
        self.m+=[*p,1]
        return self
    def e(self,s,f):
        self.m+=[*s,1,*f,1]
        return self
    def __str__(self):
        return "\n".join(" ".join("%4.2f"%i for i in self.m[j::4]) for j in range(4))+"\n"
    def x(self,m):
        return Etrx([sum(float(m[i%4+k*4])*self.m[i-(i%4)+k]for k in range(4))for i in range(len(self.m))])
    def idm(self):
        return Etrx([1 if i==j else 0 for i in range(4)for j in range(4)])
    def rot(self,xyz,a):
        return self.x({"x":(1,0,0,0,0,cos(a/180*pi),sin(a/180*pi),0,0,sin(a/-180*pi),cos(a/180*pi),0,0,0,0,1),"y":(cos(a/180*pi),0,sin(a/-180*pi),0,0,1,0,0,sin(a/180*pi),0,cos(a/180*pi),0,0,0,0,1),"z":(cos(a/180*pi),sin(a/180*pi),0,0,sin(a/-180*pi),cos(a/180*pi),0,0,0,0,1,0,0,0,0,1)}[xyz])
    def mov(self,x,y,z):
        return self.x((1,0,0,0,0,1,0,0,0,0,1,0,x,y,z,1))
    def scl(self,v):
        return self.x((v,0,0,0,0,v,0,0,0,0,v,0,0,0,0,1))
    def scla(self,x,y,z):
        return self.x((x,0,0,0,0,y,0,0,0,0,z,0,0,0,0,1))
    def edgs(self):
        return[(tuple(self.m[i+j]for j in(0,1,2)),tuple(self.m[i+j]for j in(4,5,6)))for i in range(0,len(self.m),8)]
    ########self.c,self.hb,self.t,self.bfc,self.nermal,self.dtp,self.crs,self.nilrecurring,self.collapsethelightintoearth,self.limelight=(lambda x,y,z,r:[[self.e(*[[x+r*cos((t+d)/mx*2*pi),y+r*sin((t+d)/mx*2*pi),z]for d in(0,1)])for t in range(round(mx))]for mx in[40]]),(lambda xyxy,m:[[self.e(*[[(lambda a,t:sum(pow(t,3-i)*a[i]for i in range(4)))(Etrx([xyxy[2*i+k]for i in range(4)]).x(m).m,(h+d)/mx)for k in(0,1)]+[0]for d in(0,1)])for h in range(mx)]for mx in[20]]),(lambda p,b,d:[self.m.append(i)for i in(*p,1,*b,1,*d,1)]),(lambda i,lk:self.dtp(lk,self.nermal(i))),(lambda i:self.nilrecurring(self.crs(*[[self.m[i+j+k]-self.m[i+j]for j in(0,1,2)]for k in(4,8)]))),(lambda m,pth:sum(m[i]*pth[i]for i in range(len(pth)))),(lambda p,vi:(p[1]*vi[2]-p[2]*vi[1],p[2]*vi[0]-p[0]*vi[2],p[0]*vi[1]-p[1]*vi[0])),(lambda x:[[i/f for i in x]for f in[sqrt(self.dtp(x,x))]][0]if self.dtp(x,x)else[0]*3),(lambda i,l,u:[sum(e*pow(256,i)for i,e in enumerate([round(min(255,l[0][c]*u['a'][c]+sum([(u['d'][c]*max(0,self.dtp(z,Z))+u['s'][c]*pow(max(0,2*z[2]*self.dtp(Z,z)-Z[2]),4))*k['l'][c]for Z in[self.nilrecurring(k['v'])]][0]for k in l[1:])))for c in(2,1,0)]))for z in[self.nermal(i)]][0]),(lambda u=[1,1,1]:sum(pow(256,i)*round(255*u[2-i])for i in(0,1,2)))
