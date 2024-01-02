# Balles que le joueur doit attraper
import pygame
import random

class Balle(pygame.sprite.Sprite):
    "Balle"
    def __init__(self, x,screen):
        super().__init__()
        self.image = pygame.Surface((20,10))
        self.image.fill((255,255,255))
        self.x = x if x is not None else random.randint(20, 400) # Position x initiale de la balle
        self.y = 20 # Position y initiale de la balle

        self.rect = self.image.get_rect() # Obtenir le rectangle de l'image de la balle
        self.rect.x = self.x # Position x actuelle de la balle
        self.rect.y = self.y # Position y actuelle de la balle

        self.vitesse = random.uniform(0.45, 1) # On choisit une vitesse de déplacement au hasard

        self.screen = screen # Surface sur laquelle on va dessiner la balle

    def fall(self):
        "La balle tombe"
        self.rect.y += self.vitesse
        print("Position y de la balle :", self.rect.y)


    def clear(self):
        self.screen.fill((0,0,0))    

    def draw(self):
        "Dessiner la balle à l'écran"
        #self.screen.fill((0,0,0))
        self.screen.blit(self.image, (self.rect.x,  self.rect.y)) 
    
