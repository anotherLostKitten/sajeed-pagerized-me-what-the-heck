import pygame
from math import pi,sin,cos

class TextBox:
    def __init__(self, cx, cy, tex, box, surface, font):
        self.centerX = cx
        self.centerY = cy
        self.label_text = tex
        self.value_text = ""
        self.sur = surface
        self.boxText = str(box)
        self.font = font

    def draw(self):
        textHolder = pygame.Rect(len(self.text)*3.6 + self.centerX + 5, self.centerY - 6, 30, 12)
        pygame.draw.rect(self.sur, (0, 0, 0), pygame.Rect(len(self.text)*3.6 + self.centerX + 4, self.centerY - 7, 32, 14), 0)
        pygame.draw.rect(self.sur, (255, 255, 255), textHolder, 0)
        number = self.font.render(self.boxText, True, (0, 0, 0))
        numberRect = number.get_rect()
        numberRect.center = textHolder.center
        self.sur.blit(number, textHolder)

class UserInterface:
    def __init__(self, surf, field, px, py, pz):
        self.sur = surf
        self.f = "%4.2f" % field
        self.x = px
        self.y = py
        self.z = pz
        self.textBoxes = []

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
    def draw(self):
        border = pygame.Rect(0, 500, 672, 172)
        pygame.draw.rect(self.sur, (200, 200, 200), border, 0)
        ui = pygame.Rect(10, 510, 652, 152)
        pygame.draw.rect(self.sur, (230, 230, 230), ui, 0)
        pygame.draw.line(self.sur, (0, 0, 0), (615, 543), (645, 543), 3)
        self.solenoid(620, 586)
        #self.toroid(620, 629)
        myText = pygame.font.Font('cour.ttf', 12)
        myB = myText.render(str(self.f), True, (0, 0, 0))
        bRect = myB.get_rect()
        bRect.center = (41.5, 527.5)
        letterB = myText.render('B:', True, (0, 0, 0))
        letterRect = letterB.get_rect()
        letterRect.center = (17, 527.5)
        pygame.draw.rect(self.sur, (0, 0, 0), pygame.Rect(24, 518, 36, 17), 0)
        pygame.draw.rect(self.sur, (255, 255, 255), pygame.Rect(25, 519, 34, 15), 0)
        self.sur.blit(myB, bRect)
        self.sur.blit(letterB, letterRect)
        self.text(myText, "X:", self.x, 17, 590)
        self.text(myText, "Y:", self.y, 17, 620)
        self.text(myText, "Z:", self.z, 17, 650)
        self.text(myText, "Current:", "0", 498, 519.5)
        self.text(myText, "Start X:", "0", 498, 537.5)
        self.text(myText, "Start Y:", "0", 498, 549.5)
        self.text(myText, "Start Z:", "0", 498, 562.5)
        self.text(myText, "End X:", "0", 505, 581.5)
        self.text(myText, "End Y:", "0", 505, 594.5)
        self.text(myText, "End Z:", "0", 505, 607.5)
        self.text(myText, "Loop Radius:", "0", 483, 624)
        self.text(myText, "Number of Turns:", "0", 469, 637)
        self.text(myText, "Major Radius:", "0", 480, 655.5)

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

    def text(self, font, text, boxText, centerX, centerY):
        letter = font.render(text, True, (0, 0, 0))
        letterRect = letter.get_rect()
        letterRect.center = (centerX, centerY)
        self.sur.blit(letter, letterRect)
        DaBox = TextBox(centerX, centerY, text, boxText, self.sur, font)
        DaBox.draw()
        self.textBoxes += [DaBox]
    
    def returnTextBoxes(self):
        return self.textBoxes