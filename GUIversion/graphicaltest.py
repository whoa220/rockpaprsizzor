import sys

import pygame

from rock import Rock

class scissorrock:
	"""managing game assets sha-"""

	def __init__(self):
		"""makes the game and resources"""
		pygame.init()

		pygame.display.set_caption("rock paper dodechahedreaon scissors")

		self.screen = pygame.display.set_mode((1200, 800))

		self.rock = Rock(self)

	def run_game(self):
		"""starts the loop for the game, primary"""
		clock = pygame.time.Clock()

		background = pygame.Surface(self.screen.get_size())
		ts, w, h, c1, c2 = 50, *background.get_size(), (128, 128, 128), (64, 64, 64)
		tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
		[pygame.draw.rect(background, color, rect) for rect, color in tiles]
		
		while True:
			# i see you keyboard and mouse
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.quit()

			# checkerboard background
			self.screen.blit(background, (0, 0))
			pygame.display.flip()
			clock.tick(60)
			self.rock.blitme()

			# makes last screen visable
			pygame.display.flip()

if __name__ == '__main__':
	# make game instnace and run said instnace
	sr = scissorrock()
	sr.run_game()
