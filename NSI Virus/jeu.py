import pygame
pygame.init()

class Plateau:
    def __init__(self):
        """
        plateau est utilisé sous forme x et y : i[x][y] , x représentant l'aspect "horizontal" et y l'aspect "vertical" dans une matrice représentée en plateau
        """
        self.plateau = [[0,1,0,1,0,1,0],  #0 tu peux bouger , 1 tu ne peux pas
                        [1,0,1,0,1,0,1],
                        [0,1,0,1,0,1,0],
                        [1,0,1,0,1,0,1],
                        [0,1,0,1,0,1,0],
                        [1,0,1,0,1,0,1],
                        [0,1,0,1,0,1,0]]
        
    def mouvement_possible(self,tabY,tabX,liste_id,pièce_id): #y et x les tableaux des coordonées de chaque point de la pièce
            """
            vérifie si la destination vers où bouger est possible

            -------------------------------------------------------------------------------------------------------------------------

            paramètres : - tableau : - TabY , tabX ; tableaux contenants les coordonnées des points de la pièce vers où le déplacement veut se faire
                         - tableau : - liste_id : tableau contenant chaque id présent dans le plateau 
                         - int : - pièce_id ; id (chiffre de 2 à 10) permettant de créer des pièces uniques  
            """
            for y,x in zip(tabY,tabX):
                if y <= -1 or x <= -1 or y >= 7 or x >= 7: #vérifie que le déplacement ne dépasse pas les limites du plateau
                    return False
                elif y == 0 and x == 0: #veut dire que le point de la pièce est actuellement à la case 0,0 (case pour gagner)
                    if pièce_id == 2: #id de la pièce rouge (celle qui permet de gagner
                        return "GG"
                    else:
                        pass
                elif self.plateau[y][x] == 1 : #case non jouable
                    return False
                elif self.plateau[y][x] in liste_id: #autre pièce est déjà présente à l'emplacement
                    return False
                else:
                    pass
            return True
    
    def update_plateau(self,tabY,tabX,id,tabOldY,tabOldX):
            """
            met à jour le plateau avec les id et les positions de chaque pièces

            -------------------------------------------------------------------------------------------------------------------------

            paramètres : - tableau : - TabY , tabX , tabOldY , tabOldX ; tableaux contenants les nouvelles coordonnées des points de la pièce et les anciennes
                         - int : - id ; id (chiffre de 2 à 10) permettant de créer des pièces uniques  
            """
            for oldY,oldX in zip(tabOldY,tabOldX):
                if oldY == 99 and oldX == 99: #permet l'initialisation des pièces au démarage ou lors d'un reset
                    pass
                else:
                    self.plateau[oldY][oldX] = 0

            for y,x in zip(tabY,tabX): #zip permettant la répartition de chaque élément
                self.plateau[y][x] = id

    def pièce(self,emplacement_initiale,id):
        """
        emplacement un tableau de coordonées x et y de chaque points de la position initiale de la pièce
        id la représentation de la pièce spécifique (permet au programme de différencier chaque pièce) bien sur chaque pièce doit avoir une id différente

        -------------------------------------------------------------------------------------------------------------------------

            paramètres : - tableau : - emplacement_initiale ; tableaux contenants les coordonnées des points de la pièce à initialiser
                         - int : - id ; id (chiffre de 2 à 10) permettant de créer des pièces uniques  
        """    
        for i in emplacement_initiale:
            if self.update_plateau(i[0],i[1],id,99,99) == False:
                print("Erreur lors de l'initialisation des pièces")
                break #pièce mal placée lors de la création du jeu
            else:
                pass


class Niveau(Plateau):
    def __init__(self):
        super().__init__()

    def emplacement(self,emplacement):
        return emplacement
    
    def mouvement(self, pièce_selectionnée, rect_pièce_selectionnée, pièce_id, liste_id, direction):
        if not pièce_selectionnée:
            return False
        tabX, tabY, oldy, oldx = [], [], [], []
        for i in pièce_selectionnée:
            oldy.append(i[0])
            oldx.append(i[1])
            if direction == "upleft":
                tabY.append(i[0] - 1)
                tabX.append(i[1] - 1)
            elif direction == "upright":
                tabY.append(i[0] - 1)
                tabX.append(i[1] + 1)
            elif direction == "downleft":
                tabY.append(i[0] + 1)
                tabX.append(i[1] - 1)
            elif direction == "downright":
                tabY.append(i[0] + 1)
                tabX.append(i[1] + 1)

        if self.mouvement_possible(tabY, tabX, liste_id, pièce_id) == True:
            self.update_plateau(tabY, tabX, pièce_id, oldy, oldx)
            coordx, coordy = (tabX[0] * 105) + 465, (tabY[0] * 105) + 60
            rect_pièce_selectionnée.topleft = (coordx, coordy)

            new_position = []
            for i in pièce_selectionnée:
                if direction == "upleft":
                    new_position.append((i[0] - 1, i[1] - 1))
                elif direction == "upright":
                    new_position.append((i[0] - 1, i[1] + 1))
                elif direction == "downleft":
                    new_position.append((i[0] + 1, i[1] - 1))
                elif direction == "downright":
                    new_position.append((i[0] + 1, i[1] + 1))
            
            return new_position

        elif self.mouvement_possible(tabY, tabX, liste_id, pièce_id) == "GG":
            return "GG"
        elif self.mouvement_possible(tabY, tabX, liste_id, pièce_id) == False:
            return False

    

class Image:
    def __init__(self):
        self.background = pygame.image.load("assets/background.png")

        self.boutton_regle_image = pygame.image.load("assets/Regle.png")
        self.boutton_quitter_image = pygame.image.load("assets/Quitter.png")
        self.boutton_jouer_image = pygame.image.load("assets/Jouer.png")
        self.fleche_volume_gauche_image = pygame.image.load("assets/fleche_gauche.png")
        self.fleche_volume_droite_image = pygame.image.load("assets/fleche_droite.png")

        self.fleche_upleft_image = pygame.image.load("assets/fleche_upleft.png")
        self.fleche_upright_image = pygame.image.load("assets/fleche_upright.png")
        self.fleche_downleft_image = pygame.image.load("assets/fleche_downleft.png")
        self.fleche_downright_image = pygame.image.load("assets/fleche_downright.png")

        self.niveau1_image = pygame.image.load("assets/niveau1.png")
        self.niveau2_image = pygame.image.load("assets/niveau2.png")
        self.niveau3_image = pygame.image.load("assets/niveau3.png")
        self.niveau4_image = pygame.image.load("assets/niveau4.png")
        self.niveau5_image = pygame.image.load("assets/niveau5.png")
        self.niveau6_image = pygame.image.load("assets/niveau6.png")
        self.niveau7_image = pygame.image.load("assets/niveau7.png")
        self.niveau8_image = pygame.image.load("assets/niveau8.png")
        self.niveau9_image = pygame.image.load("assets/niveau9.png")

        self.Plateau_image = pygame.image.load("assets/PlateauDeJeu.png")

        self.piece_non_jouable_image = pygame.image.load("assets/non_jouable.png")
        self.piece_diagonale_image = pygame.image.load('assets/diagonale.png')
        self.piece_droite_image = pygame.image.load("assets/droite.png")
        self.piece_violette_image = pygame.image.load("assets/violet.png")
        self.piece_rose_image = pygame.image.load("assets/rose.png")
        self.piece_verte_image = pygame.image.load("assets/verte.png")
        self.piece_bleu_image = pygame.image.load("assets/bleu.png")
        self.piece_violette2_image = pygame.image.load("assets/violet2.png")
        self.piece_bleu2_image = pygame.image.load("assets/bleu2.png")
        self.piece_orange_image = pygame.image.load("assets/orange.png")
        self.piece_violette3_image = pygame.image.load("assets/violet3.png")
        self.piece_jaune_image = pygame.image.load("assets/jaune.png")
        self.recommencer_image = pygame.image.load("assets/Recommencer.png")

        self.mask_diagonale = pygame.mask.from_surface(self.piece_diagonale_image, 127)
        self.mask_droite = pygame.mask.from_surface(self.piece_droite_image, 127)
        self.mask_violette = pygame.mask.from_surface(self.piece_violette_image, 127) #utilisation de masque pour dégager les pixels transparents lors de la sélection
        self.mask_rose = pygame.mask.from_surface(self.piece_rose_image, 127)
        self.mask_verte = pygame.mask.from_surface(self.piece_verte_image, 127)
        self.mask_bleu = pygame.mask.from_surface(self.piece_bleu_image, 127)
        self.mask_violette2 = pygame.mask.from_surface(self.piece_violette2_image, 127)
        self.mask_bleu2 = pygame.mask.from_surface(self.piece_bleu2_image, 127)
        self.mask_orange = pygame.mask.from_surface(self.piece_orange_image, 127)
        self.mask_violette3 = pygame.mask.from_surface(self.piece_violette3_image, 127)
        self.mask_jaune = pygame.mask.from_surface(self.piece_jaune_image, 127)

class Button:
    def __init__(self, x, y, image, scale):
        x_image = image.get_width()
        y_image = image.get_height()
        self.image = pygame.transform.scale(image, (int(x_image * scale), int(y_image * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.son = pygame.mixer.Sound('assets/button_pushed.mp3')

    def pressed(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                self.son.play()

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))