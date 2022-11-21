import pygame
import sys
import random
from pygame.locals import *
from debug import draw_grid
from game_state import GameState

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_SQUARE_SIZE = 20

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

game_state = GameState(WINDOW, GRID_SQUARE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT)

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
        game_state.handle_input(pressed)

        if frames % 30 == 0:
            game_state.update()

        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        draw_grid(WINDOW, GRID_SQUARE_SIZE)
        game_state.render()

        pygame.display.update()
        fpsClock.tick(FPS)
        frames += 1

main()