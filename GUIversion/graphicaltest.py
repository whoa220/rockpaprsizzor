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
		self.choice = False # choice module
		self.score_calculated = False
		self.aiplayer = 0
		self.player = 0

		self.text_x = 100
		self.text_y = 150

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
		font = pygame.font.SysFont(None, 48)

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
					self.choice = False

			# checkerboard background
			self.screen.blit(background, (0, 0))
			clock.tick(60)

			# make the clanker choose
			choices = ["rock", "paper", "objectd", "scissors"]
			aichoice = random.choice(choices)

			#asset loading
			for rock in self.rock:
				rock.blitme()
				if pygame.mouse.get_pressed()[0] and rock.rect.collidepoint(mouse_pos) and self.can_clik:
					self.can_clik = False
					self.choice = "rock"
					print("it works for the rock")

			for paper in self.paper:
				paper.blitme()
				if pygame.mouse.get_pressed()[0] and paper.rect.collidepoint(mouse_pos) and self.can_clik:
					self.can_clik = False
					self.choice = "paper"
					print(f"it works for paper and the computer chooses {aichoice}")
					if aichoice == "rock":
						print("victory")
						self.player += 1
					else:
						print("epic stewie fail, make the computer choose r next time fool ;p")
						self.aiplayer += 1
			          
			for scissor in self.scissor:
				scissor.blitme()
				if pygame.mouse.get_pressed()[0] and scissor.rect.collidepoint(mouse_pos) and self.can_clik:
					self.can_clik = False
					self.choice = "scissors"
					print("it works for " + self.choice)
					if aichoice == "paper":
						print("ayyeeeee nice!")
						self.player += 1
					else:
						print("just get good...")

			for objectd in self.objectd:
				objectd.blitme()
				if pygame.mouse.get_pressed()[0] and objectd.rect.collidepoint(mouse_pos) and self.can_clik:
					self.can_clik = False
					self.choice = "objectd"
					print("it works for the objectd")
					if aichoice == "r":
						print("why are you so bad at this game? SUPER F!!!")
						self.aiplayer += 20
					elif aichoice == "p":
						print("alas, you cannot make a dodecahedreon on a piece of p, so YOU WIN!!!")
						self.player += 20
					if aichoice == "s":
						print("you cant cut a dodecahedreon you clanker")
						self.player += 20

			if self.choice and not self.score_calculated:
				self.score_calculated = True
				print(f"computa chose {aichoice}")
				print("																				")

			ubuntu_bold = pygame.font.Font('/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', 30)
			score_text = pygame.font.Font.render(ubuntu_bold, 'player: {self.player} | computer: {self.aiplayer}', True, (255, 255, 255))
			self.screen.blit(score_text, (250, 300))

			# makes last screen visable
			pygame.display.flip()

		pygame.quit()

if __name__ == '__main__':
	# make game instnace and run said instnace
	sr = scissorrock()
	sr.run_game()
