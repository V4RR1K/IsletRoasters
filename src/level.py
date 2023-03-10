"""

Greg Lynskey
03/~/2023
"""
import pygame

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        pass