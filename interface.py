import pygame
from math import pi,sin,cos
class UserInterface:
    def __init__(self, surf):
        self.sur = surf

    def draw(self):
        border = pygame.Rect(0, 500, 672, 172)
        pygame.draw.rect(self.sur, (200, 200, 200), border, 0)
        ui = pygame.Rect(10, 510, 652, 152)
        pygame.draw.rect(self.sur, (230, 230, 230), ui, 0)
        pygame.draw.line(self.sur, (0, 0, 0), (615, 543), (645, 543), 3)
        self.solenoid(620, 586)
        #self.toroid(620, 629)
        myText = pygame.font.Font('ebrima.ttf', 12)
        myB = myText.render('42.16', True, (0, 0, 0))
        bRect = myB.get_rect()
        bRect.center = (40, 527.5)
        letterB = myText.render('B:', True, (0, 0, 0))
        letterRect = letterB.get_rect()
        letterRect.center = (17, 527.5)
        pygame.draw.rect(self.sur, (0, 0, 0), pygame.Rect(24, 519, 32, 17), 0)
        pygame.draw.rect(self.sur, (255, 255, 255), pygame.Rect(25, 520, 30, 15), 0)
        self.sur.blit(myB, bRect)
        self.sur.blit(letterB, letterRect)
        self.text(myText, "Current:", 498, 516.5)
        self.text(myText, "Start X:", 500, 532.5)
        self.text(myText, "Start Y:", 500, 544.5)
        self.text(myText, "Start Z:", 500, 556.5)
        self.text(myText, "End X:", 502, 574.5)
        self.text(myText, "End Y:", 502, 592.5)
        self.text(myText, "End Z:", 502, 604.5)
        self.text(myText, "Loop Radius:", 485, 622.5)
        self.text(myText, "Number of Turns:", 473, 634.5)
        self.text(myText, "Major Radius:", 483, 652.5)

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

    def text(self, font, text, centerX, centerY):
        letter = font.render(text, True, (0, 0, 0))
        letterRect = letter.get_rect()
        letterRect.center = (centerX, centerY)
        self.sur.blit(letter, letterRect)