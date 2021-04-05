#!/usr/bin/python

import pygame

class Ship:
    """A class to manage the player ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store decimal value for ships horizontal position
        self.x = float(self.rect.x)
        
        # Ship control flags
        self.moving_right = False
        self.moving_left = False
        self.shooting = False

    def update(self):
        """Update the ship's movement flags."""
        # Update self.x float value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
            
        # Update rect object with self.x coordinates
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        
        self.screen.blit(self.image, self.rect)