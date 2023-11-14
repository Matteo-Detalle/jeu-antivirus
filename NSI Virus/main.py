import pygame , sys
pygame.init()
from jeu import *

pygame.display.set_caption("Anti-virus Game")

horloge = pygame.time.Clock()
fps = 30

screen = pygame.display.set_mode((1600,900))

running = True
menu1 = True
menu_explication = False
menu_jouer = False
niveau1,niveau2,niveau3,niveau4,niveau5,niveau6,niveau7,niveau8,niveau9 = False,False,False,False,False,False,False,False,False
niveau1_class = Niveau()
niveau2_class = Niveau()
niveau3_class = Niveau()

background = pygame.image.load("assets/background.png")

boutton_regle_image = pygame.image.load("assets/Regle.png")
boutton_quitter_image = pygame.image.load("assets/Quitter.png")
boutton_jouer_image = pygame.image.load("assets/Jouer.png")

fleche_up_image = pygame.image.load("assets/fleche_upleft.png")

Regle_button = Button(600,300,boutton_regle_image,1)
Quitter_button = Button(600,550,boutton_quitter_image,1)
Jouer_button = Button(600,50,boutton_jouer_image,1)

niveau1_image = pygame.image.load("assets/niveau1.png")
niveau2_image = pygame.image.load("assets/niveau2.png")
niveau3_image = pygame.image.load("assets/niveau3.png")
niveau4_image = pygame.image.load("assets/niveau4.png")
niveau5_image = pygame.image.load("assets/niveau5.png")
niveau6_image = pygame.image.load("assets/niveau6.png")
niveau7_image = pygame.image.load("assets/niveau7.png")
niveau8_image = pygame.image.load("assets/niveau8.png")
niveau9_image = pygame.image.load("assets/niveau9.png")

niveau1_button = Button(450,200,niveau1_image,1)
niveau2_button = Button(600,200,niveau2_image,1)
niveau3_button = Button(750,200,niveau3_image,1)
niveau4_button = Button(900,200,niveau4_image,1)
niveau5_button = Button(450,400,niveau5_image,1)
niveau6_button = Button(600,400,niveau6_image,1)
niveau7_button = Button(750,400,niveau7_image,1)
niveau8_button = Button(900,400,niveau8_image,1)
niveau9_button = Button(675,600,niveau9_image,1)

fleche_up_button = Button(900,700,fleche_up_image,1)

Plateau_image = pygame.image.load("assets/PlateauDeJeu.png")

piece_non_jouable_image , piece_diagonale_image , piece_droite_image , piece_violette_image , piece_rose_image , piece_verte_image = niveau1_class.images()
niveau1_first_launch = True
niveau2_first_launch = True
niveau3_first_launch = True

font = pygame.font.Font(None, 36)
echap_text = font.render("Appuyez sur Echap pour revenir en arrière",True,(255,255,255))

while running:
    screen.blit(background, (0,0))
    horloge.tick(fps)

    if menu1 == True:
        Regle_button.draw(screen)
        Quitter_button.draw(screen)
        Jouer_button.draw(screen)

        if Quitter_button.pressed():
            pygame.quit()
            sys.exit()
        if Regle_button.pressed():
            menu_explication,menu1 = True, False
        if Jouer_button.pressed():
            menu_jouer,menu1 = True , False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

    if menu_explication == True:
        regle_texte = font.render("Objectif : mettre la pièce rouge dans le trou en haut à gauche ",True,(255,255,255))
        regle_texte2 = font.render("Pour ce faire , vous pourrez selectionner une pièce et la bouger à l'aide des flèches directionnels du clavier ",True,(255,255,255))
        regle_texte3 = font.render("ou bien en clickant sur les boutons à l'écran",True,(255,255,255))
        screen.blit(regle_texte,(70,200))
        screen.blit(regle_texte2,(150,250))
        screen.blit(regle_texte3,(150,300))
        screen.blit(echap_text,(500,800))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    menu_explication , menu1 = False , True

    
    if menu_jouer == True:
        niveau1_button.draw(screen)
        niveau2_button.draw(screen)
        niveau3_button.draw(screen)
        niveau4_button.draw(screen)
        niveau5_button.draw(screen)
        niveau6_button.draw(screen)
        niveau7_button.draw(screen)
        niveau8_button.draw(screen)
        niveau9_button.draw(screen)

        if niveau1_button.pressed():
            menu_jouer,niveau1 = False , True
        if niveau2_button.pressed():
            menu_jouer,niveau2 = False , True
        if niveau3_button.pressed():
            menu_jouer,niveau3 = False , True
        if niveau4_button.pressed():
            menu_jouer,niveau4 = False , True
        if niveau5_button.pressed():
            menu_jouer,niveau5 = False , True
        if niveau6_button.pressed():
            menu_jouer,niveau6 = False , True
        if niveau7_button.pressed():
            menu_jouer,niveau7 = False , True
        if niveau8_button.pressed():
            menu_jouer,niveau8 = False , True
        if niveau9_button.pressed():
            menu_jouer,niveau9 = False , True
        
        screen.blit(echap_text,(500,800))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    menu_jouer , menu1 = False , True

    #Initialisation de tous les niveaux (tous se ressemble juste avec un nombre et des pièces différentes)

    if niveau1 == True:
        screen.blit(Plateau_image,(0,0))

        if niveau1_first_launch == True:
            position_piece_non_jouable1 = niveau1_class.emplacement((3,1)) #emplacement d'origine
            position_piece_non_jouable2 = niveau1_class.emplacement((3,5))
            position_piece_diagonale = niveau1_class.emplacement([(1,5),(2,6)])
            position_piece_droite = niveau1_class.emplacement([(1,1),(1,3)])

            rect_piece_droite = piece_droite_image.get_rect()
            rect_piece_droite.topleft = (570,165)

            rect_piece_diagonale = piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (990,165)
            
            niveau1_class.update_plateau([1,2],[5,6],2,[99,99],[99,99]) #initialisation de la pièce diagonale dans la plateau
            niveau1_class.update_plateau([1,1],[1,3],3,[99,99],[99,99]) #initialisation de la pièce droite dans le plateau
            niveau1_class.update_plateau([3,3],[1,5],1,[99,99],[99,99]) #initialisation des pièces non jouables dans le plateau

            piece_selectionnée_text = font.render("Pas de Pièce sélectionnée", True, (255, 255, 255))
            piece_rose_text = font.render("Pièce rose sélectionnée", True, (255, 255, 255))
            piece_rouge_text = font.render("Pièce rouge sélectionnée", True, (255, 255, 255))

            pièce_selectionnée = False

            niveau1_first_launch = False
        
        screen.blit(piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(piece_droite_image, rect_piece_droite.topleft)
        screen.blit(piece_non_jouable_image,(570,375)) #espace de 210 entre 2 espaces jouables donc 105 pour espace de 1
        screen.blit(piece_non_jouable_image,(990,375))
        screen.blit(piece_selectionnée_text,(70,500))
        
        fleche_up_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau1 , menu_jouer = False , True
                if event.key == pygame.K_LEFT:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]-1)
                            newx.append(i[1]-1)
                        if niveau1_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True :
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]-1 , i[1]-1))

                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_droite:
                                position_piece_droite = new_position

                            pièce_selectionnée = new_position
                        elif niveau1_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau1 , menu_jouer = False , True
                
                if event.key == pygame.K_RIGHT:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]+1)
                            newx.append(i[1]+1)
                        if niveau1_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]+1 , i[1]+1))
                            
                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_droite:
                                position_piece_droite = new_position
                            
                            pièce_selectionnée = new_position
                        elif niveau1_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau1 , menu_jouer = False , True
                
                if event.key == pygame.K_UP:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]-1)
                            newx.append(i[1]+1)
                        if niveau1_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]-1 , i[1]+1))
                            
                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_droite:
                                position_piece_droite = new_position
                            
                            pièce_selectionnée = new_position
                        elif niveau1_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau1 , menu_jouer = False , True
                
                if event.key == pygame.K_DOWN:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]+1)
                            newx.append(i[1]-1)
                        if niveau1_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]+1 , i[1]-1))
                            
                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_droite:
                                position_piece_droite = new_position
                                
                            pièce_selectionnée = new_position
                        elif niveau1_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau1 , menu_jouer = False , True


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
                        piece_selectionnée_text = piece_rose_text

                    elif rect_piece_diagonale.collidepoint(pos):
                        pièce_selectionnée = position_piece_diagonale
                        liste_id = [2,3,4,5,6,7,8,9]
                        pièce_id = 2
                        liste_id.remove(2)
                        rect_pièce_selectionnée = rect_piece_diagonale
                        piece_selectionnée_text = piece_rouge_text

    if niveau2 == True:
        screen.blit(Plateau_image,(0,0))

        if niveau2_first_launch == True:
            position_piece_non_jouable1 = niveau2_class.emplacement((2,4)) #emplacement d'origine
            position_piece_non_jouable2 = niveau2_class.emplacement((4,0))
            position_piece_diagonale = niveau2_class.emplacement([(3,5),(4,6)])
            position_piece_violette = niveau2_class.emplacement([(1,1),(1,3),(3,3)])

            rect_piece_violette = piece_violette_image.get_rect()
            rect_piece_violette.topleft = (570,165) #465 + x*105 et 60 + y*105 du point en haut à gauche

            rect_piece_diagonale = piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (990,375)
            
            niveau2_class.update_plateau([3,4],[5,6],2,[99,99],[99,99]) #initialisation de la pièce diagonale dans la plateau
            niveau2_class.update_plateau([1,1,3],[1,3,3],3,[99,99,99],[99,99,99]) #initialisation de la pièce violette dans le plateau
            niveau2_class.update_plateau([2,4],[4,0],1,[99,99],[99,99]) #initialisation des pièces non jouables dans le plateau

            piece_selectionnée_text = font.render("Pas de Pièce sélectionnée", True, (255, 255, 255))
            piece_violette_text = font.render("Pièce violette sélectionnée", True, (255, 255, 255))
            piece_rouge_text = font.render("Pièce rouge sélectionnée", True, (255, 255, 255))

            pièce_selectionnée = False

            niveau2_first_launch = False
        
        screen.blit(piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(piece_violette_image, rect_piece_violette.topleft)
        screen.blit(piece_non_jouable_image,(465,480)) 
        screen.blit(piece_non_jouable_image,(885,270))
        screen.blit(piece_selectionnée_text,(70,500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau2 , menu_jouer = False , True
                if event.key == pygame.K_LEFT:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]-1)
                            newx.append(i[1]-1)
                        if niveau2_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True :
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]-1 , i[1]-1))

                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_violette:
                                position_piece_violette = new_position

                            pièce_selectionnée = new_position
                        elif niveau2_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau2 , menu_jouer = False , True
                
                if event.key == pygame.K_RIGHT:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]+1)
                            newx.append(i[1]+1)
                        if niveau2_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]+1 , i[1]+1))
                            
                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_violette:
                                position_piece_violette = new_position
                            
                            pièce_selectionnée = new_position
                        elif niveau2_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau2 , menu_jouer = False , True
                
                if event.key == pygame.K_UP:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]-1)
                            newx.append(i[1]+1)
                        if niveau2_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]-1 , i[1]+1))
                            
                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_violette:
                                position_piece_violette = new_position
                            
                            pièce_selectionnée = new_position
                        elif niveau2_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau2 , menu_jouer = False , True
                
                if event.key == pygame.K_DOWN:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]+1)
                            newx.append(i[1]-1)
                        if niveau2_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]+1 , i[1]-1))
                            
                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_violette:
                                position_piece_violette = new_position
                                
                            pièce_selectionnée = new_position
                        elif niveau2_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau2 , menu_jouer = False , True


            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  #vérifie si clique gauche
                    pos = pygame.mouse.get_pos() 

                    #vérifie sur quelle pièce le clique a été fait
                    if rect_piece_violette.collidepoint(pos): 
                        pièce_selectionnée = position_piece_violette
                        liste_id = [2,3,4,5,6,7,8,9]
                        pièce_id = 3
                        liste_id.remove(3)
                        rect_pièce_selectionnée = rect_piece_violette
                        piece_selectionnée_text = piece_violette_text

                    elif rect_piece_diagonale.collidepoint(pos):
                        pièce_selectionnée = position_piece_diagonale
                        liste_id = [2,3,4,5,6,7,8,9]
                        pièce_id = 2
                        liste_id.remove(2)
                        rect_pièce_selectionnée = rect_piece_diagonale
                        piece_selectionnée_text = piece_rouge_text

    if niveau3 == True:
        screen.blit(Plateau_image,(0,0))

        if niveau3_first_launch == True:
            position_piece_non_jouable1 = niveau3_class.emplacement((4,0)) #emplacement d'origine (y,x)
            position_piece_non_jouable2 = niveau3_class.emplacement((3,3))
            position_piece_diagonale = niveau3_class.emplacement([(0,4),(1,5)])
            position_piece_verte = niveau3_class.emplacement([(2,2),(2,4)])
            position_piece_rose = niveau3_class.emplacement([(0,6),(2,6)])

            rect_piece_verte = piece_verte_image.get_rect()
            rect_piece_verte.topleft = (675,270) #465 + x*105 et 60 + y*105 du point en haut à gauche

            rect_piece_diagonale = piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (885,60)

            rect_piece_rose = piece_rose_image.get_rect()
            rect_piece_rose.topleft = (1095,60)
            
            niveau3_class.update_plateau([0,1],[4,5],2,[99,99],[99,99]) #initialisation de la pièce diagonale dans la plateau
            niveau3_class.update_plateau([2,2],[2,4],3,[99,99],[99,99]) #initialisation de la pièce verte dans le plateau
            niveau3_class.update_plateau([0,2],[6,6],4,[99,99],[99,99]) #initialisation de la pièce rose dans le plateau
            niveau3_class.update_plateau([4,3],[0,3],1,[99,99],[99,99]) #initialisation des pièces non jouables dans le plateau

            piece_selectionnée_text = font.render("Pas de Pièce sélectionnée",True,(255,255,255))
            piece_rose_text = font.render("Pièce rose sélectionnée",True,(255,255,255))
            piece_rouge_text = font.render("Pièce rouge sélectionnée",True,(255,255,255))
            piece_verte_text = font.render("Pièce verte sélectionnée",True,(255,255,255))

            pièce_selectionnée = False

            niveau3_first_launch = False
        
        screen.blit(piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(piece_verte_image, rect_piece_verte.topleft)
        screen.blit(piece_rose_image, rect_piece_rose.topleft)
        screen.blit(piece_non_jouable_image,(465,480)) 
        screen.blit(piece_non_jouable_image,(780,375))
        screen.blit(piece_selectionnée_text,(70,500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau3 , menu_jouer = False , True
                if event.key == pygame.K_LEFT:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]-1)
                            newx.append(i[1]-1)
                        if niveau3_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True :
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]-1 , i[1]-1))

                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_verte:
                                position_piece_verte = new_position
                            elif pièce_selectionnée == position_piece_rose:
                                position_piece_rose = new_position

                            pièce_selectionnée = new_position
                        elif niveau3_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau3 , menu_jouer = False , True
                
                if event.key == pygame.K_RIGHT:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]+1)
                            newx.append(i[1]+1)
                        if niveau3_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]+1 , i[1]+1))
                            
                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_verte:
                                position_piece_verte = new_position
                            elif pièce_selectionnée == position_piece_rose:
                                position_piece_rose = new_position
                            
                            pièce_selectionnée = new_position
                        elif niveau3_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau3 , menu_jouer = False , True
                
                if event.key == pygame.K_UP:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]-1)
                            newx.append(i[1]+1)
                        if niveau3_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]-1 , i[1]+1))
                            
                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_verte:
                                position_piece_verte = new_position
                            elif pièce_selectionnée == position_piece_rose:
                                position_piece_rose = new_position
                            
                            pièce_selectionnée = new_position
                        elif niveau3_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau3 , menu_jouer = False , True
                
                if event.key == pygame.K_DOWN:
                    if pièce_selectionnée == False:
                        pass
                    else:
                        oldx , oldy , newx , newy = [],[],[],[]
                        for i in pièce_selectionnée:
                            oldy.append(i[0])
                            oldx.append(i[1])
                            newy.append(i[0]+1)
                            newx.append(i[1]-1)
                        if niveau3_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]+1 , i[1]-1))
                            
                            if pièce_selectionnée == position_piece_diagonale:
                                position_piece_diagonale = new_position
                            elif pièce_selectionnée == position_piece_verte:
                                position_piece_verte = new_position
                            elif pièce_selectionnée == position_piece_rose:
                                position_piece_rose = new_position
                                
                            pièce_selectionnée = new_position
                        elif niveau3_class.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau3 , menu_jouer = False , True
            
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  #vérifie si clique gauche
                    pos = pygame.mouse.get_pos() 

                    #vérifie sur quelle pièce le clique a été fait
                    if rect_piece_verte.collidepoint(pos): 
                        pièce_selectionnée = position_piece_verte
                        liste_id = [2,3,4,5,6,7,8,9]
                        pièce_id = 3
                        liste_id.remove(3)
                        rect_pièce_selectionnée = rect_piece_verte
                        piece_selectionnée_text = piece_verte_text

                    elif rect_piece_diagonale.collidepoint(pos):
                        pièce_selectionnée = position_piece_diagonale
                        liste_id = [2,3,4,5,6,7,8,9]
                        pièce_id = 2
                        liste_id.remove(2)
                        rect_pièce_selectionnée = rect_piece_diagonale
                        piece_selectionnée_text = piece_rouge_text
                    
                    elif rect_piece_rose.collidepoint(pos):
                        pièce_selectionnée = position_piece_rose
                        liste_id = [2,3,4,5,6,7,8,9]
                        pièce_id = 4
                        liste_id.remove(4)
                        rect_pièce_selectionnée = rect_piece_rose
                        piece_selectionnée_text = piece_rose_text

    if niveau4 == True:
        screen.blit(Plateau_image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau4 , menu_jouer = False , True

    if niveau5 == True:
        screen.blit(Plateau_image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau5 , menu_jouer = False , True

    if niveau6 == True:
        screen.blit(Plateau_image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau6 , menu_jouer = False , True
                
    if niveau7 == True:
        screen.blit(Plateau_image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau7 , menu_jouer = False , True

    if niveau8 == True:
        screen.blit(Plateau_image,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau8 , menu_jouer = False , True

    if niveau9 == True:
        screen.blit(Plateau_image,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau9 , menu_jouer = False , True
    
    pygame.display.update()

