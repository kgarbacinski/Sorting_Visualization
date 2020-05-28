import pygame

class Button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, surf: pygame.Surface, outline = None):
        #For hovering
        if(outline):
            pygame.draw.rect(surf, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(surf, self.color, (self.x, self.y, self.width, self.height), 0)

        if(self.text != ''):
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (255,255,255))
            surf.blit(text, ((self.x + (self.width / 2 - text.get_width() / 2)), self.y + (self.height / 2 - text.get_height()/2)))


    def set_text(self, text):
        self.text = text

    def is_over(self, pos):
        if(pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height):
          return True
        else:
          return False

    def set_hover(self):
        self.color = (235,245,255)

    def del_hover(self):
        self.color = (0,0,0)
