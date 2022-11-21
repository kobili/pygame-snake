from snake import Snake, Direction
from food import Food
import pygame

class GameState:
    def __init__(self, window: pygame.Surface, grid_size: int, window_width: int, window_height: int):
        self.snake = Snake(window_width - 2 * grid_size, 2 * grid_size, Direction.DOWN, window_width - grid_size, window_height - grid_size, grid_size)
        self.food = Food(grid_size, window_height - 2 * grid_size, grid_size)
        self.window = window

    def handle_input(self, pressed):
        self.snake.update_direction(pressed)

    def update(self):
        self.snake.update()
    
    def render(self):
        self.food.render(self.window)
        self.snake.render(self.window)