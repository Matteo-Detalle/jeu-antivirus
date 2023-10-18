import pygame , sys
pygame.init()

pygame.display.set_caption("Anti-virus Game Menu")

from jeu import *
from button import Button

#mise en place des fps

horloge = pygame.time.Clock()
fps = 60

#import des images

background = pygame.image.load("assets/background.png")
boutton_options_image = pygame.image.load("assets/Options.png")
boutton_quitter_image = pygame.image.load("assets/Quitter.png")
boutton_jouer_image = pygame.image.load("assets/Jouer.png")
Plateau_image = pygame.image.load("assets/PlateauDeJeu.png")

#paramètres de base

screen = pygame.display.set_mode((1600,900))
running = True
enJeu = False

Options_button = Button(500,200,boutton_options_image,1)
Quitter_button = Button(500,450,boutton_quitter_image,1)
Jouer_button = Button(500,-50,boutton_jouer_image,1)

while running:

    screen.blit(background, (0,0))
    horloge.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                enJeu = False
    if enJeu == False:
        Options_button.draw(screen)
        Quitter_button.draw(screen)
        Jouer_button.draw(screen)

        if Quitter_button.pressed():
            pygame.quit()
            sys.exit()
        if Options_button.pressed():
            ""
        if Jouer_button.pressed():
            enJeu = True
    elif enJeu == True:
        screen.blit(Plateau_image,(0,0))
        
    pygame.display.update()



