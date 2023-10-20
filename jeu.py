import pygame
pygame.init()

class Plateau:
    def __init__(self):
        self.plateau = [[0,1,0,1,0,1,0],  #0 tu peux bouger , 1 tu ne peux pas
                        [1,0,1,0,1,0,1],
                        [0,1,0,1,0,1,0],
                        [1,0,1,0,1,0,1],
                        [0,1,0,1,0,1,0],
                        [1,0,1,0,1,0,1],
                        [0,1,0,1,0,1,0]]
    def mouvement(self,mouvement,emplacement):
        i = self.plateau[0]








def pièce1():
    taille = [[1,2]
              [2,1]]
    image = pygame.image.load("assets/pièce1.png")