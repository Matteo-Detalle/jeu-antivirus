import pygame
pygame.display.set_caption("Anti-virus Game")
screen = pygame.display.set_mode((1080,720))

running = True
background = pygame.image.load(r"assets\background.png")
horloge = pygame.time.Clock()
fps = 60
#myfont = pygame.font.SysFont('Helvetic', 20)


while running:

    screen.blit(background, (0,-100))
    pygame.display.flip()
    horloge.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


class Bouton(pygame.sprite.Sprite):
    def __init__(self, texte, couleur, font, x, y, largeur, hauteur, commande) :
        super().__init__()
        self._commande = commande

        self.image = pygame.Surface((largeur, hauteur))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.texte = font.render(texte, True, (0, 0, 0))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (largeur/2, hauteur/2)

        self.dessiner(couleur)

    def dessiner(self, couleur) :
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

    def executerCommande(self) :
        self._commande()
