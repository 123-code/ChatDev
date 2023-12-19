'''
Food Class
'''
import pygame
class Food:
    '''
    Represents the food in the game
    '''
    def __init__(self, x, y, block_size):
        '''
        Initialize the food with position and block size
        '''
        self.x = x
        self.y = y
        self.block_size = block_size
    def draw(self, game_window, color):
        '''
        Draw the food on the game window
        '''
        pygame.draw.rect(game_window, color, [self.x, self.y, self.block_size, self.block_size])