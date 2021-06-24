import pygame


class Box:
    def __init__(self, WIN: pygame.surface.Surface, x: int, y: int, w: int, h: int, color: tuple=(200, 200, 200)):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw(self):
        pygame.draw.rect(self.WIN, self.color, pygame.Rect(self.x + 1, self.y + 1, self.w - 2, self.h - 2))

