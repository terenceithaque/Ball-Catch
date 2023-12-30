# Balles que le joueur doit attraper
import pygame

class Balle(pygame.sprite.Sprite):
    "Balle"
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.Surface((11,5))
        self.image.fill((255,255,255))
        self.x = 120 # Position x initiale de la balle
        self.y = 20 # Position y initiale de la balle

        self.rect = self.image.get_rect() # Obtenir le rectangle de l'image de la balle
        self.rect.x = self.x # Position x actuelle de la balle
        self.rect.y = self.y # Position y actuelle de la balle

        self.screen = screen # Surface sur laquelle on va dessiner la balle

    def fall(self):
        "La balle tombe"
        self.rect.y += 0.50

    def draw(self):
        "Dessiner la balle à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))    