import pygame

class Rock:
	"""class to manage rock and stone"""

	def __init__(self, ai_game):
		"""initialize rock and where it will sit"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# get the rock into frame
		self.image = pygame.image.load('photos/rock.png')
		self.rect = self.image.get_rect()

		# start it at the bottom of screen, in a neat row
		self.rect.bottomright = self.screen_rect.bottomright

	def blitme(self):
		"""doodle the rock at its spot"""
		self.screen.blit(self.image, self.rect)
