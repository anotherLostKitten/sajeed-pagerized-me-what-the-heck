import pygame
from math import pi,sin,cos

class TextBox:
    def __init__(self, cx, cy, tex, surface, font):
        self.centerX = cx
        self.centerY = cy
        self.label_text = tex
        self.value_text = ""
        self.sur = surface
        self.font = font
        self.active = False
        
    def draw(self):
        letter = self.font.render(self.label_text, True, (0, 0, 0))
        letterRect = letter.get_rect()
        letterRect.center = (self.centerX, self.centerY)
        self.sur.blit(letter, letterRect)
        
        if(self.active):
            pygame.draw.rect(self.sur, (0, 0, 0), pygame.Rect(len(self.label_text)*3.6 + self.centerX + 4, self.centerY - 7, 32, 14), 0)
        pygame.draw.rect(self.sur, (255, 255, 255), pygame.Rect(len(self.label_text)*3.6 + self.centerX + 5, self.centerY - 6, 30, 12), 0)
    def key(self,key):
        self.value_text+=key
    def clicked(self,x,y):
        self.active = len(self.label_text)*3.6 +self.centerX-12 < x < len(self.label_text)*3.6 +self.centerX+20 and self.centerY-6 <  y < self.centerY+6
        return self.active
class UserInterface:
    def __init__(self, surf):
        self.sur = surf
        self.font = pygame.font.Font('cour.ttf', 12)

        self.texts=[TextBox(17,590,"X:", self.sur, self.font),
                    TextBox(17, 620,"Y:",self.sur, self.font),
                    TextBox(17, 650,"Z:",self.sur, self.font),
                    TextBox(498, 519.5,"Current:",self.sur, self.font),
                    TextBox(498, 537.5,"Start X:",self.sur, self.font),
                    TextBox(498, 549.5,"Start Y:",self.sur, self.font),
                    TextBox(498, 562.5,"Start Z:",self.sur, self.font),
                    TextBox(505, 581.5,"End X:",self.sur, self.font),
                    TextBox(505, 594.5,"End Y:",self.sur, self.font),
                    TextBox(505, 607.5,"End Z:",self.sur, self.font),
                    TextBox(484, 624,"Loop Radius:",self.sur, self.font),
                    TextBox(470,637,"Number of Turns:",self.sur, self.font),
                    TextBox(480, 655.5,"Major Radius:",self.sur, self.font)]
        self.active_text = -1
        self.mode = []
    def draw(self):
        border = pygame.Rect(0, 500, 672, 172)
        pygame.draw.rect(self.sur, (200, 200, 200), border, 0)
        ui = pygame.Rect(10, 510, 652, 152)
        pygame.draw.rect(self.sur, (230, 230, 230), ui, 0)
        pygame.draw.line(self.sur, (0, 0, 0), (615, 543), (645, 543), 3)
        self.solenoid(620, 586)
        #self.toroid(620, 629)
        myB = self.font.render('42.16', True, (0, 0, 0))
        bRect = myB.get_rect()
        bRect.center = (40, 527.5)
        letterB = self.font.render('B:', True, (0, 0, 0))
        letterRect = letterB.get_rect()
        letterRect.center = (17, 527.5)
        pygame.draw.rect(self.sur, (0, 0, 0), pygame.Rect(24, 519, 32, 17), 0)
        pygame.draw.rect(self.sur, (255, 255, 255), pygame.Rect(25, 520, 30, 15), 0)
        self.sur.blit(myB, bRect)
        self.sur.blit(letterB, letterRect)
        for i in self.texts:
            i.draw()
    def key(self,key):
        if active_text != -1:
            if key in"0123456789.":
                self.texts[self.active_text].key(key)
            elif key=="":
                pass
    def click(self,x,y):
        ts=[i for i in range(len(self.texts))if self.texts[i].clicked(x,y)]
        self.active_text=ts[0]if ts else-1
        print(self.active_text)
    def solenoid(self, startx, starty):
        pygame.draw.line(self.sur, (0, 0, 0), (startx - 5, starty + 10), (startx, starty + 10), 3)
        for i in range(3):
            container = pygame.Rect(startx + i * 4, starty, 10, 20)
            pygame.draw.arc(self.sur, (0, 0, 0), container, 3 * pi / 2, pi, 3)
            container2 = pygame.Rect(startx + i * 4 + 3, starty, 10, 20)
            pygame.draw.arc(self.sur, (0, 0, 0), container2, pi, 3 * pi / 2, 3)
        container = pygame.Rect(startx + 12, starty, 10, 20)
        pygame.draw.arc(self.sur, (0, 0, 0), container, 0, pi, 3)
        pygame.draw.line(self.sur, (0, 0, 0), (startx + 20, starty + 10), (startx + 25, starty + 10), 3)
    
    def toroid(self, startx, starty):
        for i in range(8):
            if i != 2 and i != 6:
                print (i)
                print(round(startx + 5 * cos(i * pi / 4)))
                print(round(starty + 5 * sin(i * pi / 4)))
                print(round(5 * cos(i * pi / 4)))
                container = pygame.Rect(round(startx + 5 * cos(i * pi / 4)), round(starty + 5 * sin(i * pi / 4)), round(5 * cos(i * pi / 4)), 5)
                pygame.draw.ellipse(self.sur, (0, 0, 0), container, 1)

#    def text(self, font, text, centerX, centerY):
#        letter = font.render(text, True, (0, 0, 0))
#        letterRect = letter.get_rect()
#        letterRect.center = (centerX, centerY)
#        self.sur.blit(letter, letterRect)
#        DaBox = TextBox(centerX, centerY, text, self.sur)
#        DaBox.draw()
