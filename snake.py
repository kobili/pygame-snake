import pygame

class Snake:
    def __init__(self, head_x: int, head_y: int, length: int = 1):
        self.head_x = head_x
        self.head_y = head_y
        self.length = length
