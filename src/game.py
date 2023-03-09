import pygame
import sys
import debug as dbg
import fpsmeter as fm
from settings import *
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, pygame.RESIZABLE)
        pygame.display.set_caption("Islet Roasters: Brewing Away!")

        self.clock = pygame.time.Clock()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def draw(self):
        self.screen.fill("black")
        fm.fpsMeter(f"{self.clock.get_fps() :.1f}")

    def update(self):
        pygame.display.update()
        self.clock.tick(FPS)
    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()

