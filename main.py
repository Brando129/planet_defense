# Imports
import pygame
import os
import time
import random

# Create width/height for our screeen, and set name for the display.
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Defense")

# Load images.
red_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
green_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
blue_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player ship.
yellow_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers.
red_laser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
green_laser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
blue_laser = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
yellow_laser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background.
bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# Game loop function
def main_loop():
    run = True
    fps = 60
    level = 1
    lives = 3
    clock = pygame.time.Clock()

    def redraw_window():
        win.blit(bg, (0,0))
        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main_loop()