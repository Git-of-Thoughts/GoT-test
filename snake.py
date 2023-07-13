import pygame

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game

    # Draw the game
    window.fill(black)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
