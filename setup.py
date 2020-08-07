import cx_Freeze

executables = [cx_Freeze.Executable("lines.py")]

cx_Freeze.setup(
	name = "Lines", 
	options = {"build_exe":{"packages":["pygame"], 
				"include_files":["background.wav",
				 "coin_collect.wav", "create.wav", 
				 "delete.wav", "gameover.wav", "high_score.txt", "rules.txt"]}}, 

	executables = executables

	)