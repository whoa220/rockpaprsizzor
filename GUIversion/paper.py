import pygame

class Paper:
	"""class to manage paper and stone"""

	def __init__(self, ai_game):
		"""initialize paper and where it will sit"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# get the paper into frame
		og_img = pygame.image.load('photos/paper.png')
		self.image = pygame.transform.scale_by(og_img, 0.3)
		self.rect = self.image.get_rect()
		

		# start it at the bottom of screen, in a neat row
		self.rect.bottomleft = self.screen_rect.bottomleft

	def blitme(self):
		"""doodle the paper at its spot"""
		self.screen.blit(self.image, self.rect)
