import pygame

class Dot():

	def __init__(self, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#start with the dot at the center
		# self.default = self.screen_rect.center
		self.pos = self.screen_rect.center
		self.radius = 5

	def blitme(self):
		"""draw the dot at its current location"""
		# pygame.draw.circle(self.screen, (0, 255, 0), self.default, self.radius)
		pygame.draw.circle(self.screen, (255, 255, 255), self.pos, self.radius)