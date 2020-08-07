import pygame

class Settings():
	"""Class storing the settings of the game"""

	def __init__(self):
		self.screen_width, self.screen_height = pygame.display.Info().current_w-325, pygame.display.Info().current_h-180
		self.bg_color = (0, 0, 0)
		self.coin_value = 2
		self.line_value = 1
		self.delete_value = 1
		self.coin_points = 10