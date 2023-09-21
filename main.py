# Imports
import pygame
import os
import time
import random

# Initialize the in game font.
pygame.font.init()

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

# Classes.
# Ship Class.
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))

# Game loop function.
def main_loop():
    run = True
    fps = 60
    level = 1
    lives = 3
    main_font = pygame.font.SysFont("comicsans", 50)
    player_vel = 5 
    clock = pygame.time.Clock()

    ship = Ship(380, 650)

    def redraw_window():
        win.blit(bg, (0,0))
        # Draw text.
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        win.blit(lives_label, (10,10))
        win.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        ship.draw(win)

        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Moving the player keys.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship.x - player_vel > 0: # LEFT
            ship.x -= player_vel
        if keys[pygame.K_RIGHT] and ship.x + player_vel + 50 < WIDTH: # RIGHT
            ship.x += player_vel
        if keys[pygame.K_UP] and ship.y - player_vel > 0: # UP
            ship.y -= player_vel
        if keys[pygame.K_DOWN] and ship.y + player_vel + 50 < HEIGHT: # DOWN
            ship.y += player_vel

main_loop()