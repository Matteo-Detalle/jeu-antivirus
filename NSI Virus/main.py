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

fleche_upleft_button = Button(1250,650,images.fleche_upleft_image,1)
fleche_upright_button = Button(1350,650,images.fleche_upright_image,1)
fleche_downleft_button = Button(1250,750,images.fleche_downleft_image,1)
fleche_downright_button = Button(1350,750,images.fleche_downright_image,1)

recommencer_button = Button(1200,150,images.recommencer_image,1)

niveau1_first_launch = True
niveau2_first_launch = True
niveau3_first_launch = True
niveau4_first_launch = True

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
    regle_texte2 = font.render("Pour ce faire , vous pourrez selectionner une pièce avec la souris et la bouger à l'aide des touches 'a' 'z' 'q' 's' ",True,(255,255,255))
    regle_texte3 = font.render("prenant la direction respective de chaque touche",True,(255,255,255))
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
    global menu_jouer, niveau_actuel, running , menu1

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
        menu_jouer,niveau_actuel = False, 1
    if niveau2_button.pressed():
        menu_jouer,niveau_actuel = False, 2
    if niveau3_button.pressed():
        menu_jouer,niveau_actuel = False, 3
    if niveau4_button.pressed():
        menu_jouer,niveau_actuel = False, 4
    if niveau5_button.pressed():
        menu_jouer,niveau_actuel = False, 5
    if niveau6_button.pressed():
        menu_jouer,niveau_actuel = False, 6
    if niveau7_button.pressed():
        menu_jouer,niveau_actuel = False, 7
    if niveau8_button.pressed():
        menu_jouer,niveau_actuel = False, 8
    if niveau9_button.pressed():
        menu_jouer,niveau_actuel = False, 9
        
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
def niveau1_fonction(direction):
    global pièce_selectionnée , rect_pièce_selectionnée , pièce_id , liste_id , position_piece_diagonale , position_piece_droite , niveau_actuel , menu_jouer , niveau1_first_launch

    if niveau1_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == "GG" and pièce_selectionnée == position_piece_diagonale:
        niveau_actuel , menu_jouer, niveau1_first_launch = 0 , True , True
    elif niveau1_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == False:
        pass
    else:
        new_position = niveau1_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction)
        if pièce_selectionnée == position_piece_diagonale:
            position_piece_diagonale = new_position
        elif pièce_selectionnée == position_piece_droite:
            position_piece_droite = new_position
        pièce_selectionnée = new_position

def niveau2_fonction(direction):
    global pièce_selectionnée , rect_pièce_selectionnée , pièce_id , liste_id , position_piece_diagonale , position_piece_violette , niveau_actuel , menu_jouer , niveau2_first_launch

    if niveau2_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == "GG" and pièce_selectionnée == position_piece_diagonale:
        niveau_actuel , menu_jouer,  niveau2_first_launch = 0 , True , True
    elif niveau2_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == False:
        pass
    else:
        new_position = niveau2_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction)
        if pièce_selectionnée == position_piece_diagonale:
            position_piece_diagonale = new_position
        elif pièce_selectionnée == position_piece_violette:
            position_piece_violette = new_position
        pièce_selectionnée = new_position

def niveau3_fonction(direction):
    global pièce_selectionnée , rect_pièce_selectionnée , pièce_id , liste_id , position_piece_diagonale , position_piece_verte , position_piece_rose, niveau_actuel , menu_jouer ,  niveau3_first_launch

    if niveau3_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == "GG" and pièce_selectionnée == position_piece_diagonale:
        niveau_actuel , menu_jouer,  niveau3_first_launch = 0 , True , True
    elif niveau3_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == False:
        pass
    else:
        new_position = niveau3_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction)
        if pièce_selectionnée == position_piece_diagonale:
            position_piece_diagonale = new_position
        elif pièce_selectionnée == position_piece_verte:
            position_piece_verte = new_position
        elif pièce_selectionnée == position_piece_rose:
            position_piece_rose = new_position
        pièce_selectionnée = new_position

def niveau4_fonction(direction):
    global pièce_selectionnée , rect_pièce_selectionnée , pièce_id , liste_id , position_piece_diagonale , position_piece_violette2 , position_piece_rose ,position_piece_bleu , niveau_actuel , menu_jouer ,  niveau4_first_launch
    if niveau4_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == "GG" and pièce_selectionnée == position_piece_diagonale:
        niveau_actuel , menu_jouer,  niveau4_first_launch = 0 , True , True
    elif niveau4_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == False:
        pass    
    else:
        new_position = niveau4_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction)
        if pièce_selectionnée == position_piece_diagonale:
            position_piece_diagonale = new_position
        elif pièce_selectionnée == position_piece_violette2:
            position_piece_violette2 = new_position
        elif pièce_selectionnée == position_piece_rose:
            position_piece_rose = new_position
        elif pièce_selectionnée == position_piece_bleu:
            position_piece_bleu = new_position
        pièce_selectionnée = new_position

while running:
    screen.blit(images.background, (0,0))
    horloge.tick(fps)

    if menu1 == True:
        menu1_fonction()
    elif menu_explication == True:
        menu_explication_fonction()
    elif menu_jouer == True:
        menu_jouer_fonction()

    if niveau_actuel == 1:

        screen.blit(images.Plateau_image,(0,0))

        if niveau1_first_launch == True:
            niveau1_class.plateau = [[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0]]
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
            rect_pièce_selectionnée = False
            pièce_id = False
            liste_id = False

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

        if fleche_upleft_button.pressed():
            niveau1_fonction("upleft")
        if fleche_upright_button.pressed():
            niveau1_fonction("upright")
        if fleche_downleft_button.pressed():
            niveau1_fonction("downleft")
        if fleche_downright_button.pressed():
            niveau1_fonction("downright")

        recommencer_button.draw(screen)
        if recommencer_button.pressed():
            niveau1_first_launch = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer , niveau1_first_launch = 0 , True , True

                if event.key == pygame.K_a:
                    niveau1_fonction("upleft")
                if event.key == pygame.K_s:
                    niveau1_fonction("downright")
                if event.key == pygame.K_z:
                    niveau1_fonction("upright")
                if event.key == pygame.K_q:
                    niveau1_fonction("downleft")

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
    
    elif niveau_actuel == 2:
        screen.blit(images.Plateau_image,(0,0))

        if niveau2_first_launch == True:
            niveau2_class.plateau = [[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0]]
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
            rect_pièce_selectionnée = False
            pièce_id = False
            liste_id = False

            niveau2_first_launch = False
        
        screen.blit(images.piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(images.piece_violette_image, rect_piece_violette.topleft)
        screen.blit(images.piece_non_jouable_image,(465,480)) 
        screen.blit(images.piece_non_jouable_image,(885,270))
        screen.blit(piece_selectionnée_text,(70,500))

        fleche_upleft_button.draw(screen)
        fleche_upright_button.draw(screen)
        fleche_downleft_button.draw(screen)
        fleche_downright_button.draw(screen)

        if fleche_upleft_button.pressed():
            niveau2_fonction("upleft")
        if fleche_upright_button.pressed():
            niveau2_fonction("upright")
        if fleche_downleft_button.pressed():
            niveau2_fonction("downleft")
        if fleche_downright_button.pressed():
            niveau2_fonction("downright")
        
        recommencer_button.draw(screen)
        if recommencer_button.pressed():
            niveau2_first_launch = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer , niveau2_first_launch = 0 , True , True

                if event.key == pygame.K_a:
                    niveau2_fonction("upleft")
                if event.key == pygame.K_s:
                    niveau2_fonction("downright")
                if event.key == pygame.K_z:
                    niveau2_fonction("upright")
                if event.key == pygame.K_q:
                    niveau2_fonction("downleft")

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

    elif niveau_actuel == 3:
        screen.blit(images.Plateau_image,(0,0))

        if niveau3_first_launch == True:
            niveau3_class.plateau = [[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0]]
            position_piece_non_jouable1 = niveau3_class.emplacement((4,0)) #emplacement d'origine (y,x)
            position_piece_non_jouable2 = niveau3_class.emplacement((3,3))
            position_piece_diagonale = niveau3_class.emplacement([(0,4),(1,5)])
            position_piece_verte = niveau3_class.emplacement([(2,2),(2,4)])
            position_piece_rose = niveau3_class.emplacement([(0,6),(2,6)])

            rect_piece_verte = images.piece_verte_image.get_rect()
            rect_piece_verte.topleft = (675,270) #465 + x*105 et 60 + y*105 du point en haut à gauche

            rect_piece_diagonale = images.piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (885,60)

            rect_piece_rose = images.piece_rose_image.get_rect()
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
            rect_pièce_selectionnée = False
            pièce_id = False
            liste_id = False

            niveau3_first_launch = False
        
        screen.blit(images.piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(images.piece_verte_image, rect_piece_verte.topleft)
        screen.blit(images.piece_rose_image, rect_piece_rose.topleft)
        screen.blit(images.piece_non_jouable_image,(465,480)) 
        screen.blit(images.piece_non_jouable_image,(780,375))
        screen.blit(piece_selectionnée_text,(70,500))

        fleche_upleft_button.draw(screen)
        fleche_upright_button.draw(screen)
        fleche_downleft_button.draw(screen)
        fleche_downright_button.draw(screen)

        if fleche_upleft_button.pressed():
            niveau3_fonction("upleft")
        if fleche_upright_button.pressed():
            niveau3_fonction("upright")
        if fleche_downleft_button.pressed():
            niveau3_fonction("downleft")
        if fleche_downright_button.pressed():
            niveau3_fonction("downright")
        
        recommencer_button.draw(screen)
        if recommencer_button.pressed():
            niveau3_first_launch = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer , niveau3_first_launch = 0 , True , True

                if event.key == pygame.K_a:
                    niveau3_fonction("upleft")
                if event.key == pygame.K_s:
                    niveau3_fonction("downright")
                if event.key == pygame.K_z:
                    niveau3_fonction("upright")
                if event.key == pygame.K_q:
                    niveau3_fonction("downleft")

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
    
    elif niveau_actuel == 4:
        screen.blit(images.Plateau_image,(0,0))

        if niveau4_first_launch == True:
            niveau4_class.plateau = [[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0]]
            position_piece_violette2 = niveau4_class.emplacement([(0,0),(0,2),(2,0)]) #emplacement d'origine (y,x)
            position_piece_diagonale = niveau4_class.emplacement([(5,1),(6,2)])
            position_piece_bleu = niveau4_class.emplacement([(3,1),(4,2)])
            position_piece_rose = niveau4_class.emplacement([(4,4),(6,4)])

            rect_piece_violette2 = images.piece_violette2_image.get_rect()
            rect_piece_violette2.topleft = (465,60) #465 + x*105 et 60 + y*105 du point en haut à gauche

            rect_piece_bleu = images.piece_bleu_image.get_rect()
            rect_piece_bleu.topleft = (570,375)

            rect_piece_diagonale = images.piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (580,585)

            rect_piece_rose = images.piece_rose_image.get_rect()
            rect_piece_rose.topleft = (885,480)
            
            niveau4_class.update_plateau([0,0,2],[0,2,0],5,[99,99,99],[99,99,99]) #initialisation de la pièce violette2 dans la plateau
            niveau4_class.update_plateau([5,6],[1,2],2,[99,99],[99,99]) #initialisation de la pièce diagonale dans le plateau
            niveau4_class.update_plateau([3,4],[1,2],3,[99,99],[99,99]) #initialisation de la pièce bleu dans le plateau
            niveau4_class.update_plateau([4,6],[4,4],4,[99,99],[99,99]) #initialisation de la pièce rose dans le plateau

            piece_selectionnée_text = font.render("Pas de Pièce sélectionnée",True,(255,255,255))
            piece_rose_text = font.render("Pièce rose sélectionnée",True,(255,255,255))
            piece_rouge_text = font.render("Pièce rouge sélectionnée",True,(255,255,255))
            piece_violette_text = font.render("Pièce violette sélectionnée",True,(255,255,255))
            piece_bleu_text = font.render("Pièce bleu selectionée",True,(255,255,255))

            pièce_selectionnée = False
            rect_pièce_selectionnée = False
            pièce_id = False
            liste_id = False

            niveau4_first_launch = False
        
        screen.blit(images.piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(images.piece_violette2_image, rect_piece_violette2.topleft)
        screen.blit(images.piece_rose_image, rect_piece_rose.topleft)
        screen.blit(images.piece_bleu_image, rect_piece_bleu)
        screen.blit(piece_selectionnée_text,(70,500))

        fleche_upleft_button.draw(screen)
        fleche_upright_button.draw(screen)
        fleche_downleft_button.draw(screen)
        fleche_downright_button.draw(screen)

        if fleche_upleft_button.pressed():
            niveau4_fonction("upleft")
        if fleche_upright_button.pressed():
            niveau4_fonction("upright")
        if fleche_downleft_button.pressed():
            niveau4_fonction("downleft")
        if fleche_downright_button.pressed():
            niveau4_fonction("downright")
        
        recommencer_button.draw(screen)
        if recommencer_button.pressed():
            niveau4_first_launch = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer , niveau4_first_launch = 0 , True , True
                
                if event.key == pygame.K_a:
                    niveau4_fonction("upleft")
                if event.key == pygame.K_s:
                    niveau4_fonction("downright")
                if event.key == pygame.K_z:
                    niveau4_fonction("upright")
                if event.key == pygame.K_q:
                    niveau4_fonction("downleft")

            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  #vérifie si clique gauche
                    pos = pygame.mouse.get_pos() 

                    #vérifie sur quelle pièce le clique a été fait
                    if rect_piece_violette2.collidepoint(pos): 
                        pièce_selectionnée = position_piece_violette2
                        liste_id = [2,3,4,5,6,7,8,9]
                        pièce_id = 5
                        liste_id.remove(5)
                        rect_pièce_selectionnée = rect_piece_violette2
                        piece_selectionnée_text = piece_violette_text

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
                    
                    elif rect_piece_bleu.collidepoint(pos):
                        pièce_selectionnée = position_piece_bleu
                        liste_id = [2,3,4,5,6,7,8,9]
                        pièce_id = 3
                        liste_id.remove(3)
                        rect_pièce_selectionnée = rect_piece_bleu
                        piece_selectionnée_text = piece_bleu_text
   
    elif niveau_actuel == 5:
        screen.blit(images.Plateau_image,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer = 0 , True
    
    elif niveau_actuel == 6:
        screen.blit(images.Plateau_image,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer = 0 , True
    
    elif niveau_actuel == 7:
        screen.blit(images.Plateau_image,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer = 0 , True
    
    elif niveau_actuel == 8:
        screen.blit(images.Plateau_image,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer = 0 , True
    
    elif niveau_actuel == 9:
        screen.blit(images.Plateau_image,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer = 0 , True
        
    pygame.display.update()