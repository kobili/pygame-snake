from snake import Snake, Direction
from food import Food
import pygame
import random

class GameState:
    def __init__(self, window: pygame.Surface, grid_size: int, window_width: int, window_height: int):
        self.snake = Snake(window_width - 2 * grid_size, 2 * grid_size, Direction.DOWN, window_width - grid_size, window_height - grid_size, grid_size)
        self.food = Food(grid_size, window_height - 2 * grid_size, grid_size)
        self.window = window
        self.grid_size = grid_size
        self.window_width = window_width
        self.window_height = window_height

    def handle_input(self, pressed):
        self.snake.update_direction(pressed)

    def update(self):
        self.snake.update()

        # check if snake has eaten the foot
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.snake.tail_length += 1
            self.food = Food(
                self.grid_size * random.randint(0, (self.window_width / self.grid_size) - 1),
                self.grid_size * random.randint(0, (self.window_height / self.grid_size) - 1), 
                self.grid_size
            )
    
    def render(self):
        self.snake.render(self.window)
        self.food.render(self.window)