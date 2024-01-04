# Script principal du jeu
import pygame # Importer le module pygame
from joueur import * # Importer toutes les propriétés provenant du fichier joueur.py
from balle import * # Importer toutes les propriétés provenant du fichier balle.py
from tkinter import messagebox
import random
pygame.init() # Initialiser pygame





largeur_ecran = 800 # Largeur maximale de la fenêtre de jeu
hauteur_ecran = 600 # Hauteur maximale de la fenêtre de jeu

ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran)) # Créer l'écran de jeu avec les dimensions désirées
pygame.display.set_caption("Ball-Catch")

joueur = Joueur(screen=ecran) # Créer un nouveau joueur
balles = pygame.sprite.Group(Balle(x=random.randint(20, 400), screen=ecran))
balles.add(Balle(x=random.randint(20,400), screen=ecran))

execution = True # On crée une variable pour tenir compte de l'état de l'exécution du jeu

pause = False # On crée une variable pour savoir si le jeu est en pause on non

def mettre_pause():
    "Mettre le jeu en pause"
    global pause
    if pause == False: # Si le jeu n'est pas en pause
        pause_font = pygame.font.Font(None, 30)
        texte_pause = "Pause ! (Touche Espace pour reprendre)"
        pause = True 
        ecran.blit(pause_font.render(texte_pause, True, (255, 255, 255)), (0,50))
        pygame.display.update()
        

    else:
        pause = False   

def demander_quitter():
    "Demander au joueur s'il souhaite quitter le jeu"
    quit = messagebox.askquestion("Désirez-vous quitter le jeu ?", "Souhaitez-vous quitter le jeu maintenant ? Votre meilleur score est déjà sauvegardé.") # On affiche une boîte de dialogue pour demander au joueur de confirmer la fin de la partie
    if quit == "yes": # Si le joueur clique sur "Oui"
        global execution
        execution = False # Alors on arrête l'exécution du jeu

while execution: # Tant que le jeu est en cours d'exécution
    joueur.sauvegarder_score() # On sauvegarde le score du joueur à chaque frame pour pouvoir le récupérer en cas de besoin
    

    touches = pygame.key.get_pressed() # Obtenir toutes les touches pressées par le joueur pendant l'exécution du jeu

    for evenement in pygame.event.get(): # On intercèpte tous les évènements qui ont lieu pendant l'exécution du jeu
        if evenement.type == pygame.QUIT or touches[pygame.K_ESCAPE]: # Si le joueur veut quitter le jeu
            demander_quitter() # On demande au joueur de confirmer la fin de la partie

        if touches[pygame.K_SPACE]:
            mettre_pause() 

    killed_balls = [] # Liste des balles supprimées du jeu

    if not pause: 
        ecran.fill((0,0,0))
        

        #ecran.fill((0,0,0))          

        
        joueur.mettre_a_jour_pos(touches)
        joueur.draw()  # Dessiner le joueur à l'écran
        
            #print(list(balles))
            #balle.clear()
            
            
            #print(balle)
            
        copie_balles = balles.copy()

        for balle in copie_balles:
            
                balle.fall()

                if not balle.en_pos_depart(): # On vérifie si la balle a bougée ou non
                    balle.draw()
            #ecran.fill((0,0,0))

                    if balle.rect.colliderect(joueur.rect): # Si la balle entre en collision avec le joueur
                        print("La balle est entrée en collision avec le joueur")
                        balle.kill()
                        balles.remove(balle)
                        joueur.mettre_a_jour_score() # Mettre à jour le score du joueur
                        print("Score du joueur :", joueur.score)
                        balles.add(Balle(x=random.randint(20, 400), screen=ecran))

                    if balle.rect.y > 530:
                        print("La balle est sortie de l'écran")
                        balle.kill()
                        balles.remove(balle)

                        if len(balles) == 0:
                
                            balles.add(Balle(x=random.randint(20, 400), screen=ecran))


                #balles.clear(ecran, (0,0,0))

                else:
                    balle.kill()
                    balles.remove(balle)
                    balles.add(Balle(x=random.randint(20, 400), screen=ecran))                

        
            
    joueur.afficher_score() # Afficher le score du joueur à l'écran

    pygame.display.flip()