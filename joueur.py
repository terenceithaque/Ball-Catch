# Joueur
import pygame

class Joueur(pygame.sprite.Sprite):
    "Joueur"
    def __init__(self, screen):
        super().__init__() # On hérite des attributs de la classe Sprite
        self.image = pygame.Surface((10, 60))
        self.image = pygame.transform.rotate(self.image, 90)
        self.image.fill((255,255,255))
        self.x = 400 # Position x de départ du joueur
        self.y = 500 # Position y de départ du joueur

        self.rect = self.image.get_rect() # Obtenir le rectangle de l'image du joueur

        self.rect.x = self.x # Position x actuelle du joueur
        self.rect.y = self.y # Position y actuelle du joueur

        self.screen = screen # Surface sur laquelle on affichera le joueur


    def mettre_a_jour_pos(self, touche):
        "Mettre à jour la position de la raquette du joueur"
        if touche[pygame.K_LEFT]: # Si le joueur presse la touche "flèche vers la gauche"
            self.rect.x -= 0.75 # Metttre à jour la position x de la raquette de manière à la déplacer vers la gauche
            #print("Position x actuelle du joueur :", self.rect.x)
            if self.rect.x < 0: # On doit vérifier à chaque déplacement que la raquette ne sort pas de l'écran
                self.rect.x = 0 # Et si c'est le cas, alors on la replace sur l'écran

        if touche[pygame.K_RIGHT]: # Si le joueur presse la touche "flèche vers la droite"
            self.rect.x += 0.75 # Mettre à jour la position de la raquette de manière à la déplacer vers la droite
            #print("Position x actuelle du joueur :", self.rect.x)
            if self.rect.x > 750: # On doit vérifier à chaque déplacement que la raquette ne sort pas de l'écran
                self.rect.x = 750  # Et si c'est le cas, alors on la replace sur l'écran


    def draw(self):
        "Dessiner le joueur à l'écran"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))    
