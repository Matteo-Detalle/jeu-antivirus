import pygame
pygame.init()
pygame.display.set_caption("Anti-virus Game")
screen = pygame.display.set_mode((1080,720))

running = True
background = pygame.image.load(r"assets\background.png")

while running:

    screen.blit(background, (0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

