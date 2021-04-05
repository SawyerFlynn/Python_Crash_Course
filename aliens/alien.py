#!/usr/bin/python

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alient instance."""
    def __init__(self, ai_game):
        """Initialize the alien, set starting position and attributes."""
        super().__init__()
        self.screen = ai_game.screen
        
        # Load alien image and set rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
