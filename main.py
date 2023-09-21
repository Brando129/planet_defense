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
bg = pygame.image.load(os.path.join("assets", "background-black.png"))