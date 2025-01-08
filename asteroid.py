import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, center=self.position, radius=self.radius, color="white", width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)