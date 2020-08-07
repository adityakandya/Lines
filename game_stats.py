class GameStats():
	"""Stats for the game"""

	def __init__(self, lin_settings):
		self.lin_settings = lin_settings
		self.reset_stats()
		self.active = True
		self.high_score = 0
		self.check = True
		self.game_over_active = False


	def reset_stats(self):
		self.money = 0
		self.score = 0
		# 0 for create line
		# 1 for coin collect
		# 2 for delete line
		self.last_action = -1



	def initialize_high_score(self):
		with open('high_score.txt') as file_object:
			for line in file_object:
				self.high_score = int(line)
