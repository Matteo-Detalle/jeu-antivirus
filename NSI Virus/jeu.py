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
            for y,x in zip(tabY,tabX):
                if y <= -1 or x <= -1 or y >= 7 or x >= 7:
                    return False
                elif y == 0 and x == 0: #veut dire que le point de la pièce est actuellement à la case 0,0
                    if pièce_id == 2:
                        return "GG"
                    else:
                        pass
                elif self.plateau[y][x] == 1 :
                    return False
                elif self.plateau[y][x] in liste_id:
                    return False
                else:
                    pass
            return True
    
    def update_plateau(self,tabY,tabX,id,tabOldY,tabOldX):
            for y,x,oldY,oldX in zip(tabY,tabX,tabOldY,tabOldX): #zip permettant la répartition de chaque élément
                self.plateau[y][x] = id

                if oldY == 99 and oldX == 99: #permet l'initialisation des pièces par défaut 
                    pass
                else:
                    self.plateau[oldY][oldX] = 0
    
    def pièce(self,emplacement_initiale,id):
        """
        emplacement un tableau de coordonées x et y de chaque points de la position initiale de la pièce
        id la représentation de la pièce spécifique (permet au programme de différencier chaque pièce) bien sur chaque pièce doit avoir une id différente
        """    
        for i in emplacement_initiale:
            if self.update_plateau(i[0],i[1],id,99,99) == False: #si un des 2 points est impossible le mouvement est bloqué
                break
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

        self.recommencer_image = pygame.image.load("assets/Recommencer.png")
        
     

class Button:
	def __init__(self, x, y, image, scale):
		x_image = image.get_width()
		y_image = image.get_height()
		self.image = pygame.transform.scale(image, (int(x_image * scale), int(y_image * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def pressed(self):
		action = False
		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #vérifie l'état du clique et que c'est bien que le clique gauche
				self.clicked = True
				action = True
				
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
			
		return action
	
	def draw(self,surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))