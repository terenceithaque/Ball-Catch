# Joueur
import pygame

class Joueur(pygame.sprite.Sprite):
    "Joueur"
    def __init__(self, screen):
        super().__init__() # On hérite des attributs de la classe Sprite
        self.image = pygame.Surface((10, 60))
        self.image.fill((255,255,255))
        self.x = 50 # Position x de départ du joueur
        self.y = 100 # Position y de départ du joueur

        self.rect = self.image.get_rect() # Obtenir le rectangle de l'image du joueur

        self.rect.x = self.x # Position x actuelle du joueur
        self.rect.y = self.y # Position y actuelle du joueur

        self.screen = screen # Surface sur laquelle on affichera le joueur

    def draw(self):
        "Dessiner le joueur à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))    
