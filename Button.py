import pygame

from constants import FONT_NAME

class Button:
    def __init__(self, color, x, y, width, height, text="", text_size=60):
        self._is_pressed = False
        self._color = color
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._text = text
        self._text_size = text_size

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self.width

    @property
    def height(self):
        return self._height

    @property
    def is_pressed(self):
        return self._is_pressed

    @is_pressed.setter
    def is_pressed(self, state):
        self._is_pressed = state


    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text


    def draw(self, surf: pygame.Surface, outline = None):
        #For hovering
        if(outline):
            pygame.draw.rect(surf, outline, (self._x - 2, self._y - 2, self._width + 4, self._height + 4), 0)

        pygame.draw.rect(surf, self._color, (self._x, self._y, self._width, self._height), 0)

        if(self._text != ''):
            font = pygame.font.SysFont(FONT_NAME, self._text_size)
            text = font.render(self._text, 1, (255,255,255))
            surf.blit(text, ((self._x + (self._width / 2 - text.get_width() / 2)), self._y + (self._height / 2 - text.get_height()/2)))


    def is_over(self, pos):
        if(pos[0] > self._x and pos[0] < self._x + self._width and pos[1] > self._y and pos[1] < self._y + self._height):
          return True
        else:
          return False

    def set_hover(self):
        self._color = (235,245,255)

    def del_hover(self):
        self._color = (0,0,0)
