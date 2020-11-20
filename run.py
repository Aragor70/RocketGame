import pygame
import sys
from rocket import Rocket

class Game(object):
    def __init__(self):
        # config
        self.max_tps = 300.0

        # initialization
        pygame.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        # player
        self.player = Rocket(self)

        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            # ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0

            while self.tps_delta > 1 / self.max_tps:
                self.tick() # run 300 ticks per second
                self.tps_delta -= 1 / self.max_tps
            # drawing

            self.screen.fill((0, 0, 0))  # clear the screen
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()

if __name__ == "__main__":
    Game()
