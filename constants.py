# The following file contains all constants that are used in the project
import pygame
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()
snake_block = 10  # The size of one piece of snake
snake_basespeed = 5  # Snake's initial speed on level 0
# Text stylization
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 15)