import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Create class to manage bullets fired from ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.sceen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect (0,0) and set it to the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height,)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullets position as decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up to the screen"""
        #update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        #update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.sceen, self.color, self.rect)
        