import sys

import pygame

import random

from rock import Rock

from paper import Paper

from scissor import Scissor

from objectd import ObjectD

class scissorrock:
	"""managing game assets sha-"""

	def __init__(self):
		"""makes the game and resources"""
		pygame.init()

		self.can_clik = True # toggle

		pygame.display.set_caption("rock paper dodechahedreaon scissors")

		self.screen = pygame.display.set_mode((1200, 800))

		self.rock = []
		self.paper = []
		self.scissor = []
		self.objectd = []

		for i in range(5):
			self.rock.append(Rock(self))
			self.paper.append(Paper(self))
			self.scissor.append(Scissor(self))
			self.objectd.append(ObjectD(self))

	def run_game(self):
		"""starts the loop for the game, primary"""
		clock = pygame.time.Clock()

		background = pygame.Surface(self.screen.get_size())
		ts, w, h, c1, c2 = 50, *background.get_size(), (128, 128, 128), (64, 64, 64)
		tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
		[pygame.draw.rect(background, color, rect) for rect, color in tiles]
		
		while True:
			# i see you keyboard and mouse
			mouse_pos = pygame.mouse.get_pos()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.MOUSEBUTTONUP:
					self.can_clik = True

			# checkerboard background
			self.screen.blit(background, (0, 0))
			clock.tick(60)

			# make the clanker choose
			choices = ["r", "p", "d", "s"]
			aichoice = random.choice(choices)

			#asset loading
			for rock in self.rock:
				rock.blitme()
				if pygame.mouse.get_pressed()[0] and rock.rect.collidepoint(mouse_pos) and self.can_clik:
					self.can_clik = False
					print("it works for the rock")

			for paper in self.paper:
				paper.blitme()
				if pygame.mouse.get_pressed()[0] and paper.rect.collidepoint(mouse_pos) and self.can_clik:
					self.can_clik = False
					print("it works for paper")
			          
			for scissor in self.scissor:
				scissor.blitme()
				if pygame.mouse.get_pressed()[0] and scissor.rect.collidepoint(mouse_pos) and self.can_clik:
					self.can_clik = False
					print("it works for the scissor")

			for objectd in self.objectd:
				objectd.blitme()
				if pygame.mouse.get_pressed()[0] and objectd.rect.collidepoint(mouse_pos) and self.can_clik:
					self.can_clik = False
					print("it works for the objectd")

			# makes last screen visable
			pygame.display.flip()

		pygame.quit()

if __name__ == '__main__':
	# make game instnace and run said instnace
	sr = scissorrock()
	sr.run_game()
