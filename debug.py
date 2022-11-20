import pygame

def draw_grid(WINDOW: pygame.Surface, grid_square_side_length: int):
    window_height = WINDOW.get_height()
    window_width = WINDOW.get_width()
    COLOUR_BLACK = (0, 0, 0)

    for i in range(0, window_width, grid_square_side_length):
        pygame.draw.line(WINDOW, COLOUR_BLACK, (i, 0), (i, window_height), 1)

    for j in range(0, window_height, grid_square_side_length):
        pygame.draw.line(WINDOW, COLOUR_BLACK, (0, j), (window_width, j), 1)
    