import pygame.font

class scorekeep:
	"""scoring data, dumbass."""

	def __init__(self, scissorrock):
		self.screen = scissorrock.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = scissorrock.settings
		self.stats = 

		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
