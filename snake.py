import pygame
from enum import Enum

Direction = Enum('Direction', ['UP', 'DOWN', 'RIGHT', 'LEFT'])

HEAD_COLOUR = (255, 0, 0)
BODY_COLOUR = (0, 0, 255)

class SnakeSegment:
    def __init__(self, x: int, y: int, direction: Direction, colour: tuple, size: int):
        self.x = x
        self.y = y
        self.direction = direction
        self.colour = colour
        self.size = size

    def render(self, WINDOW):
        rectangle = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(WINDOW, self.colour, rectangle)

class Snake:
    def __init__(self, head_x: int, head_y: int, segment_size: int, direction: Direction = Direction.DOWN):
        self.head_x = head_x
        self.head_y = head_y
        self.direction = direction
        if segments is None:
            segments = [
                SnakeSegment(head_x, head_y, direction, HEAD_COLOUR, segment_size),
                SnakeSegment(head_x, head_y - segment_size, direction, BODY_COLOUR, segment_size)    # put this body segment above the head to start
            ]
        self.segments = segments

    def render(self, WINDOW: pygame.Surface):
        for segment in self.segments:
            segment.render(WINDOW)
