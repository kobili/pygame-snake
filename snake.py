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
        self.y = y
        self.segment_size = segment_size
        self.colour = colour
        self.direction = direction
        self.prev = prev
        self.next = next

    def update(self, direction: Direction, max_x: int, max_y: int):
        self.direction = direction

        new_x = self.x
        new_y = self.y

        if direction == Direction.UP:
            new_y = clamp(self.y - self.segment_size, 0, max_y)
        elif direction == Direction.DOWN:
            new_y = clamp(self.y + self.segment_size, 0, max_y)
        elif direction == Direction.RIGHT:
            new_x = clamp(self.x + self.segment_size, 0, max_x)
        elif direction == Direction.LEFT:
            new_x = clamp(self.x - self.segment_size, 0, max_x)

        if (not self.prev is None):
            if (new_x == self.prev.x and new_y == self.prev.y):
                # do nothing so segments don't overlap
                return
                
        self.x = new_x
        self.y = new_y
            

    def render(self, WINDOW):
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

        # initialize head segment and one body segment
        self.head_segment = SnakeSegment(head_x, head_y, segment_size, HEAD_COLOUR, Direction.DOWN, None, None)
        self.tail_segment = SnakeSegment(head_x, head_y - segment_size, segment_size, BODY_COLOUR, Direction.DOWN, self.head_segment, None)
        self.head_segment.next = self.tail_segment
        

    def update(self, pressed):
        previous_segment_direction = self.head_direction
        # update direction based on user input
        if (pressed[K_RIGHT] or pressed[K_d]):
            self.head_direction = Direction.RIGHT
        if (pressed[K_LEFT] or pressed[K_a]):
            self.head_direction = Direction.LEFT
        if (pressed[K_UP] or pressed[K_w]):
            self.head_direction = Direction.UP
        if (pressed[K_DOWN] or pressed[K_s]):
            self.head_direction = Direction.DOWN

        # Update the head position first
        self.head_segment.update(self.head_direction, self.max_x, self.max_y)

        current_segment = self.head_segment.next
        while (not current_segment is None):
            current_segment_direction = current_segment.direction
            current_segment.update(previous_segment_direction, self.max_x, self.max_y)
            current_segment = current_segment.next
            previous_segment_direction = current_segment_direction


    def render(self, WINDOW: pygame.Surface):
        current_segment = self.head_segment
        while (not current_segment is None):
            current_segment.render(WINDOW)
            current_segment = current_segment.next




def clamp(x: int, min: int, max: int) -> int:
    if x < min:
        x = min
    elif x > max:
        x = max
    return x