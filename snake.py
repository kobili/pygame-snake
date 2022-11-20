from __future__ import annotations
import pygame
from pygame.locals import *
from enum import Enum

Direction = Enum('Direction', ['UP', 'DOWN', 'RIGHT', 'LEFT'])

HEAD_COLOUR = (255, 0, 0)
BODY_COLOUR = (0, 0, 255)

class SnakeSegment:
    def __init__(self, x: int, y: int, segment_size: int, colour: tuple, direction: Direction, prev: SnakeSegment | None, next: SnakeSegment | None):
        self.x = x
        self.y = y,
        self.segment_size = segment_size
        self.colour = colour
        self.direction = direction
        self.prev = prev
        self.next = next

    # def update(self, direction: Direction, segment_size: int, max_x: int, max_y: int):
    #     self.direction = direction
    #     if direction == Direction.UP:
    #         self.y = clamp(self.y - segment_size, 0, max_y)
    #     elif direction == Direction.DOWN:
    #         self.y = clamp(self.y + segment_size, 0, max_y)
    #     elif direction == Direction.RIGHT:
    #         self.x = clamp(self.x + segment_size, 0, max_x)
    #     elif direction == Direction.LEFT:
    #         self.x = clamp(self.x - segment_size, 0, max_x)

    def render(self, WINDOW):
        current_segment: SnakeSegment = self

        while(current_segment is not None):
            rectangle = pygame.Rect(self.x, self.y, self.segment_size, self.segment_size)
            pygame.draw.rect(WINDOW, self.colour, rectangle)

class Snake:
    def __init__(self, head_x: int, head_y: int, segment_size: int, head_direction: Direction, max_x: int, max_y: int):
        self.head_x = head_x
        self.head_y = head_y
        self.head_direction = head_direction
        self.segment_size = segment_size
        
        self.max_x = max_x
        self.max_y = max_y

        self.head_segment = SnakeSegment(head_x, head_y, segment_size, HEAD_COLOUR, Direction.DOWN, None, None)
        self.tail_segment = SnakeSegment(head_x, head_y - segment_size, segment_size, BODY_COLOUR, Direction.DOWN, self.head_segment, None)
        self.head_segment.next = self.tail_segment
        

    # def update(self, pressed):

    #     # update direction based on user input
    #     if (pressed[K_RIGHT] or pressed[K_d]):
    #         self.head_direction = Direction.RIGHT
    #     if (pressed[K_LEFT] or pressed[K_a]):
    #         self.head_direction = Direction.LEFT
    #     if (pressed[K_UP] or pressed[K_w]):
    #         self.head_direction = Direction.UP
    #     if (pressed[K_DOWN] or pressed[K_s]):
    #         self.head_direction = Direction.DOWN

    #     new_direction = self.head_direction

    #     for segment in self.segments:
    #         temp = segment.direction
    #         segment.update(new_direction, self.segment_size, self.max_x, self.max_y)
    #         new_direction = temp

    def render(self, WINDOW: pygame.Surface):
        self.head_segment.render(WINDOW)

def clamp(x: int, min: int, max: int) -> int:
    if x < min:
        x = min
    elif x > max:
        x = max
    return x