import pygame
from pygame.math import Vector2

class Rocket(object):
    def __init__(self, game):
        self.game = game

        size = self.game.screen.get_size()

        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

        self.speed = 1.2
        self.gravity = 0.5




    def add_force(self, force):
        self.acceleration += force

    def tick(self):
        # input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -self.speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed, 0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed, 0))

        # border
        if self.position[0] < 0:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = 0
        if self.position[0] > self.game.width - 50:
            self.position[0] = self.game.width - 50
        if self.position[1] > self.game.height - 50:
            self.position[1] = self.game.height - 50

        # physics
        self.velocity *= 0.8 # resistance
        self.velocity -= Vector2(0, -self.gravity)
        # gravity

        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0




    def draw(self):
        # draw the player
        points = [Vector2(0, -10), Vector2(5, 5), Vector2(-5, 5)]

        angle = self.velocity.angle_to(Vector2(0, 1))

        points = [p.rotate(angle) for p in points]

        # fix y axis
        points = [Vector2(p.x, p.y * -1) for p in points]

        points = [self.position + p * 2 for p in points]

        pygame.draw.polygon(self.game.screen, (0, 100, 255), points)
