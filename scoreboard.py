import pygame.font
import game_functions as gf

class Scoreboard():
    """Scoring Information"""

    def __init__(self, lin_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.lin_settings = lin_settings
        self.stats = stats

        self.text_color = (230, 230, 230) 
        self.font = pygame.font.Font(gf.rp('freesansbold.ttf'), 35)

        self.game_over_image = self.font.render('Game Over :(', True,
                        self.text_color, self.lin_settings.bg_color)
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = self.screen_rect.center
        self.game_over_rect.width = 500
        self.game_over_rect.height = 250

        self.prep_images()

    def prep_score(self):
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.lin_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.centerx
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.money_image, self.money_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.lin_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.right - 50
        self.high_score_rect.top = self.score_rect.top

    def prep_money(self):
        money_str = "{:,}".format(self.stats.money)
        self.money_image = self.font.render(money_str, True, self.text_color,
            self.lin_settings.bg_color)

        self.money_rect = self.money_image.get_rect()
        self.money_rect.right = self.screen_rect.left + 40
        self.money_rect.top = 20

    def prep_images(self):
        self.prep_money()
        self.prep_score()
        self.prep_high_score()

    def game_over(self):
        self.screen.blit(self.game_over_image, self.game_over_rect)
