import pygame

class SpaceShip:
    
    def __init__(self,ai_run_blue_program):
        self.screen = ai_run_blue_program.screen
        self.screen_rect = ai_run_blue_program.screen.get_rect()

        self.image= pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center 

    def blitme(self):
        self.screen.blit(self.image, self.rect)