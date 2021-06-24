import pygame


class Ball:
    def __init__(self, WIN: pygame.surface.Surface, x: int, y: int, w: int, h: int, speed: int, color: tuple=(255, 0, 0)):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
        self.color = color

    def draw(self):
        pygame.draw.rect(self.WIN, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def out_of_bounds(self):
        if self.x <= 0 or self.x + self.w >= self.WIN.get_width():
            self.speed_x *= -1
        if self.y <= 0:
            self.speed_y *= -1

    def collide(self, box):
        if pygame.Rect(box.x, box.y, box.w, box.h).collidepoint(self.x, self.y):
            self.speed_y *= -1
            return True
        return False

