import pygame
from constants import WINDOW_HEIGHT, FONT_NAME

class Slider:
    def __init__(self, name, val, maxi, mini, pos):
        self._val = val
        self._maxi = maxi
        self._mini = mini
        self._xpos = pos #horizontal pos
        self._ypos = WINDOW_HEIGHT / 2 + 100;

        self.power = 2

        self._surf = pygame.surface.Surface((300, 100))
        self._is_hit = False

        font = pygame.font.SysFont(FONT_NAME, 24)
        self._txt_surf = font.render(name, 1, (0, 0, 0))
        self._txt_rect = self._txt_surf.get_rect(center=(150, 15))

        #Slider background
        self._surf.fill((255,255,255))
        pygame.draw.rect(self._surf, (0, 0, 0), [0, 40, 300, 10], 0)


        self._surf.blit(self._txt_surf, self._txt_rect)

        #Slider circle
        self._button_surf = pygame.surface.Surface((20, 40))
        self._button_surf.fill((1, 1, 1))
        self._button_surf.set_colorkey((1, 1, 1))

        pygame.draw.circle(self._button_surf, (0, 0, 0), (10, 30), 15, 0)
        #pygame.draw.circle(self._button_surf, (200, 100, 50), (10, 10), 4, 0)

    @property
    def is_hit(self):
        return self._is_hit

    @is_hit.setter
    def is_hit(self, state):
        self._is_hit = state

    @property
    def button_rect(self):
        return self._button_rect

    @property
    def val(self):
        return self._val


    def draw(self, screen: pygame.Surface):
        surf = self._surf.copy()


        pos = (10 + int((self._val - self._mini) / (self._maxi - self._mini) * 280), 33)
        self._button_rect = self._button_surf.get_rect(center = pos)
        surf.blit(self._button_surf, self._button_rect)
        self._button_rect.move_ip(self._xpos, self._ypos)

        screen.blit(surf, (self._xpos, self._ypos))

    def move(self):
        self.power = pow(2, int((pygame.mouse.get_pos()[0] - self._xpos) / 33))

        if self.power > 512:
            self.power = 512

        if self.power < 2:
            self.power = 2

        self._val = int((pygame.mouse.get_pos()[0] - self._xpos) / 280 * (self._maxi - self._mini) + self._mini)

        if self._val < self._mini:
            self._val = self._mini

        if self._val > self._maxi:
            self._val = self._maxi
