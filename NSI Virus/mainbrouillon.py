import pygame , sys
pygame.init()

pygame.display.set_caption("Anti-virus Menu")

from jeubrouillon import *

#mise en place des fps

horloge = pygame.time.Clock()
fps = 30

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
pièce_selectionnée = False

Options_button = Button(500,200,boutton_options_image,1)
Quitter_button = Button(500,450,boutton_quitter_image,1)
Jouer_button = Button(500,-50,boutton_jouer_image,1)

niveau1 = Niveau1()
#initialisation des pièces dans la tableau

niveau1.pièce([(3,1),(3,5)],1) #pièces non jouables
niveau1.pièce([(1,1),(1,3)],3) #pièce droite
niveau1.pièce([(1,5),(2,6)],2) #pièce diagonale

position_piece_non_jouable1 = niveau1.position_piece_non_jouable1 #(3,1)
position_piece_non_jouable2 = niveau1.position_piece_non_jouable2 #(3,5)
position_piece_diagonale = niveau1.position_piece_diagonale #[(1,5),(2,6)]
position_piece_droite = niveau1.position_piece_droite #[(1,1),(1,3)]

piece_non_jouable_image , piece_diagonale_image , piece_droite_image = niveau1.pièces()

rect_piece_droite = piece_droite_image.get_rect()
rect_piece_droite.topleft = (570,165)

rect_piece_diagonale = piece_diagonale_image.get_rect()
rect_piece_diagonale.topleft = (990,165)

while running:

    screen.blit(background, (0,0))
    horloge.tick(fps)
    plateau = Plateau()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.set_caption("Anti-virus Menu")
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
            pygame.display.set_caption("Anti-virus Game")
            enJeu = True

    elif enJeu == True:

        screen.blit(Plateau_image,(0,0))
        screen.blit(piece_non_jouable_image,(570,375)) #espace de 210 entre 2 espaces jouables donc 105 pour espace de 1
        screen.blit(piece_non_jouable_image,(990,375))
        screen.blit(piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(piece_droite_image, rect_piece_droite.topleft)

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  #vérifie si clique gauche
                    pos = pygame.mouse.get_pos() 

                    #vérifie sur quelle pièce le clique a été fait
                    if rect_piece_droite.collidepoint(pos): 
                       pièce_selectionnée = position_piece_droite
                       liste_id = [2,3,4,5,6,7,8,9]
                       pièce_id = 3
                       liste_id.remove(3)
                       rect_pièce_selectionnée = rect_piece_droite
                       print("pièce rose selectionnée")

                    elif rect_piece_diagonale.collidepoint(pos):
                        pièce_selectionnée = position_piece_diagonale
                        liste_id = [2,3,4,5,6,7,8,9]
                        pièce_id = 2
                        liste_id.remove(2)
                        rect_pièce_selectionnée = rect_piece_diagonale
                        print("pièce rouge selectionnée")
                       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tabx,taby,tabOldx,tabOldy = [] , [] , [] , []
                    if pièce_selectionnée == False:
                        print("Selectionnez une pièce")
                    else:
                        for i in range(len(pièce_selectionnée)):
                            y,x = pièce_selectionnée[i]
                            tabOldx.append(x) #enregistre les anciens emplacement de x et y
                            tabOldy.append(y)
    
                            pièce_selectionnée[i] = (y-1,x-1) #nouvelle coordonées

                            tabx.append(x-1)
                            taby.append(y-1)  

                            tab = []     

                        for i in pièce_selectionnée:
                            if niveau1.mouvement_possible(i[0],i[1],liste_id) == False:
                                print("Mouvement impossible")
                                tabx,taby,tabOldx,tabOldy = [] , [] , [] , []
                                tab.append(False)
                            elif niveau1.mouvement_possible(i[0],i[1],liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                                print("GG")
                                enJeu = False      
                            else: tab.append(True)

                        if tab ==[True,True]:
                            for i in range(len(tabx)):
                                niveau1.update_plateau(taby[i],tabx[i],pièce_id,tabOldy[i],tabOldx[i])
                            y,x = pièce_selectionnée[0]
                            x,y = (x*105)+465, (y*105)+60 #465 et 60 étant les coordonées du point 0 , 0
                            rect_pièce_selectionnée.topleft = (x,y)
                            tab = []
                
                if event.key == pygame.K_RIGHT:
                    tabx,taby,tabOldx,tabOldy = [] , [] , [] , []
                    if pièce_selectionnée == False:
                        print("Selectionnez une pièce")
                    else:
                        tab = []
                        for i in range(len(pièce_selectionnée)):
                            y,x = pièce_selectionnée[i]
                            tabOldx.append(x)
                            tabOldy.append(y)
                            pièce_selectionnée[i] = (y+1,x+1)
                            tabx.append(x+1)
                            taby.append(y+1)                        
                        for i in pièce_selectionnée:
                            if niveau1.mouvement_possible(i[0],i[1],liste_id) == False:
                                print("Mouvement impossible")
                                tabx,taby,tabOldx,tabOldy = [] , [] , [] , []
                                tab.append(False)
                            elif niveau1.mouvement_possible(i[0],i[1],liste_id) == True and pièce_selectionnée == position_piece_diagonale:
                                print("GG")
                                enJeu = False            
                            else:
                                tab.append(True)

                        if tab == [True,True]:
                            for i in range(len(tabx)):
                                niveau1.update_plateau(taby[i],tabx[i],pièce_id,tabOldy[i],tabOldx[i])
                            y,x = pièce_selectionnée[0]
                            x,y = (x*105)+465, (y*105)+60
                            rect_pièce_selectionnée.topleft = (x,y)
                            tab = []

                if event.key == pygame.K_UP:
                    tabx,taby,tabOldx,tabOldy = [] , [] , [] , []
                    if pièce_selectionnée == False:
                        print("Selectionnez une pièce")
                    else:
                        tab = []
                        for i in range(len(pièce_selectionnée)):
                            y,x = pièce_selectionnée[i]
                            tabOldx.append(x)
                            tabOldy.append(y)
                            pièce_selectionnée[i] = (y-1,x+1)
                            tabx.append(x+1)
                            taby.append(y+1)                        
                        for i in pièce_selectionnée:
                            if niveau1.mouvement_possible(i[0],i[1],liste_id) == False:
                                print("Mouvement impossible")
                                tabx,taby,tabOldx,tabOldy = [] , [] , [] , []
                                tab.append(False)
                            elif niveau1.mouvement_possible(i[0],i[1],liste_id) == True and pièce_selectionnée == position_piece_diagonale:
                                print("GG")
                                enJeu = False            
                            else:
                                tab.append(True)

                        if tab == [True,True]:
                            for i in range(len(tabx)):
                                niveau1.update_plateau(taby[i],tabx[i],pièce_id,tabOldy[i],tabOldx[i])
                            y,x = pièce_selectionnée[0]
                            x,y = (x*105)+465, (y*105)+60
                            rect_pièce_selectionnée.topleft = (x,y)
                            tab = []
                
                if event.key == pygame.K_DOWN:
                    tabx,taby,tabOldx,tabOldy = [] , [] , [] , []
                    if pièce_selectionnée == False:
                        print("Selectionnez une pièce")
                    else:
                        tab = []
                        for i in range(len(pièce_selectionnée)):
                            y,x = pièce_selectionnée[i]
                            tabOldx.append(x)
                            tabOldy.append(y)
                            pièce_selectionnée[i] = (y+1,x-1)
                            tabx.append(x+1)
                            taby.append(y+1)                        
                        for i in pièce_selectionnée:
                            if niveau1.mouvement_possible(i[0],i[1],liste_id) == False:
                                print("Mouvement impossible")
                                tabx,taby,tabOldx,tabOldy = [] , [] , [] , []
                                tab.append(False)
                            elif niveau1.mouvement_possible(i[0],i[1],liste_id) == True and pièce_selectionnée == position_piece_diagonale:
                                print("GG")
                                enJeu = False            
                            else:
                                tab.append(True)

                        if tab == [True,True]:
                            for i in range(len(tabx)):
                                niveau1.update_plateau(taby[i],tabx[i],pièce_id,tabOldy[i],tabOldx[i])
                            y,x = pièce_selectionnée[0]
                            x,y = (x*105)+465, (y*105)+60
                            rect_pièce_selectionnée.topleft = (x,y)
                            tab = []
                    
                    

    pygame.display.update()


