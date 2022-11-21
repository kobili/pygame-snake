import pygame

class Food:
    def __init__(self, x: int, y: int, square_size: int):
        self.x = x
        self.y = y
        self.square_size = square_size
        # self.snake_x = snake_x
        # self.snake_y = snake_y

    def render(self, WINDOW: pygame.Surface):
        square = pygame.Rect(self.x, self.y, self.square_size, self.square_size)
        pygame.draw.rect(WINDOW, (0, 255, 0), square)
