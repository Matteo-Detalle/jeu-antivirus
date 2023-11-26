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

niveau1_class, niveau2_class, niveau3_class, niveau4_class, niveau5_class, niveau6_class, niveau7_class, niveau8_class =  Niveau(), Niveau(), Niveau(), Niveau(), Niveau(), Niveau(), Niveau(), Niveau()

images = Image()

Regle_button = Button(600,350,images.boutton_regle_image,1)
Quitter_button = Button(600,600,images.boutton_quitter_image,1)
Jouer_button = Button(600,100,images.boutton_jouer_image,1)
fleche_volume_gauche_button = Button(170,100,images.fleche_volume_gauche_image,1)
fleche_volume_droite_button = Button(330,100,images.fleche_volume_droite_image,1)

niveau1_button = Button(450,250,images.niveau1_image,1)
niveau2_button = Button(600,250,images.niveau2_image,1)
niveau3_button = Button(750,250,images.niveau3_image,1)
niveau4_button = Button(900,250,images.niveau4_image,1)
niveau5_button = Button(450,500,images.niveau5_image,1)
niveau6_button = Button(600,500,images.niveau6_image,1)
niveau7_button = Button(750,500,images.niveau7_image,1)
niveau8_button = Button(900,500,images.niveau8_image,1)

fleche_upleft_button = Button(1250,650,images.fleche_upleft_image,1)
fleche_upright_button = Button(1350,650,images.fleche_upright_image,1)
fleche_downleft_button = Button(1250,750,images.fleche_downleft_image,1)
fleche_downright_button = Button(1350,750,images.fleche_downright_image,1)

recommencer_button = Button(1200,150,images.recommencer_image,1)

Buttons = [Regle_button,Quitter_button,Jouer_button,fleche_volume_gauche_button,fleche_volume_droite_button,niveau1_button,niveau2_button,niveau3_button,niveau4_button,niveau5_button,niveau6_button,niveau7_button,niveau8_button,fleche_upleft_button,fleche_upright_button,fleche_downleft_button,fleche_downright_button]

niveau1_first_launch,niveau2_first_launch,niveau3_first_launch,niveau4_first_launch,niveau5_first_launch,niveau6_first_launch,niveau7_first_launch,niveau8_first_launch = True,True,True,True,True,True,True,True

font = pygame.font.Font(None, 36)
echap_text = font.render("Appuyez sur Echap pour revenir en arrière",True,(255,255,255))

volume = 0.5
volume_text = font.render(f"Volume: {int(volume * 100)}", True, (255, 255, 255))

pygame.mixer.music.load("assets/musique.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(volume)

def menu1_fonction():
    global menu1, menu_explication, menu_jouer , running , volume , Buttons , volume_text

    Regle_button.draw(screen)
    Quitter_button.draw(screen)
    Jouer_button.draw(screen)
    fleche_volume_gauche_button.draw(screen)
    fleche_volume_droite_button.draw(screen)

    screen.blit(volume_text,(240,80))

    if fleche_volume_gauche_button.pressed():
        if volume - 0.1 < 0:
            pass
        else:
            volume -= 0.1
            pygame.mixer.music.set_volume(volume)
            for i in Buttons:
                i.son.set_volume(volume)
            volume_text = font.render(f"Volume: {int(volume * 100)}", True, (255, 255, 255))
            
    
    if fleche_volume_droite_button.pressed():
        if volume + 0.1 > 1:
            pass
        else:
            volume += 0.1
            pygame.mixer.music.set_volume(volume)
            for i in Buttons:
                i.son.set_volume(volume)
            volume_text = font.render(f"Volume: {int(volume * 100)}", True, (255, 255, 255))

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

def niveau5_fonction(direction):
    global pièce_selectionnée , rect_pièce_selectionnée , pièce_id , liste_id , position_piece_diagonale , position_piece_violette  ,position_piece_bleu2 , niveau_actuel , menu_jouer ,  niveau5_first_launch
    if niveau5_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == "GG" and pièce_selectionnée == position_piece_diagonale:
        niveau_actuel , menu_jouer,  niveau5_first_launch = 0 , True , True
    elif niveau5_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == False:
        pass    
    else:
        new_position = niveau5_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction)
        if pièce_selectionnée == position_piece_diagonale:
            position_piece_diagonale = new_position
        elif pièce_selectionnée == position_piece_violette:
            position_piece_violette = new_position
        elif pièce_selectionnée == position_piece_bleu2:
            position_piece_bleu2 = new_position
        pièce_selectionnée = new_position

def niveau6_fonction(direction):
    global pièce_selectionnée , rect_pièce_selectionnée , pièce_id , liste_id , position_piece_diagonale , position_piece_violette3  ,position_piece_bleu , position_piece_orange , niveau_actuel , menu_jouer ,  niveau6_first_launch
    if niveau6_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == "GG" and pièce_selectionnée == position_piece_diagonale:
        niveau_actuel , menu_jouer,  niveau6_first_launch = 0 , True , True
    elif niveau6_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == False:
        pass    
    else:
        new_position = niveau6_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction)
        if pièce_selectionnée == position_piece_diagonale:
            position_piece_diagonale = new_position
        elif pièce_selectionnée == position_piece_violette3:
            position_piece_violette3 = new_position
        elif pièce_selectionnée == position_piece_bleu:
            position_piece_bleu = new_position
        elif pièce_selectionnée == position_piece_orange:
            position_piece_orange = new_position
        pièce_selectionnée = new_position

def niveau7_fonction(direction):
    global pièce_selectionnée , rect_pièce_selectionnée , pièce_id , liste_id , position_piece_diagonale , position_piece_violette2  ,position_piece_rose , position_piece_jaune , niveau_actuel , menu_jouer ,  niveau7_first_launch
    if niveau7_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == "GG" and pièce_selectionnée == position_piece_diagonale:
        niveau_actuel , menu_jouer,  niveau7_first_launch = 0 , True , True
    elif niveau7_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == False:
        pass    
    else:
        new_position = niveau7_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction)
        if pièce_selectionnée == position_piece_diagonale:
            position_piece_diagonale = new_position
        elif pièce_selectionnée == position_piece_violette2:
            position_piece_violette2 = new_position
        elif pièce_selectionnée == position_piece_rose:
            position_piece_rose = new_position
        elif pièce_selectionnée == position_piece_jaune:
            position_piece_jaune = new_position
        pièce_selectionnée = new_position

def niveau8_fonction(direction):
    global pièce_selectionnée , rect_pièce_selectionnée , pièce_id , liste_id , position_piece_diagonale, position_piece_droite , position_piece_jaune , niveau_actuel , menu_jouer ,  niveau8_first_launch
    if niveau8_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == "GG" and pièce_selectionnée == position_piece_diagonale:
        niveau_actuel , menu_jouer,  niveau8_first_launch = 0 , True , True
    elif niveau8_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction) == False:
        pass    
    else:
        new_position = niveau8_class.mouvement(pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id,direction)
        if pièce_selectionnée == position_piece_diagonale:
            position_piece_diagonale = new_position
        elif pièce_selectionnée == position_piece_droite:
            position_piece_droite = new_position
        elif pièce_selectionnée == position_piece_jaune:
            position_piece_jaune = new_position
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
                        if images.mask_droite.get_at((pos[0] - rect_piece_droite.x, pos[1] - rect_piece_droite.y)):  
                            pièce_selectionnée = position_piece_droite
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 3
                            liste_id.remove(3)
                            rect_pièce_selectionnée = rect_piece_droite
                            piece_selectionnée_text = piece_rose_text

                    elif rect_piece_diagonale.collidepoint(pos):
                        if images.mask_diagonale.get_at((pos[0] - rect_piece_diagonale.x, pos[1] - rect_piece_diagonale.y)):  
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

                    if rect_piece_diagonale.collidepoint(pos):
                        if images.mask_diagonale.get_at((pos[0] - rect_piece_diagonale.x, pos[1] - rect_piece_diagonale.y)): 
                            pièce_selectionnée = position_piece_diagonale
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 2
                            liste_id.remove(2)
                            rect_pièce_selectionnée = rect_piece_diagonale
                            piece_selectionnée_text = piece_rouge_text
                    
                    elif rect_piece_violette.collidepoint(pos):
                        if images.mask_violette.get_at((pos[0] - rect_piece_violette.x, pos[1] - rect_piece_violette.y)): 
                            pièce_selectionnée = position_piece_violette
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 3
                            liste_id.remove(3)
                            rect_pièce_selectionnée = rect_piece_violette
                            piece_selectionnée_text = piece_violette_text

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
                        if images.mask_verte.get_at((pos[0] - rect_piece_verte.x, pos[1] - rect_piece_verte.y)): 
                            pièce_selectionnée = position_piece_verte
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 3
                            liste_id.remove(3)
                            rect_pièce_selectionnée = rect_piece_verte
                            piece_selectionnée_text = piece_verte_text

                    elif rect_piece_diagonale.collidepoint(pos):
                        if images.mask_diagonale.get_at((pos[0] - rect_piece_diagonale.x, pos[1] - rect_piece_diagonale.y)): 
                            pièce_selectionnée = position_piece_diagonale
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 2
                            liste_id.remove(2)
                            rect_pièce_selectionnée = rect_piece_diagonale
                            piece_selectionnée_text = piece_rouge_text
                    
                    elif rect_piece_rose.collidepoint(pos):
                        if images.mask_rose.get_at((pos[0] - rect_piece_rose.x, pos[1] - rect_piece_rose.y)): 
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

                    if rect_piece_diagonale.collidepoint(pos):
                        if images.mask_diagonale.get_at((pos[0] - rect_piece_diagonale.x, pos[1] - rect_piece_diagonale.y)): 
                            pièce_selectionnée = position_piece_diagonale
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 2
                            liste_id.remove(2)
                            rect_pièce_selectionnée = rect_piece_diagonale
                            piece_selectionnée_text = piece_rouge_text
                    
                    elif rect_piece_rose.collidepoint(pos):
                        if images.mask_rose.get_at((pos[0] - rect_piece_rose.x, pos[1] - rect_piece_rose.y)): 
                            pièce_selectionnée = position_piece_rose
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 4
                            liste_id.remove(4)
                            rect_pièce_selectionnée = rect_piece_rose
                            piece_selectionnée_text = piece_rose_text
                    
                    elif rect_piece_bleu.collidepoint(pos):
                        if images.mask_bleu.get_at((pos[0] - rect_piece_bleu.x, pos[1] - rect_piece_bleu.y)): 
                            pièce_selectionnée = position_piece_bleu
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 3
                            liste_id.remove(3)
                            rect_pièce_selectionnée = rect_piece_bleu
                            piece_selectionnée_text = piece_bleu_text
                    
                    if rect_piece_violette2.collidepoint(pos):
                        if images.mask_violette2.get_at((pos[0] - rect_piece_violette2.x, pos[1] - rect_piece_violette2.y)): 
                            pièce_selectionnée = position_piece_violette2
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 5
                            liste_id.remove(5)
                            rect_pièce_selectionnée = rect_piece_violette2
                            piece_selectionnée_text = piece_violette_text
   
    elif niveau_actuel == 5:
        screen.blit(images.Plateau_image,(0,0))

        if niveau5_first_launch == True:
            niveau5_class.plateau = [[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0]]
            position_piece_bleu2 = niveau5_class.emplacement([(0,0),(0,2),(0,4)]) #emplacement d'origine (y,x)
            position_piece_violette = niveau5_class.emplacement([(2,2),(2,4),(4,4)])
            position_piece_diagonale = niveau5_class.emplacement([(4,0),(5,1)])
            position_piece_non_jouable = niveau5_class.emplacement([(3,5)])

            rect_piece_bleu2 = images.piece_bleu2_image.get_rect()
            rect_piece_bleu2.topleft = (465,60) #465 + x*105 et 60 + y*105 du point en haut à gauche

            rect_piece_violette = images.piece_violette_image.get_rect()
            rect_piece_violette.topleft = (675,280)

            rect_piece_diagonale = images.piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (465,480)
            
            niveau5_class.update_plateau([0,0,0],[0,2,4],3,[99,99,99],[99,99,99]) #initialisation de la pièce bleu2 dans la plateau
            niveau5_class.update_plateau([4,5],[0,1],2,[99,99],[99,99]) #initialisation de la pièce diagonale dans le plateau
            niveau5_class.update_plateau([2,2,4],[2,4,4],4,[99,99,99],[99,99,99]) #initialisation de la pièce violette dans le plateau
            niveau5_class.update_plateau([3],[5],1,[99],[99]) #initialisation de la pièce non jouable dans le plateau

            piece_selectionnée_text = font.render("Pas de Pièce sélectionnée",True,(255,255,255))
            piece_rouge_text = font.render("Pièce rouge sélectionnée",True,(255,255,255))
            piece_violette_text = font.render("Pièce violette sélectionnée",True,(255,255,255))
            piece_bleu2_text = font.render("Pièce bleu selectionée",True,(255,255,255))

            pièce_selectionnée = False
            rect_pièce_selectionnée = False
            pièce_id = False
            liste_id = False

            niveau5_first_launch = False
        
        screen.blit(images.piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(images.piece_violette_image, rect_piece_violette.topleft)
        screen.blit(images.piece_bleu2_image, rect_piece_bleu2)
        screen.blit(images.piece_non_jouable_image,(990,375))
        screen.blit(piece_selectionnée_text,(70,500))

        fleche_upleft_button.draw(screen)
        fleche_upright_button.draw(screen)
        fleche_downleft_button.draw(screen)
        fleche_downright_button.draw(screen)

        if fleche_upleft_button.pressed():
            niveau5_fonction("upleft")
        if fleche_upright_button.pressed():
            niveau5_fonction("upright")
        if fleche_downleft_button.pressed():
            niveau5_fonction("downleft")
        if fleche_downright_button.pressed():
            niveau5_fonction("downright")
        
        recommencer_button.draw(screen)
        if recommencer_button.pressed():
            niveau5_first_launch = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer , niveau5_first_launch = 0 , True , True
                
                if event.key == pygame.K_a:
                    niveau5_fonction("upleft")
                if event.key == pygame.K_s:
                    niveau5_fonction("downright")
                if event.key == pygame.K_z:
                    niveau5_fonction("upright")
                if event.key == pygame.K_q:
                    niveau5_fonction("downleft")

            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  #vérifie si clique gauche
                    pos = pygame.mouse.get_pos() 

                    #vérifie sur quelle pièce le clique a été fait

                    if rect_piece_diagonale.collidepoint(pos):
                        if images.mask_diagonale.get_at((pos[0] - rect_piece_diagonale.x, pos[1] - rect_piece_diagonale.y)): 
                            pièce_selectionnée = position_piece_diagonale
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 2
                            liste_id.remove(2)
                            rect_pièce_selectionnée = rect_piece_diagonale
                            piece_selectionnée_text = piece_rouge_text
                
                    elif rect_piece_bleu2.collidepoint(pos):
                        if images.mask_bleu2.get_at((pos[0] - rect_piece_bleu2.x, pos[1] - rect_piece_bleu2.y)): 
                            pièce_selectionnée = position_piece_bleu2
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 3
                            liste_id.remove(3)
                            rect_pièce_selectionnée = rect_piece_bleu2
                            piece_selectionnée_text = piece_bleu2_text
                    
                    elif rect_piece_violette.collidepoint(pos):
                        if images.mask_violette.get_at((pos[0] - rect_piece_violette.x, pos[1] - rect_piece_violette.y)): 
                            pièce_selectionnée = position_piece_violette
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 4
                            liste_id.remove(4)
                            rect_pièce_selectionnée = rect_piece_violette
                            piece_selectionnée_text = piece_violette_text
        
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

        if niveau6_first_launch == True:
            niveau6_class.plateau = [[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0]]
            position_piece_bleu = niveau6_class.emplacement([(1,1),(2,2)]) #emplacement d'origine (y,x)
            position_piece_violette3 = niveau6_class.emplacement([(2,0),(4,0),(4,2)])
            position_piece_diagonale = niveau6_class.emplacement([(3,5),(4,6)])
            position_piece_orange = niveau6_class.emplacement([(1,3),(2,4),(3,3)])
            position_piece_non_jouable1 = niveau6_class.emplacement([(1,5)])
            position_piece_non_jouable2 = niveau6_class.emplacement([(5,1)])

            rect_piece_bleu = images.piece_bleu_image.get_rect()
            rect_piece_bleu.topleft = (570,165) #465 + x*105 et 60 + y*105 du point en haut à gauche

            rect_piece_violette3 = images.piece_violette3_image.get_rect()
            rect_piece_violette3.topleft = (465,280)

            rect_piece_diagonale = images.piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (990,375)

            rect_piece_orange = images.piece_orange_image.get_rect()
            rect_piece_orange.topleft = (780,165)
            
            niveau6_class.update_plateau([1,2],[1,2],3,[99,99],[99,99]) #initialisation de la pièce bleu dans la plateau
            niveau6_class.update_plateau([3,4],[5,6],2,[99,99],[99,99]) #initialisation de la pièce diagonale dans le plateau
            niveau6_class.update_plateau([2,4,4],[0,0,2],4,[99,99,99],[99,99,99]) #initialisation de la pièce violette3 dans le plateau
            niveau6_class.update_plateau([1,2,3],[3,4,3],5,[99,99,99],[99,99,99]) #initialisation de la pièce orange dans le plateau
            niveau6_class.update_plateau([1,5],[5,1],1,[99,99],[99,99]) #initialisation des pièces non jouables dans le plateau

            piece_selectionnée_text = font.render("Pas de Pièce sélectionnée",True,(255,255,255))
            piece_rouge_text = font.render("Pièce rouge sélectionnée",True,(255,255,255))
            piece_violette_text = font.render("Pièce violette sélectionnée",True,(255,255,255))
            piece_bleu_text = font.render("Pièce bleu selectionée",True,(255,255,255))
            piece_orange_text = font.render("Pièce orange selectionée",True,(255,255,255))

            pièce_selectionnée = False
            rect_pièce_selectionnée = False
            pièce_id = False
            liste_id = False

            niveau6_first_launch = False
        
        screen.blit(images.piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(images.piece_violette3_image, rect_piece_violette3.topleft)
        screen.blit(images.piece_bleu_image, rect_piece_bleu)
        screen.blit(images.piece_orange_image, rect_piece_orange)
        screen.blit(images.piece_non_jouable_image,(990,170))
        screen.blit(images.piece_non_jouable_image,(570,570))
        screen.blit(piece_selectionnée_text,(70,500))

        fleche_upleft_button.draw(screen)
        fleche_upright_button.draw(screen)
        fleche_downleft_button.draw(screen)
        fleche_downright_button.draw(screen)

        if fleche_upleft_button.pressed():
            niveau6_fonction("upleft")
        if fleche_upright_button.pressed():
            niveau6_fonction("upright")
        if fleche_downleft_button.pressed():
            niveau6_fonction("downleft")
        if fleche_downright_button.pressed():
            niveau6_fonction("downright")
        
        recommencer_button.draw(screen)
        if recommencer_button.pressed():
            niveau6_first_launch = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer , niveau6_first_launch = 0 , True , True
                
                if event.key == pygame.K_a:
                    niveau6_fonction("upleft")
                if event.key == pygame.K_s:
                    niveau6_fonction("downright")
                if event.key == pygame.K_z:
                    niveau6_fonction("upright")
                if event.key == pygame.K_q:
                    niveau6_fonction("downleft")

            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  #vérifie si clique gauche
                    pos = pygame.mouse.get_pos() 

                    #vérifie sur quelle pièce le clique a été fait

                    if rect_piece_diagonale.collidepoint(pos):
                        if images.mask_diagonale.get_at((pos[0] - rect_piece_diagonale.x, pos[1] - rect_piece_diagonale.y)): 
                            pièce_selectionnée = position_piece_diagonale
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 2
                            liste_id.remove(2)
                            rect_pièce_selectionnée = rect_piece_diagonale
                            piece_selectionnée_text = piece_rouge_text
                
                    elif rect_piece_bleu.collidepoint(pos):
                        if images.mask_bleu.get_at((pos[0] - rect_piece_bleu.x, pos[1] - rect_piece_bleu.y)): 
                            pièce_selectionnée = position_piece_bleu
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 3
                            liste_id.remove(3)
                            rect_pièce_selectionnée = rect_piece_bleu
                            piece_selectionnée_text = piece_bleu_text

                    elif rect_piece_orange.collidepoint(pos):
                        if images.mask_orange.get_at((pos[0] - rect_piece_orange.x, pos[1] - rect_piece_orange.y)): 
                            pièce_selectionnée = position_piece_orange
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 5
                            liste_id.remove(5)
                            rect_pièce_selectionnée = rect_piece_orange
                            piece_selectionnée_text = piece_orange_text
                    
                    elif rect_piece_violette3.collidepoint(pos):
                        if images.mask_violette3.get_at((pos[0] - rect_piece_violette3.x, pos[1] - rect_piece_violette3.y)):
                            pièce_selectionnée = position_piece_violette3
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 4
                            liste_id.remove(4)
                            rect_pièce_selectionnée = rect_piece_violette3
                            piece_selectionnée_text = piece_violette_text
        
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

        if niveau7_first_launch == True:
            niveau7_class.plateau = [[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0]]
            position_piece_rose = niveau7_class.emplacement([(0,0),(2,0)]) #emplacement d'origine (y,x)
            position_piece_violette2 = niveau7_class.emplacement([(1,1),(1,3),(3,1)])
            position_piece_diagonale = niveau7_class.emplacement([(2,2),(3,3)])
            position_piece_jaune = niveau7_class.emplacement([(2,4),(4,4),(5,5)])
            position_piece_non_jouable1 = niveau7_class.emplacement([(1,5)])
            position_piece_non_jouable2 = niveau7_class.emplacement([(4,6)])

            rect_piece_rose = images.piece_rose_image.get_rect()
            rect_piece_rose.topleft = (465,60) #465 + x*105 et 60 + y*105 du point en haut à gauche

            rect_piece_violette2 = images.piece_violette2_image.get_rect()
            rect_piece_violette2.topleft = (570,175)

            rect_piece_diagonale = images.piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (675,270)

            rect_piece_jaune = images.piece_jaune_image.get_rect()
            rect_piece_jaune.topleft = (885,270)
            
            niveau7_class.update_plateau([0,2],[0,0],3,[99,99],[99,99]) #initialisation de la pièce rose dans la plateau
            niveau7_class.update_plateau([2,3],[2,3],2,[99,99],[99,99]) #initialisation de la pièce diagonale dans le plateau
            niveau7_class.update_plateau([1,1,3],[1,3,1],4,[99,99,99],[99,99,99]) #initialisation de la pièce violette2 dans le plateau
            niveau7_class.update_plateau([2,4,5],[4,4,5],5,[99,99,99],[99,99,99]) #initialisation de la pièce jaune dans le plateau
            niveau7_class.update_plateau([1,4],[5,6],1,[99,99],[99,99]) #initialisation des pièces non jouables dans le plateau

            piece_selectionnée_text = font.render("Pas de Pièce sélectionnée",True,(255,255,255))
            piece_rouge_text = font.render("Pièce rouge sélectionnée",True,(255,255,255))
            piece_violette_text = font.render("Pièce violette sélectionnée",True,(255,255,255))
            piece_rose_text = font.render("Pièce rose selectionée",True,(255,255,255))
            piece_jaune_text = font.render("Pièce jaune selectionée",True,(255,255,255))

            pièce_selectionnée = False
            rect_pièce_selectionnée = False
            pièce_id = False
            liste_id = False

            niveau7_first_launch = False
        
        screen.blit(images.piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(images.piece_violette2_image, rect_piece_violette2.topleft)
        screen.blit(images.piece_rose_image, rect_piece_rose)
        screen.blit(images.piece_jaune_image, rect_piece_jaune)
        screen.blit(images.piece_non_jouable_image,(990,170))
        screen.blit(images.piece_non_jouable_image,(1095,480))
        screen.blit(piece_selectionnée_text,(70,500))

        fleche_upleft_button.draw(screen)
        fleche_upright_button.draw(screen)
        fleche_downleft_button.draw(screen)
        fleche_downright_button.draw(screen)

        if fleche_upleft_button.pressed():
            niveau7_fonction("upleft")
        if fleche_upright_button.pressed():
            niveau7_fonction("upright")
        if fleche_downleft_button.pressed():
            niveau7_fonction("downleft")
        if fleche_downright_button.pressed():
            niveau7_fonction("downright")
        
        recommencer_button.draw(screen)
        if recommencer_button.pressed():
            niveau7_first_launch = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer , niveau7_first_launch = 0 , True , True
                
                if event.key == pygame.K_a:
                    niveau7_fonction("upleft")
                if event.key == pygame.K_s:
                    niveau7_fonction("downright")
                if event.key == pygame.K_z:
                    niveau7_fonction("upright")
                if event.key == pygame.K_q:
                    niveau7_fonction("downleft")

            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  #vérifie si clique gauche
                    pos = pygame.mouse.get_pos() 

                    #vérifie sur quelle pièce le clique a été fait
                    if rect_piece_diagonale.collidepoint(pos):
                        if images.mask_diagonale.get_at((pos[0] - rect_piece_diagonale.x, pos[1] - rect_piece_diagonale.y)): 
                            pièce_selectionnée = position_piece_diagonale
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 2
                            liste_id.remove(2)
                            rect_pièce_selectionnée = rect_piece_diagonale
                            piece_selectionnée_text = piece_rouge_text

                    elif rect_piece_rose.collidepoint(pos):
                        if images.mask_rose.get_at((pos[0] - rect_piece_rose.x, pos[1] - rect_piece_rose.y)): 
                            pièce_selectionnée = position_piece_rose
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 3
                            liste_id.remove(3)
                            rect_pièce_selectionnée = rect_piece_rose
                            piece_selectionnée_text = piece_rose_text

                    elif rect_piece_jaune.collidepoint(pos):
                        if images.mask_jaune.get_at((pos[0] - rect_piece_jaune.x, pos[1] - rect_piece_jaune.y)): 
                            pièce_selectionnée = position_piece_jaune
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 5
                            liste_id.remove(5)
                            rect_pièce_selectionnée = rect_piece_jaune
                            piece_selectionnée_text = piece_jaune_text
                    
                    elif rect_piece_violette2.collidepoint(pos):
                        if images.mask_violette2.get_at((pos[0] - rect_piece_violette2.x, pos[1] - rect_piece_violette2.y)):
                            pièce_selectionnée = position_piece_violette2
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 4
                            liste_id.remove(4)
                            rect_pièce_selectionnée = rect_piece_violette2
                            piece_selectionnée_text = piece_violette_text
        
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

        if niveau8_first_launch == True:
            niveau8_class.plateau = [[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0],[1,0,1,0,1,0,1],[0,1,0,1,0,1,0]]
            position_piece_droite = niveau8_class.emplacement([(2,0),(2,2)]) #emplacement d'origine (y,x)
            position_piece_diagonale = niveau8_class.emplacement([(5,5),(6,6)])
            position_piece_jaune = niveau8_class.emplacement([(3,3),(5,3),(6,4)])
            position_piece_non_jouable1 = niveau8_class.emplacement([(4,0)])
            position_piece_non_jouable2 = niveau8_class.emplacement([(1,3)])

            rect_piece_droite = images.piece_droite_image.get_rect()
            rect_piece_droite.topleft = (465,270) #465 + x*105 et 60 + y*105 du point en haut à gauche

            rect_piece_diagonale = images.piece_diagonale_image.get_rect()
            rect_piece_diagonale.topleft = (990,585)

            rect_piece_jaune = images.piece_jaune_image.get_rect()
            rect_piece_jaune.topleft = (780,375)
            
            niveau8_class.update_plateau([2,2],[0,2],3,[99,99],[99,99]) #initialisation de la pièce droite dans la plateau
            niveau8_class.update_plateau([5,6],[5,6],2,[99,99],[99,99]) #initialisation de la pièce diagonale dans le plateau
            niveau8_class.update_plateau([3,5,6],[3,3,4],5,[99,99,99],[99,99,99]) #initialisation de la pièce jaune dans le plateau
            niveau8_class.update_plateau([4,1],[0,3],1,[99,99],[99,99]) #initialisation de la pièce non jouable dans le plateau

            piece_selectionnée_text = font.render("Pas de Pièce sélectionnée",True,(255,255,255))
            piece_rouge_text = font.render("Pièce rouge sélectionnée",True,(255,255,255))
            piece_droite_text = font.render("Pièce rose selectionée",True,(255,255,255))
            piece_jaune_text = font.render("Pièce jaune selectionée",True,(255,255,255))

            pièce_selectionnée = False
            rect_pièce_selectionnée = False
            pièce_id = False
            liste_id = False

            niveau8_first_launch = False
        
        screen.blit(images.piece_diagonale_image,rect_piece_diagonale.topleft)
        screen.blit(images.piece_droite_image, rect_piece_droite)
        screen.blit(images.piece_jaune_image, rect_piece_jaune)
        screen.blit(images.piece_non_jouable_image,(780,175))
        screen.blit(images.piece_non_jouable_image,(465,480))
        screen.blit(piece_selectionnée_text,(70,500))

        fleche_upleft_button.draw(screen)
        fleche_upright_button.draw(screen)
        fleche_downleft_button.draw(screen)
        fleche_downright_button.draw(screen)

        if fleche_upleft_button.pressed():
            niveau8_fonction("upleft")
        if fleche_upright_button.pressed():
            niveau8_fonction("upright")
        if fleche_downleft_button.pressed():
            niveau8_fonction("downleft")
        if fleche_downright_button.pressed():
            niveau8_fonction("downright")
        
        recommencer_button.draw(screen)
        if recommencer_button.pressed():
            niveau8_first_launch = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Anti-virus Menu")
                    niveau_actuel , menu_jouer , niveau8_first_launch = 0 , True , True
                
                if event.key == pygame.K_a:
                    niveau8_fonction("upleft")
                if event.key == pygame.K_s:
                    niveau8_fonction("downright")
                if event.key == pygame.K_z:
                    niveau8_fonction("upright")
                if event.key == pygame.K_q:
                    niveau8_fonction("downleft")

            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:  #vérifie si clique gauche
                    pos = pygame.mouse.get_pos() 

                    #vérifie sur quelle pièce le clique a été fait
                    if rect_piece_diagonale.collidepoint(pos):
                        if images.mask_diagonale.get_at((pos[0] - rect_piece_diagonale.x, pos[1] - rect_piece_diagonale.y)): 
                            pièce_selectionnée = position_piece_diagonale
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 2
                            liste_id.remove(2)
                            rect_pièce_selectionnée = rect_piece_diagonale
                            piece_selectionnée_text = piece_rouge_text

                    elif rect_piece_droite.collidepoint(pos):
                        if images.mask_droite.get_at((pos[0] - rect_piece_droite.x, pos[1] - rect_piece_droite.y)): 
                            pièce_selectionnée = position_piece_droite
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 3
                            liste_id.remove(3)
                            rect_pièce_selectionnée = rect_piece_droite
                            piece_selectionnée_text = piece_droite_text

                    elif rect_piece_jaune.collidepoint(pos):
                        if images.mask_jaune.get_at((pos[0] - rect_piece_jaune.x, pos[1] - rect_piece_jaune.y)): 
                            pièce_selectionnée = position_piece_jaune
                            liste_id = [2,3,4,5,6,7,8,9]
                            pièce_id = 5
                            liste_id.remove(5)
                            rect_pièce_selectionnée = rect_piece_jaune
                            piece_selectionnée_text = piece_jaune_text
        
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