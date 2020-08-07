a = 160
b = 30
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (a, b)

import pygame
import sys


from settings import Settings
from dot import Dot
from game_stats import GameStats
import game_functions as gf
from coin import Coin
from scoreboard import Scoreboard
from button import Button
from line import Line


def run_game():
    #Initialize game and create screen object
    pygame.init()
    pygame.mixer.music.load('sounds/background.wav')
    pygame.mixer.music.play(-1)
    coin_sound = pygame.mixer.Sound("sounds/coin_collect.wav")
    create_sound = pygame.mixer.Sound("sounds/create.wav")
    delete_sound = pygame.mixer.Sound("sounds/delete.wav")
    # gameover_sound = pygame.mixer.Sound("sounds/gameover.wav")

    lin_settings = Settings()
    stats = GameStats(lin_settings)
    stats.initialize_high_score()
    screen = pygame.display.set_mode(
        (lin_settings.screen_width,lin_settings.screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Lines")
    print(lin_settings.screen_width, lin_settings.screen_height)

    sb = Scoreboard(lin_settings, screen, stats)

    dot = Dot(screen)
    coin = Coin(screen, lin_settings)
    play_button = Button(lin_settings, screen, "Play", (screen.get_rect().centerx + 250, 40), (0, 255, 0))
    # undo_button = Button(lin_settings, screen, "Undo", (screen.get_rect().centerx - 250, 40), (255, 255, 0))

    #main loop of the game
    while True:
        gf.check_events(screen, dot, stats, coin, lin_settings, sb, play_button, 
            create_sound, coin_sound, delete_sound)
        gf.update_screen(lin_settings, screen, dot, coin, sb, stats, play_button)


run_game()

