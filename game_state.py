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
        self.snake.handle_input(pressed)

    def update(self):
        self.snake.update()

        # check if snake has eaten itself
        if (self.snake.x, self.snake.y) in self.snake.tail:
            self.__restart_game()

        # check if snake has eaten the food
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.__eat_food()
            
    def __eat_food(self):
        self.snake.tail_length += 1

        new_food_position = (
            self.grid_size * random.randint(0, (self.window_width / self.grid_size) - 1),
            self.grid_size * random.randint(0, (self.window_height / self.grid_size) - 1)
        )

        # try a new location if food is spawned in snake
        while new_food_position in self.snake.tail or new_food_position == (self.snake.x, self.snake.y):
            new_food_position = (
                self.grid_size * random.randint(0, (self.window_width / self.grid_size) - 1),
                self.grid_size * random.randint(0, (self.window_height / self.grid_size) - 1)
            )

        self.food = Food(
            new_food_position[0],
            new_food_position[1],
            self.grid_size
        )

    def __restart_game(self):
        self.snake = Snake(self.window_width - 2 * self.grid_size, 2 * self.grid_size, Direction.DOWN, self.window_width - self.grid_size, self.window_height - self.grid_size, self.grid_size)
        self.food = Food(self.grid_size, self.window_height - 2 * self.grid_size, self.grid_size)
    
    def render(self):
        self.snake.render(self.window)
        self.food.render(self.window)