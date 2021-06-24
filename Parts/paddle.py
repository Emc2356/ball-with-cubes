import pygame


class Paddle:
    def __init__(self, WIN: pygame.surface.Surface, x: float, y: float, w: float, h: float, speed: int, color: tuple=(150, 150, 150)):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.color = color

    def draw(self):
        pygame.draw.rect(self.WIN, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

    def move(self):
        self.x += self.speed

    def change_direction(self):
        self.speed *= -1

    def is_moving_right(self):
        if self.speed > 0:
            return True
        return False

    def out_of_bounds(self):
        if self.x + self.speed <= 0 or self.x + self.w + self.speed >= self.WIN.get_width():
            return True
        return False

    def collision(self, ball):
        if ball.y + ball.h >= self.y and ball.y + ball.h <= self.y + self.h and ball.x + ball.w >= self.x and ball.x <= self.x + self.w:
            return True
        return False
