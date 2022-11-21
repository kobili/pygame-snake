from __future__ import annotations
from enum import Enum
import pygame

Direction = Enum('Direction', ['UP', 'DOWN', 'LEFT', 'RIGHT'])

HEAD_COLOUR = (255, 0, 0)
TAIL_COLOUR = (0, 0, 255)

class Snake:
    def __init__(self, start_x: int, start_y: int, direction: Direction, max_x: int, max_y: int, segment_size: int):
        self.direction = direction
        self.max_x = max_x
        self.max_y = max_y
        self.segment_size = segment_size

        self.head = SnakeSegment(start_x, start_y, None, None)
        self.tail = SnakeSegment(start_x, start_y - segment_size, self.head, None)
        self.head.next = self.tail

    def render(self, WINDOW: pygame.Surface):
        current_segment = self.head
        isHead = True
        while not current_segment is None:
            colour = TAIL_COLOUR

            if isHead:
                colour = HEAD_COLOUR
                isHead = False

            current_segment.render(WINDOW, colour, self.segment_size)
            current_segment = current_segment.next


class SnakeSegment:
    def __init__(self, x: int, y: int, prev: SnakeSegment | None, next: SnakeSegment | None):
        self.x = x
        self.y = y
        self.last_x = x
        self.last_y = y

        self.prev = prev
        self.next = next
    
    def render(self, WINDOW: pygame.Surface, colour: tuple, segment_size: int):
        square = pygame.Rect(self.x, self.y, segment_size, segment_size)

        pygame.draw.rect(WINDOW, colour, square)