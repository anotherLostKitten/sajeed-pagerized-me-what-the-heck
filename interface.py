import pygame
class UserInterface:
    def draw(self, sur):
        border = pygame.Rect(0, 500, 672, 172)
        pygame.draw.rect(sur, (200, 200, 200), border, 0)
        ui = pygame.Rect(10, 510, 652, 152)
        pygame.draw.rect(sur, (230, 230, 230), ui, 0)