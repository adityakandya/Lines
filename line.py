import pygame
import random
import math

class Line():
	def __init__(self, screen, mouse_pos, dot):
		self.screen = screen
		self.x = math.floor((random.random()*230 + 20))
		self.y = math.floor((random.random()*230 + 20))
		self.z = math.floor((random.random()*230 + 20))
		self.color = (self.x, self.y, self.z)
		self.a = dot.pos
		self.b = mouse_pos
		self.width = 5

	def draw_line(self):
		pygame.draw.line(self.screen, self.color, self.a, self.b, self.width)





