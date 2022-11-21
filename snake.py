from __future__ import annotations
from enum import Enum
import pygame
from pygame.locals import *

Direction = Enum('Direction', ['UP', 'DOWN', 'LEFT', 'RIGHT'])

HEAD_COLOUR = (255, 0, 0)
TAIL_COLOUR = (0, 0, 255)

class Snake:
    def __init__(self, start_x: int, start_y: int, direction: Direction, max_x: int, max_y: int, segment_size: int, tail_length: int = 1):
        self.direction = direction
        self.max_x = max_x
        self.max_y = max_y
        self.segment_size = segment_size

        self.x = start_x
        self.y = start_y
        self.tail_length = tail_length
        self.tail = [(start_x, start_y - segment_size)]

    def update_direction(self, pressed):
        if pressed[K_UP] or pressed[K_w]:
            self.direction = Direction.UP
        elif pressed[K_RIGHT] or pressed[K_d]:
            self.direction = Direction.RIGHT
        elif pressed[K_DOWN] or pressed[K_s]:
            self.direction = Direction.DOWN
        elif pressed[K_LEFT] or pressed[K_a]:
            self.direction = Direction.LEFT

    def update(self):

        self.tail.insert(0, (self.x, self.y))

        if self.direction == Direction.UP:
            self.y = clamp(self.y - self.segment_size, 0, self.max_y)
        elif self.direction == Direction.DOWN:
            self.y = clamp(self.y + self.segment_size, 0, self.max_y)
        elif self.direction == Direction.RIGHT:
            self.x = clamp(self.x + self.segment_size, 0, self.max_x)
        elif self.direction == Direction.LEFT:
            self.x = clamp(self.x - self.segment_size, 0, self.max_x)
        # if (self.x, self.y) == current_pos:
        #     return

        if len(self.tail) > self.tail_length:
            self.tail = self.tail[:-1]
        
    def render(self, WINDOW: pygame.Surface):
        head = pygame.Rect(self.x, self.y, self.segment_size, self.segment_size)
        pygame.draw.rect(WINDOW, HEAD_COLOUR, head)

        for position in self.tail:
            tail = pygame.Rect(position[0], position[1], self.segment_size, self.segment_size)
            pygame.draw.rect(WINDOW, TAIL_COLOUR, tail)

def clamp(x, min, max):
    if x < min:
        x = min
    elif x > max:
        x = max
    return x