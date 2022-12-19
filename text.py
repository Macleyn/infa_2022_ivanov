# FILE in which all the functions for working with text messages are stored.
import pygame

pygame.init()
from constants import *


def message(str, color, x, y):
    #The following functions print a text message on the screen
    #Arguments:     str(string) - the text of the message
    #               color(pygame.color) - the color of the text
    #               x(int) - x coordinate of the text first letter's position
    #               y(int) - y coordinate of the text first letter's position
    msg = font_style.render(str, True, color)
    dis.blit(msg, [x, y])


def score_write(score):
    # The following function prints player's score in the top left corner of the screen
    # Arguments:    score(int) - player's score
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])  # - score display.