import pygame
import random
import math
import game_functions as gf

class Coin():
	def __init__(self, screen, lin_settings):
		self.screen = screen
		self.color = (math.floor((random.random()*235 + 15)), math.floor((random.random()*235 + 15)),
						 math.floor((random.random()*235 + 15)))
		self.center=(0, 0)
		self.center = gf.gen_coin(self, screen, lin_settings)
		self.radius = 5
		self.rect = pygame.draw.circle(self.screen, self.color, self.center, self.radius)

	def draw_coin(self):
		pygame.draw.circle(self.screen, self.color, self.center, self.radius)

	

	def dist_bw(self, a, b):
		return(math.sqrt((a[0]-b[0])**2 + (a[0]-b[0])**2))