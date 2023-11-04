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
        self.plateau = [[25,1,0,1,0,1,0],  #0 tu peux bouger , 1 tu ne peux pas
                        [1,0,1,0,1,0,1],
                        [0,1,0,1,0,1,0],
                        [1,0,1,0,1,0,1],
                        [0,1,0,1,0,1,0],
                        [1,0,1,0,1,0,1],
                        [0,1,0,1,0,1,0]]
        
    def mouvement_possible(self,y,x,liste_id):
            try :
                if self.plateau[y][x] == 25:
                    return True
                elif self.plateau[y][x] == 1 :
                    return False
                elif y <= -1 or x <= -1 or y >= 7 or x >= 7:
                    return False
                elif self.plateau[y][x] in liste_id:
                    return False
                else:
                    return y,x
            except:
                return False


    def update_plateau(self,y,x,id,old_y,old_x):
            self.plateau[y][x] = id
            
            if old_y and old_x == 99:
                pass
            else:
                self.plateau[old_y][old_x] = 0
    
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


class Niveau1(Plateau):
    def __init__(self):
        super().__init__()
        self.position_piece_non_jouable1 = (3,1)
        self.position_piece_non_jouable2 = (3,5)
        self.position_piece_diagonale = [(1,5),(2,6)]
        self.position_piece_droite = [(1,1),(1,3)]

    def pièces(self):

        pièces_non_jouable_image = pygame.image.load("assets/non_jouable.png")
        pièce_diagonale_image = pygame.image.load('assets/diagonale.png')
        piece_droite_image = pygame.image.load("assets/droite.png")

        return pièces_non_jouable_image , pièce_diagonale_image , piece_droite_image
