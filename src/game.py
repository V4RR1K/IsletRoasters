"""
Game holds the main game class information
Greg Lynskey
03/05/2023
"""
import pygame
import sys
import debug as dbg
import level
import fpsmeter as fm
import settings as st

class Game:
    def __init__(self):
        self.settings = st.settings()
        pygame.init()

        if self.settings.FULL_SCREEN:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))

        pygame.display.set_caption("Islet Roasters: Brewing Away!")
        pygame.display.set_icon(pygame.image.load("assets/player/MainCharacterForwardIdle.png"))
        self.level = level.Level()

        self.clock = pygame.time.Clock()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_MINUS):
                pygame.quit()
                sys.exit()
    def draw(self):
        self.screen.fill("black")
        self.level.run()
        fm.fpsMeter(f"{self.clock.get_fps() :.1f}")
        dbg.debug("8==D")

    def update(self):
        pygame.display.update()
        self.clock.tick(self.settings.FPS)
    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()

