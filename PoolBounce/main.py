from Pool import Ball, Pool, WIDTH, HEIGHT
import pygame
import sys
import random as rd

def generate_random_ball():
    x = rd.randint(0, WIDTH)
    y = rd.randint(0, HEIGHT)
    velX = rd.randint(-10, 10)
    velY = rd.randint(-10, 10)
    return Ball(x, y, velX, velY, 10)

def generate_random_balls(n):
    return [generate_random_ball() for _ in range(n)]

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pool Table Simulation')

# Create pool table with balls
poolTable = Pool(generate_random_balls(10), (0, 100, 0))

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the pool table
    poolTable.update(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
