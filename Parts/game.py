import pygame
from .box import Box
from .ball import Ball
from .paddle import Paddle


class Game:
    def __init__(self, WIN: pygame.surface.Surface, FPS: int, board_shape: list, SQ_SIZE: int, ball: Ball, paddle: Paddle):
        self.WIN = WIN
        self.WIDTH = WIN.get_width()
        self.HEIGHT = WIN.get_height()
        self.FPS = FPS
        self.board_shape = board_shape
        self.SQ_SIZE = SQ_SIZE
        self.ball = ball
        self.paddle = paddle
        self.font = pygame.font.SysFont("comicsans", 100)
        self.boxes = []
        self.popped = []

    def create_boxes(self):
        self.boxes = [
            [
                [

                ] for _ in range(self.board_shape[1])
            ] for _ in range(self.board_shape[0])
        ]

        y = 0
        for row in range(self.board_shape[0]):
            x = 0
            for column in range(self.board_shape[1]):
                self.boxes[row][column] = Box(self.WIN, y, x, self.SQ_SIZE, self.SQ_SIZE)
                x += self.SQ_SIZE
            y += self.SQ_SIZE

    def create_paddle_ball(self):
        ball_w = 8
        ball_h = 8
        ball_speed = -9
        self.ball = Ball(self.WIN, round(self.WIDTH / 2 - ball_w / 2), 650, ball_w, ball_h, ball_speed)

        paddle_w = 100
        paddle_h = 20
        paddle_speed = 15
        self.paddle = Paddle(self.WIN, self.WIDTH / 2 - paddle_w / 2, self.HEIGHT - paddle_h - 10, paddle_w, paddle_h, paddle_speed)

    def draw(self):
        self.WIN.fill((30, 30, 30))

        for row in range(self.board_shape[0]):
            for column in range(self.board_shape[1]):
                if not [row, column] in self.popped:
                    self.boxes[row][column].draw()
        self.ball.draw()
        self.paddle.draw()

        pygame.display.update()

    def collision(self):
        if self.paddle.collision(self.ball):
            self.ball.speed_y *= -1
            self.ball.y += self.ball.speed_y

        for row in range(self.board_shape[0]):
            for column in range(self.board_shape[1]):
                if not [row, column] in self.popped:
                    if self.ball.collide(self.boxes[row][column]):
                        self.popped.append([row, column])

    @staticmethod
    def event_handler():
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit(-1)

    def move(self):
        # move the ball and check if the ball is out of the bounds
        self.ball.move()
        self.ball.out_of_bounds()

        # move paddle based on keys that are pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if self.paddle.x > 0:
                    if self.paddle.is_moving_right():
                        self.paddle.change_direction()
                        self.paddle.move()
                    else:
                        self.paddle.move()
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if self.paddle.x + self.paddle.w <= self.WIDTH:
                    if self.paddle.is_moving_right():
                        self.paddle.move()
                    else:
                        self.paddle.change_direction()
                        self.paddle.move()

    def check_if_game_over(self):
        if self.ball.y > self.HEIGHT:
            score_label = self.font.render(f"""score: {len(self.popped)}""", True, (255, 0, 0))
            self.WIN.blit(score_label, (self.WIDTH/2 - score_label.get_width()/2, self.HEIGHT/2 - score_label.get_height()/2))
            press_button = self.font.render(f"""press 'r' to restart the game""", True, (255, 0, 0))
            self.WIN.blit(press_button, (self.WIDTH/2 - press_button.get_width()/2, self.HEIGHT/2 - press_button.get_height()/2 + score_label.get_height() + 10))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit(-1)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.popped = []
                        self.boxes = []
                        self.create_paddle_ball()
                        self.run()

    def run(self):
        self.create_boxes()
        while True:
            pygame.time.Clock().tick(self.FPS)
            self.draw()
            self.collision()
            self.event_handler()
            self.move()
            self.check_if_game_over()
