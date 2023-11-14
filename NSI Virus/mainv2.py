import pygame , sys
pygame.init()
from jeuv2 import *

pygame.display.set_caption("Anti-virus Game")

horloge = pygame.time.Clock()
fps = 30

screen = pygame.display.set_mode((1600,900))

running = True
menu1 = True
menu_explication = False
menu_jouer = False
niveau_jouer = False
niveau_actuel = 0

niveau1_class, niveau2_class, niveau3_class, niveau4_class, niveau5_class, niveau6_class, niveau7_class, niveau8_class, niveau9_class = Niveau() , Niveau(), Niveau(), Niveau(), Niveau(), Niveau(), Niveau(), Niveau(), Niveau()

images = Image()

Regle_button = Button(600,300,images.boutton_regle_image,1)
Quitter_button = Button(600,550,images.boutton_quitter_image,1)
Jouer_button = Button(600,50,images.boutton_jouer_image,1)

niveau1_button = Button(450,200,images.niveau1_image,1)
niveau2_button = Button(600,200,images.niveau2_image,1)
niveau3_button = Button(750,200,images.niveau3_image,1)
niveau4_button = Button(900,200,images.niveau4_image,1)
niveau5_button = Button(450,400,images.niveau5_image,1)
niveau6_button = Button(600,400,images.niveau6_image,1)
niveau7_button = Button(750,400,images.niveau7_image,1)
niveau8_button = Button(900,400,images.niveau8_image,1)
niveau9_button = Button(675,600,images.niveau9_image,1)

fleche_upleft_button = Button(1000,800,images.fleche_upleft_image,1)
fleche_upright_button = Button(1050,800,images.fleche_upright_image,1)
fleche_downleft_button = Button(1000,850,images.fleche_downleft_image,1)
fleche_downright_button = Button(1050,850,images.fleche_downright_image,1)

niveau1_first_launch = True
niveau2_first_launch = True
niveau3_first_launch = True

font = pygame.font.Font(None, 36)
echap_text = font.render("Appuyez sur Echap pour revenir en arrière",True,(255,255,255))

def menu1_fonction():
    global menu1, menu_explication, menu_jouer , running

    Regle_button.draw(screen)
    Quitter_button.draw(screen)
    Jouer_button.draw(screen)

    if Quitter_button.pressed():
        pygame.quit()
        sys.exit()
    if Regle_button.pressed():
        menu1 = False
        menu_explication = True
    if Jouer_button.pressed():
        menu_jouer,menu1 = True , False

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

def menu_explication_fonction():
    global menu1, menu_explication , running

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

def menu_jouer_fonction():
    global menu_jouer, niveau_actuel, running , menu1 , niveau_jouer

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
        menu_jouer,niveau_jouer,niveau_actuel = False , True , 1
    if niveau2_button.pressed():
        menu_jouer,niveau_jouer,niveau_actuel = False , True , 2
    if niveau3_button.pressed():
        menu_jouer,niveau_jouer,niveau_actuel = False , True , 3
    if niveau4_button.pressed():
        menu_jouer,niveau_jouer,niveau_actuel = False , True , 4
    if niveau5_button.pressed():
        menu_jouer,niveau_jouer,niveau_actuel = False , True , 5
    if niveau6_button.pressed():
        menu_jouer,niveau_jouer,niveau_actuel = False , True , 6
    if niveau7_button.pressed():
        menu_jouer,niveau_jouer,niveau_actuel = False , True , 7
    if niveau8_button.pressed():
        menu_jouer,niveau_jouer,niveau_actuel = False , True , 8
    if niveau9_button.pressed():
        menu_jouer,niveau_jouer,niveau_actuel = False , True , 9
        
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

while running:
    screen.blit(images.background, (0,0))
    horloge.tick(fps)

    if menu1 == True:
        menu1_fonction()
    elif menu_explication == True:
        menu_explication_fonction()
    elif menu_jouer == True:
        menu_jouer_fonction()
    elif niveau_jouer == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel, niveau_jouer , menu_jouer, niveau1_first_launch , niveau2_first_launch , niveau3_first_launch = 0 , False ,True , True , True , True
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
                        if niveau1_class.mouvement(newy,newx,oldy,oldx,rect_pièce_selectionnée,pièce_id,liste_id) == True :
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]-1 , i[1]-1))

                            if niveau_actuel == 1:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_droite:
                                    position_piece_droite = new_position
                            if niveau_actuel == 2:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_violette:
                                    position_piece_violette = new_position
                            if niveau_actuel == 3:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_verte:
                                    position_piece_verte = new_position
                                elif pièce_selectionnée == position_piece_rose:
                                    position_piece_rose = new_position

                            pièce_selectionnée = new_position
                        elif niveau1_class.mouvement(newy,newx,oldy,oldx,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau_actuel, niveau_jouer , menu_jouer, niveau1_first_launch , niveau2_first_launch , niveau3_first_launch = 0 , False ,True , True , True , True
                
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
                        if niveau1_class.mouvement(newy,newx,oldy,oldx,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]+1 , i[1]+1))
                            
                            if niveau_actuel == 1:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_droite:
                                    position_piece_droite = new_position
                            if niveau_actuel == 2:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_violette:
                                    position_piece_violette = new_position
                            if niveau_actuel == 3:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_verte:
                                    position_piece_verte = new_position
                                elif pièce_selectionnée == position_piece_rose:
                                    position_piece_rose = new_position
                            
                            pièce_selectionnée = new_position
                        elif niveau1_class.mouvement(newy,newx,oldy,oldx,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau_actuel, niveau_jouer , menu_jouer, niveau1_first_launch , niveau2_first_launch , niveau3_first_launch = 0 , False ,True , True , True , True 
                
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
                        if niveau1_class.mouvement(newy,newx,oldy,oldx,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]-1 , i[1]+1))
                            
                            if niveau_actuel == 1:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_droite:
                                    position_piece_droite = new_position
                            if niveau_actuel == 2:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_violette:
                                    position_piece_violette = new_position
                            if niveau_actuel == 3:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_verte:
                                    position_piece_verte = new_position
                                elif pièce_selectionnée == position_piece_rose:
                                    position_piece_rose = new_position
                            
                            pièce_selectionnée = new_position
                        elif niveau1_class.mouvement(newy,newx,oldy,oldx,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau_actuel, niveau_jouer , menu_jouer, niveau1_first_launch , niveau2_first_launch , niveau3_first_launch = 0 , False ,True , True , True , True 
                
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
                        if niveau1_class.mouvement(newy,newx,oldy,oldx,rect_pièce_selectionnée,pièce_id,liste_id) == True:
                            new_position = []
                            for i in pièce_selectionnée:
                                new_position.append((i[0]+1 , i[1]-1))
                            
                            if niveau_actuel == 1:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_droite:
                                    position_piece_droite = new_position
                            if niveau_actuel == 2:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_violette:
                                    position_piece_violette = new_position
                            if niveau_actuel == 3:
                                if pièce_selectionnée == position_piece_diagonale:
                                    position_piece_diagonale = new_position
                                elif pièce_selectionnée == position_piece_verte:
                                    position_piece_verte = new_position
                                elif pièce_selectionnée == position_piece_rose:
                                    position_piece_rose = new_position
                                
                            pièce_selectionnée = new_position
                        elif niveau1_class.mouvement(newy,newx,oldy,oldx,rect_pièce_selectionnée,pièce_id,liste_id) == "GG" and pièce_selectionnée == position_piece_diagonale:
                            niveau_actuel, niveau_jouer , menu_jouer, niveau1_first_launch , niveau2_first_launch , niveau3_first_launch = 0 , False ,True , True , True , True        
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  #vérifie si clique gauche
                    pos = pygame.mouse.get_pos() 

                    #vérifie sur quelle pièce le clique a été fait
                    if niveau_actuel == 1:
                        if rect_piece_droite.collidepoint(pos): 
                            pièce_selectionnée = position_piece_droite
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 3
                            liste_id.remove(3)
                            rect_pièce_selectionnée = rect_piece_droite
                            piece_selectionnée_text = piece_rose_text

                    if niveau_actuel == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 :
                        if rect_piece_diagonale.collidepoint(pos):
                            pièce_selectionnée = position_piece_diagonale
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 2
                            liste_id.remove(2)
                            rect_pièce_selectionnée = rect_piece_diagonale
                            piece_selectionnée_text = piece_rouge_text
                    
                    if niveau_actuel == 2:
                        if rect_piece_violette.collidepoint(pos): 
                            pièce_selectionnée = position_piece_violette
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 4
                            liste_id.remove(4)
                            rect_pièce_selectionnée = rect_piece_violette
                            piece_selectionnée_text = piece_violette_text
                    
                    if niveau_actuel == 3:
                        if rect_piece_verte.collidepoint(pos): 
                            pièce_selectionnée = position_piece_verte
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 5
                            liste_id.remove(3)
                            rect_pièce_selectionnée = rect_piece_verte
                            piece_selectionnée_text = piece_verte_text
                    
                    if niveau_actuel == 3:
                        if rect_piece_rose.collidepoint(pos):
                            pièce_selectionnée = position_piece_rose
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 6
                            liste_id.remove(4)
                            rect_pièce_selectionnée = rect_piece_rose
                            piece_selectionnée_text = piece_rose_text

    if niveau_actuel == 1:

        screen.blit(images.Plateau_image,(0,0))

        if niveau1_first_launch == True:
            position_piece_non_jouable1 = niveau1_class.emplacement((3,1)) #emplacement d'origine
            position_piece_non_jouable2 = niveau1_class.emplacement((3,5))
            position_piece_diagonale = niveau1_class.emplacement([(1,5),(2,6)])
            position_piece_droite = niveau1_class.emplacement([(1,1),(1,3)])

            rect_piece_droite = images.piece_droite_image.get_rect()
            rect_piece_droite.topleft = (570,165)

            rect_piece_diagonale = images.piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (990,165)
            
            niveau1_class.update_plateau([1,2],[5,6],2,[99,99],[99,99]) #initialisation de la pièce diagonale dans la plateau
            niveau1_class.update_plateau([1,1],[1,3],3,[99,99],[99,99]) #initialisation de la pièce droite dans le plateau
            niveau1_class.update_plateau([3,3],[1,5],1,[99,99],[99,99]) #initialisation des pièces non jouables dans le plateau

            piece_selectionnée_text = font.render("Pas de Pièce sélectionnée", True, (255, 255, 255))
            piece_rose_text = font.render("Pièce rose sélectionnée", True, (255, 255, 255))
            piece_rouge_text = font.render("Pièce rouge sélectionnée", True, (255, 255, 255))

            pièce_selectionnée = False

            niveau1_first_launch = False
        
        screen.blit(images.piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(images.piece_droite_image, rect_piece_droite.topleft)
        screen.blit(images.piece_non_jouable_image,(570,375)) #espace de 210 entre 2 espaces jouables donc 105 pour espace de 1
        screen.blit(images.piece_non_jouable_image,(990,375))
        screen.blit(piece_selectionnée_text,(70,500))
        
        fleche_upleft_button.draw(screen)
        fleche_upright_button.draw(screen)
        fleche_downleft_button.draw(screen)
        fleche_downright_button.draw(screen)
    
    if niveau_actuel == 2:
        screen.blit(images.Plateau_image,(0,0))

        if niveau2_first_launch == True:
            position_piece_non_jouable1 = niveau2_class.emplacement((2,4)) #emplacement d'origine
            position_piece_non_jouable2 = niveau2_class.emplacement((4,0))
            position_piece_diagonale = niveau2_class.emplacement([(3,5),(4,6)])
            position_piece_violette = niveau2_class.emplacement([(1,1),(1,3),(3,3)])

            rect_piece_violette = images.piece_violette_image.get_rect()
            rect_piece_violette.topleft = (570,165) #465 + x*105 et 60 + y*105 du point en haut à gauche

            rect_piece_diagonale = images.piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (990,375)
            
            niveau2_class.update_plateau([3,4],[5,6],2,[99,99],[99,99]) #initialisation de la pièce diagonale dans la plateau
            niveau2_class.update_plateau([1,1,3],[1,3,3],4,[99,99,99],[99,99,99]) #initialisation de la pièce violette dans le plateau
            niveau2_class.update_plateau([2,4],[4,0],1,[99,99],[99,99]) #initialisation des pièces non jouables dans le plateau

            piece_selectionnée_text = font.render("Pas de Pièce sélectionnée", True, (255, 255, 255))
            piece_violette_text = font.render("Pièce violette sélectionnée", True, (255, 255, 255))
            piece_rouge_text = font.render("Pièce rouge sélectionnée", True, (255, 255, 255))

            pièce_selectionnée = False

            niveau2_first_launch = False
        
        screen.blit(images.piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(images.piece_violette_image, rect_piece_violette.topleft)
        screen.blit(images.piece_non_jouable_image,(465,480)) 
        screen.blit(images.piece_non_jouable_image,(885,270))
        screen.blit(piece_selectionnée_text,(70,500))

    pygame.display.update()