import pygame
from Parts import Game
from Parts import Paddle
from Parts import Ball


pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

SQ_SIZE = 10
board_shape = [int(WIDTH/SQ_SIZE), int((HEIGHT-200)/SQ_SIZE)]

ball_w = 8
ball_h = 8
ball_speed = -9
ball = Ball(WIN, round(WIDTH/2 - ball_w/2), 650, ball_w, ball_h, ball_speed)

paddle_w = 100
paddle_h = 20
paddle_speed = 15
paddle = Paddle(WIN, WIDTH/2 - paddle_w/2, HEIGHT - paddle_h - 10, paddle_w, paddle_h, paddle_speed)
FPS = 30


game = Game(WIN, FPS, board_shape, SQ_SIZE, ball, paddle)
game.run()
