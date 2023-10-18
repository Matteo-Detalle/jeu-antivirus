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