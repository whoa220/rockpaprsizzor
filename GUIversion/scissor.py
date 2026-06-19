import pygame

class Scissor:
	"""class to manage scissor and stone"""

	def __init__(self, ai_game):
		"""initialize scissor and where it will sit"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# get the scissor into frame
		og_img = pygame.image.load('photos/scissors.png')
		self.image = pygame.transform.scale_by(og_img, 0.4)
		self.rect = self.image.get_rect()

		# start it at the bottom of screen, in a neat row
		self.rect.topright = self.screen_rect.topright
		

	def blitme(self):
		"""doodle the scissor at its spot"""
		self.screen.blit(self.image, self.rect)
