class Settings:
	"""to store settings, duh."""

	def __init__(self):
		window = pygame.display.set_mode((1200, 800))
		clock = pygame.time.Clock()

		background = pygame.Surface(window.get_size())
		ts, w, h, c1, c2 = 50, *background.get_size(), (128, 128, 128), (64, 64, 64)
		tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
		[pygame.draw.rect(background, color, rect) for rect, color in tiles]
