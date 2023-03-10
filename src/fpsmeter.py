"""

Greg Lynskey
03/~/2023
"""
import pygame
from settings import *

pygame.init()
font = pygame.font.Font(None, 30)

def fpsMeter(fps):
    curr_display = pygame.display.get_surface()
    message = font.render(str(fps), True, 'White')
    rect = message.get_rect(topright=(SCREEN_WIDTH - 20, 10))
    pygame.draw.rect(curr_display, 'Black', rect)
    curr_display.blit(message, rect)