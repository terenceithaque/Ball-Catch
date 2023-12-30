# Script principal du jeu
import pygame # Importer le module pygame
pygame.init() # Initialiser pygame


largeur_ecran = 800 # Largeur maximale de la fenêtre de jeu
hauteur_ecran = 600 # Hauteur maximale de la fenêtre de jeu

ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran)) # Créer l'écran de jeu avec les dimensions désirées
pygame.display.set_caption("Ball-Catch")

execution = True # On crée une variable pour tenir compte de l'état de l'exécution du jeu

while execution: # Tant que le jeu est en cours d'exécution

    for evenement in pygame.event.get(): # On intercèpte tous les évènements qui ont lieu pendant l'exécution du jeu
        if evenement.type == pygame.QUIT: # Si le joueur veut quitter le jeu
            execution = False # Dans ce cas on arrête l'exécution du jeu