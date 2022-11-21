import pygame
import sys
import random
from pygame.locals import *
from debug import draw_grid
import snake

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_SQUARE_SIZE = 50

SNAKE_START = (WINDOW_WIDTH - 2 * GRID_SQUARE_SIZE, 2 * GRID_SQUARE_SIZE)

snake_object = snake.Snake(SNAKE_START[0], SNAKE_START[1], snake.Direction.DOWN, WINDOW_WIDTH - GRID_SQUARE_SIZE, WINDOW_HEIGHT - GRID_SQUARE_SIZE, GRID_SQUARE_SIZE)

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

# The main function that controls the game
def main():
    looping = True
    frames = 0
    # Main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Processing: Section will be built later
        pressed = pygame.key.get_pressed()
        snake_object.update_direction(pressed)

        if frames % 30 == 0:
            snake_object.update()

        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        draw_grid(WINDOW, GRID_SQUARE_SIZE)
        snake_object.render(WINDOW)

        pygame.display.update()
        fpsClock.tick(FPS)
        frames += 1

main()