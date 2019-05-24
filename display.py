import pygame
import pygame.locals

movs=(pygame.K_ESCAPE, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_SPACE, pygame.K_q)

def get_textures(filename):
    m = pygame.image.load("textures/" + filename + ".png")
    mw, mh = m.get_size()
    textures = []
    for i in range(0, mh, 32):
        for j in range(0, mw, 32):
            textures.append(m.subsurface(j, i, 32, 32))
    return textures

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((672, 672))
    screen.fill((0,0,0))
    clock = pygame.time.Clock() 
    playin=True
    while playin:
        pygame.display.flip()
        clock.tick(15)
        for e in pygame.event.get():
            if e.type == pygame.locals.QUIT:
                playin = False
        pr = pygame.key.get_pressed()
        for k in (ke for ke in movs if pr[ke]):
                print(k)
        
