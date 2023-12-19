'''
Classic Snake Game
'''
import pygame
import random
# Initialize the game
pygame.init()
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Set the width and height of the game window
window_width = 800
window_height = 600
window_size = (window_width, window_height)
game_window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snake Game")
# Set the clock for the game
clock = pygame.time.Clock()
# Set the snake properties
snake_block_size = 20
snake_speed = 15
# Define the font for displaying the score
font_style = pygame.font.SysFont(None, 50)
def display_score(score):
    '''
    Display the score on the game window
    '''
    score_text = font_style.render("Score: " + str(score), True, WHITE)
    game_window.blit(score_text, [10, 10])
def draw_snake(snake_block_size, snake_list):
    '''
    Draw the snake on the game window
    '''
    for x in snake_list:
        pygame.draw.rect(game_window, GREEN, [x[0], x[1], snake_block_size, snake_block_size])
def game_loop():
    '''
    Main game loop
    '''
    game_over = False
    game_close = False
    # Initialize the snake position and movement
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0
    # Initialize the snake body
    snake_list = []
    snake_length = 1
    # Generate the initial food position
    food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0
    while not game_over:
        while game_close:
            # Game over screen
            game_window.fill(BLACK)
            game_over_text = font_style.render("Game Over!", True, RED)
            game_window.blit(game_over_text, [window_width / 2 - 100, window_height / 2 - 50])
            display_score(snake_length - 1)
            pygame.display.update()
            # Ask the user to play again or quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0
        # Check for boundaries and self-collision
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_window.fill(BLACK)
        pygame.draw.rect(game_window, RED, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        draw_snake(snake_block_size, snake_list)
        display_score(snake_length - 1)
        pygame.display.update()
        # Check if the snake has eaten the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0
            snake_length += 1
        pygame.display.flip()  # Update the game window
        clock.tick(snake_speed)
    pygame.quit()
# Start the game
game_loop()