import pygame
from enum import Enum

Direction = Enum('Direction', ['UP', 'DOWN', 'RIGHT', 'LEFT'])

HEAD_COLOUR = (255, 0, 0)
BODY_COLOUR = (0, 0, 255)

class SnakeSegment:
    def __init__(self, x: int, y: int, colour: tuple, size: int):
        self.x = x
        self.y = y
        self.colour = colour
        self.size = size

    def update(self, new_position: tuple):
        self.x = new_position[0]
        self.y = new_position[1]

    def render(self, WINDOW):
        rectangle = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(WINDOW, self.colour, rectangle)

class Snake:
    def __init__(self, head_x: int, head_y: int, segment_size: int, head_direction: Direction):
        self.head_x = head_x
        self.head_y = head_y
        self.head_direction = head_direction
        self.segment_size = segment_size
        
        self.segments = [
            SnakeSegment(head_x, head_y, HEAD_COLOUR, segment_size),
            SnakeSegment(head_x, head_y - segment_size, BODY_COLOUR, segment_size)    # put this body segment above the head to start
        ]

    def update(self):
        updated_head_position = self.get_update_head_position()
        head = self.segments[0]
        prev_head_position = (head.x, head.y)

        # update head
        head.update(updated_head_position)

        # update the rest of the snake segments
        prev_segment_position = prev_head_position
        for segment in self.segments[1:]:
            # save current segment position
            current_position = (segment.x, segment.y)
            # update current segment position to be in the position of the last segment
            segment.update(prev_segment_position)
            # update last segment to be current segment
            prev_segment_position = current_position

    def get_update_head_position(self) -> tuple:
        head = self.segments[0]

        if self.head_direction == Direction.UP:
            return (head.x, head.y - self.segment_size)
        elif self.head_direction == Direction.DOWN:
            return (head.x, head.y + self.segment_size)
        elif self.head_direction == Direction.RIGHT:
            return (head.x + self.segment_size, head.y)
        else:   # Direction.LEFT
            return (head.x - self.segment_size, head.y)

    def render(self, WINDOW: pygame.Surface):
        for segment in self.segments:
            segment.render(WINDOW)
