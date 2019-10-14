import pygame
from pygame.locals import *


class Button(object):
    def __init__(self, color, params, shape = 'rect'):
        self.color = color # color should be a rgb tuple (#,#,#)
        self.shape = shape
        if shape == 'rect':
            self.params = params # params: (#,#,#,#)
        else:
            raise ValueError("invalid button shape")

    def Draw(self, display, text=None, text_color=(0,0,0)):
        if self.shape == 'rect':
            pygame.draw.rect(display, self.color, self.params)
            if text is not None:
                text_font = pygame.font.Font("freesansbold.ttf", 17)
                text_surface = text_font.render(text, True, text_color)
                text_rect = text_surface.get_rect()
                text_rect.center = (self.params[0] + self.params[2]/2, self.params[1] + self.params[3]/2)
                display.blit(text_surface, text_rect)
        else:
            raise ValueError("invalid button shape")

    def isClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.shape == 'rect':
            if self.params[0] < mouse_pos[0] < self.params[0] + self.params[2] and \
                self.params[1] < mouse_pos[1] < self.params[1] + self.params[3]:
                return True
            else:
                return False
        else:
            raise ValueError("invalid button shape")
