# Script principal du jeu
import pygame # Importer le module pygame
from joueur import * # Importer toutes les propriétés provenant du fichier joueur.py
from tkinter import messagebox
pygame.init() # Initialiser pygame





largeur_ecran = 800 # Largeur maximale de la fenêtre de jeu
hauteur_ecran = 600 # Hauteur maximale de la fenêtre de jeu

ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran)) # Créer l'écran de jeu avec les dimensions désirées
pygame.display.set_caption("Ball-Catch")

joueur = Joueur(screen=ecran) # Créer un nouveau joueur

execution = True # On crée une variable pour tenir compte de l'état de l'exécution du jeu

def demander_quitter():
    "Demander au joueur s'il souhaite quitter le jeu"
    quit = messagebox.askquestion("Désirez-vous quitter le jeu ?", "Souhaitez-vous quitter le jeu maintenant ?") # On affiche une boîte de dialogue pour demander au joueur de confirmer la fin de la partie
    if quit == "yes": # Si le joueur clique sur "Oui"
        global execution
        execution = False # Alors on arrête l'exécution du jeu

while execution: # Tant que le jeu est en cours d'exécution

    touches = pygame.key.get_pressed() # Obtenir toutes les touches pressées par le joueur pendant l'exécution du jeu

    for evenement in pygame.event.get(): # On intercèpte tous les évènements qui ont lieu pendant l'exécution du jeu
        if evenement.type == pygame.QUIT or touches[pygame.K_ESCAPE]: # Si le joueur veut quitter le jeu
            demander_quitter() # On demande au joueur de confirmer la fin de la partie

    joueur.mettre_a_jour_pos(touches)        

    joueur.draw()  # Dessiner le joueur à l'écran

    pygame.display.flip()