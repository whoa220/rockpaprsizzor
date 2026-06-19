import pygame

class ObjectD:
	"""class to manage rock and stone"""

	def __init__(self, ai_game):
		"""initialize rock and where it will sit"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# get the rock into frame
		og_img = pygame.image.load('photos/objectd.png')
		self.image = pygame.transform.scale_by(og_img, 0.5)
		self.rect = self.image.get_rect()

		# start it at the bottom of screen, in a neat row
		self.rect.topleft = self.screen_rect.topleft

	def blitme(self):
		"""doodle the rock at its spot"""
		self.screen.blit(self.image, self.rect)