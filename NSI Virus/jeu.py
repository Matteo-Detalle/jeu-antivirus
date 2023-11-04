import pygame
pygame.init()

class Button():
	def __init__(self, x, y, image, scale):
		x_image = image.get_width()
		y_image = image.get_height()
		self.image = pygame.transform.scale(image, (int(x_image * scale), int(y_image * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def pressed(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
				
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
			
		return action
	
	def draw(self,surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))
		
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
        
    def mouvement_possible(self,y,x,liste_id,pièce_id): #y et x les tableaux des coordonées de chaque point de la pièce
            for eley,elex in zip(y,x):
                if eley <= -1 or elex <= -1 or eley >= 7 or elex >= 7:
                    return False
                elif eley == 0 and elex == 0:
                    if pièce_id == 2:
                        return "GG"
                    else:
                        pass
                elif self.plateau[eley][elex] == 1 :
                    return False
                elif self.plateau[eley][elex] in liste_id:
                    return False
                else:
                    pass
            return True

    def update_plateau(self,newy,newx,id,oldy,oldx):
            for eley,elex,eleOldy,eleOldx in zip(newy,newx,oldy,oldx): #zip permettant la répartition de chaque élément
                self.plateau[eley][elex] = id

                if eleOldy == 99 and eleOldx == 99:
                    pass
                else:
                    self.plateau[eleOldy][eleOldx] = 0
    
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
    
    def images(self):
        pièces_non_jouable_image = pygame.image.load("assets/non_jouable.png")
        pièce_diagonale_image = pygame.image.load('assets/diagonale.png')
        piece_droite_image = pygame.image.load("assets/droite.png")
        piece_violette_image = pygame.image.load("assets/violet.png")
        piece_rose_image = pygame.image.load("assets/rose.png")
        piece_verte_image = pygame.image.load("assets/verte.png")


        return pièces_non_jouable_image , pièce_diagonale_image , piece_droite_image , piece_violette_image , piece_rose_image , piece_verte_image

class Niveau(Plateau):
    def __init__(self):
        super().__init__()

    def emplacement(self,emplacement):
        return emplacement
    
    def mouvement(self,newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id):
            if self.mouvement_possible(newy,newx,liste_id,pièce_id) == True:
                self.update_plateau(newy,newx,pièce_id,oldy,oldx)
                coordx , coordy = (newx[0]*105)+465 , (newy[0]*105)+60
                rect_pièce_selectionnée.topleft = (coordx,coordy)
                return True
            elif self.mouvement_possible(newy,newx,liste_id,pièce_id) == "GG":
                return "GG"
            elif self.mouvement_possible(newy,newx,liste_id,pièce_id) == False:
                return False
            
    def mouvement_gauche(self,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id):
        if pièce_selectionnée == False:
            pass
        else:
            oldx , oldy , newx , newy = [],[],[],[]
            for i in pièce_selectionnée:
                oldy.append(i[0])
                oldx.append(i[1])
                newy.append(i[0]-1)
                newx.append(i[1]-1)
            if self.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True :
                new_position = []
                for i in pièce_selectionnée:
                    new_position.append((i[0]-1 , i[1]-1))

                return new_position

            elif self.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG":
                return "GG"
            
    def mouvement_droite(self,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id):
        if pièce_selectionnée == False:
            pass
        else:
            oldx , oldy , newx , newy = [],[],[],[]
            for i in pièce_selectionnée:
                oldy.append(i[0])
                oldx.append(i[1])
                newy.append(i[0]+1)
                newx.append(i[1]+1)
            if self.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True :
                new_position = []
                for i in pièce_selectionnée:
                    new_position.append((i[0]+1 , i[1]+1))

                return new_position

            elif self.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG":
                return "GG"
    
    def mouvement_up(self,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id):
        if pièce_selectionnée == False:
            pass
        else:
            oldx , oldy , newx , newy = [],[],[],[]
            for i in pièce_selectionnée:
                oldy.append(i[0])
                oldx.append(i[1])
                newy.append(i[0]-1)
                newx.append(i[1]+1)
            if self.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True :
                new_position = []
                for i in pièce_selectionnée:
                    new_position.append((i[0]-1 , i[1]+1))

                return new_position

            elif self.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG":
                return "GG"
    
    def mouvement_down(self,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id):
        if pièce_selectionnée == False:
            pass
        else:
            oldx , oldy , newx , newy = [],[],[],[]
            for i in pièce_selectionnée:
                oldy.append(i[0])
                oldx.append(i[1])
                newy.append(i[0]+1)
                newx.append(i[1]-1)
            if self.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == True :
                new_position = []
                for i in pièce_selectionnée:
                    new_position.append((i[0]+1 , i[1]-1))

                return new_position

            elif self.mouvement(newy,newx,oldy,oldx,pièce_selectionnée,rect_pièce_selectionnée,pièce_id,liste_id) == "GG":
                return "GG"


                
         
        