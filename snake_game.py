import pygame

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Set up the game clock
clock = pygame.time.Clock()

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the snake
snake_size = 20
snake_speed = 10

# Set up the initial position of the snake
snake_x = window_width / 2
snake_y = window_height / 2

# Set up the initial velocity of the snake
snake_dx = 0
snake_dy = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the snake position
    snake_x += snake_dx
    snake_y += snake_dy

    # Clear the game window
    window.fill(black)

    # Draw the snake
    pygame.draw.rect(window, white, (snake_x, snake_y, snake_size, snake_size))

    # Update the game display
    pygame.display.update()

    # Set the game clock tick
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
