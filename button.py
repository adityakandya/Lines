import pygame.font
import game_functions as gf

class Button():
    def __init__(self, ai_settings, screen, msg, center_tuple, color):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 100, 50
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(gf.rp('freesansbold.ttf'), 35)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = center_tuple
        # (self.screen_rect.centerx + 250, 30) 
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
