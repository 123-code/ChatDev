'''
Snake Class
'''
import pygame
class Snake:
    '''
    Represents the snake in the game
    '''
    def __init__(self, x, y, block_size):
        '''
        Initialize the snake with position and block size
        '''
        self.x = x
        self.y = y
        self.block_size = block_size
        self.x_change = 0
        self.y_change = 0
    def move(self, direction):
        '''
        Move the snake in the specified direction
        '''
        if direction == 'left':
            self.x_change = -self.block_size
            self.y_change = 0
        elif direction == 'right':
            self.x_change = self.block_size
            self.y_change = 0
        elif direction == 'up':
            self.y_change = -self.block_size
            self.x_change = 0
        elif direction == 'down':
            self.y_change = self.block_size
            self.x_change = 0
        self.x += self.x_change
        self.y += self.y_change
    def draw(self, game_window, color):
        '''
        Draw the snake on the game window
        '''
        pygame.draw.rect(game_window, color, [self.x, self.y, self.block_size, self.block_size])