import sys
import math
import pygame
import random
import os

from  line import Line
global lines

lines = []


def check_events(screen, dot, stats, coin, lin_settings, sb, play_button, 
                create_sound, coin_sound, delete_sound):
    #mouse events and keyboard event
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            save_high_score(stats)
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (math.sqrt((mouse_pos[0]-dot.pos[0])**2 + (mouse_pos[0]-dot.pos[0])**2))<=2:
                # print('Double_click')
                return
            if event.button==1:
                # if check_undo_button(undo_button, mouse_pos, dot, stats, coin):
                #     return()
                create_line(screen, mouse_pos, dot, stats, lin_settings, sb, coin, create_sound)
                create_coin(mouse_pos, coin, screen, lin_settings, stats, sb, coin_sound)
                check_game_state(mouse_pos, dot.pos, stats)
                check_play_button(lin_settings, screen, stats, sb, play_button, 
                    mouse_pos, dot, coin)
                

            elif event.button==3:
                delete_line(mouse_pos, screen, stats, lin_settings, sb, delete_sound)
                check_game_state(mouse_pos, dot.pos, stats)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                save_high_score(stats)
                sys.exit()
        
            
def update_screen(lin_settings, screen, dot, coin, sb, stats, play_button):
    screen.fill(lin_settings.bg_color)
    dot.blitme()
    coin.draw_coin()
    for i in lines:
        i.draw_line()

    sb.show_score()
    if not stats.active:
        sb.game_over()
        play_button.draw_button()
    # else:
        # undo_button.draw_button()
    #draw recent screen
    pygame.display.flip()

def create_line(screen, mouse_pos, dot, stats, lin_settings, sb, coin, create_sound):
    if stats.active :
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(create_sound)
        pygame.mixer.music.unpause()
        stats.check = check_line(mouse_pos, dot.pos)    
        lines.append(Line(screen, mouse_pos, dot))
        stats.money -= lin_settings.line_value
        sb.prep_money()
        dot.pos = mouse_pos


def check_line(a, b):
    if len(lines)>0:
        l = lines[-1]
        if a[0]==b[0] or l.a[0]==b[0]:
            if ((a[0]-b[0])/(a[1]-b[1])==(l.a[0]-b[0])/(l.a[1]-b[1])):
                return False

        else:
            # print(a[0], b[0], l.a[0], b[0])
            if ((a[1]-b[1])/(a[0]-b[0])==(l.a[1]-b[1])/(l.a[0]-b[0])):
                return False
        for i in lines[:-1]:
            if do_intersect(a, b, i.a, i.b):
                # print(a, b)
                return(False)
        return(True)

    else:
        return True
        
def orientation(p, q, r): 
    # to find the orientation of an ordered triplet (p,q,r) 
    # function returns the following values: 
    # 0 : Colinear points 
    # 1 : Clockwise points 
    # 2 : Counterclockwise 
       
    val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1])) 
    if (val > 0): 
        # Clockwise orientation 
        return 1
    elif (val < 0): 
        # Counterclockwise orientation 
        return 2
    else: 
        # Colinear orientation 
        return 0

def do_intersect(p1,q1,p2,q2): 
      
    # Find the 4 orientations required for  
    # the general and special cases 
    o1 = orientation(p1, q1, p2) 
    o2 = orientation(p1, q1, q2) 
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1) 
  
    # General case 
    if ((o1 != o2) and (o3 != o4)): 
        return True

def coin_hit(coin, screen, lin_settings):
    coin.center = gen_coin(coin, screen, lin_settings)
    # print(coin.center)
    coin.rect.center = coin.center

def gen_coin(coin, screen, lin_settings):
        coin.color = (math.floor((random.random()*245 + 5)), math.floor((random.random()*245 + 5)),
                         math.floor((random.random()*245 + 5)))
        prev_center = coin.center 
        center = (math.floor((random.random()*lin_settings.screen_width)),
                         math.floor((random.random()*(lin_settings.screen_height-50))+50))
        if tuple(screen.get_at(center))!=lin_settings.bg_color and dist_bw(prev_center, center)>10 and center[1]>20:
            return (center)
        else:
            return(gen_coin(coin, screen, lin_settings))

def create_coin(mouse_pos, coin, screen, lin_settings, stats, sb, coin_sound):
    if coin.rect.collidepoint(mouse_pos) and stats.active:
        stats.score += lin_settings.coin_points
        stats.money += lin_settings.coin_value
        sb.prep_score()
        sb.prep_money()
        coin_hit(coin, screen, lin_settings)
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(coin_sound)
        pygame.mixer.music.unpause()

def save_high_score(stats):
    with open('high_score.txt', 'w') as file_object:
        file_object.write(str(stats.high_score))

def check_game_state(mouse_pos, dot_pos, stats):
    if (stats.money<=0) or  not(stats.check):
        stats.active = False
        if stats.score>stats.high_score:
            stats.high_score=stats.score
        save_high_score(stats)


def check_play_button(lin_settings, screen, stats, sb, play_button, mouse_pos, dot, coin):
    button_clicked = play_button.rect.collidepoint(mouse_pos)
    if not stats.active and not stats.game_over_active:
        stats.game_over_active = True
        pygame.mixer.music.load('sounds/gameover.wav')
        pygame.mixer.music.play(-1)
    start_game(lin_settings, screen, stats, sb, button_clicked, dot, coin)

def start_game(lin_settings, screen, stats, sb, button_clicked, dot, coin):
    if button_clicked and not(stats.active):
        stats.game_over_active = False
        pygame.mixer.music.load('sounds/background.wav')
        pygame.mixer.music.play(-1)
        dot.pos = dot.screen_rect.center
        coin_hit(coin, screen, lin_settings)
        stats.reset_stats()
        stats.active = True
        sb.prep_images()
        global lines
        lines = []

def delete_line(mouse_pos, screen, stats, lin_settings, sb, delete_sound):
    color = screen.get_at(mouse_pos)
    line = search_line(color)

    if line!=-1:
        lines.remove(line)
        stats.money -= lin_settings.delete_value
        sb.prep_money()
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(delete_sound)
        pygame.mixer.music.unpause()

def search_line(color):
    for i in lines:
        if i.color==color:
            line = i
            break
    else:
        return(-1)
    return line

def dist_bw(a, b):
        return(math.sqrt((a[0]-b[0])**2 + (a[0]-b[0])**2))

def rp(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# def check_undo_button(undo_button, mouse_pos, dot, stats, coin):
#     button_clicked = undo_button.rect.collidepoint(mouse_pos)
#     undo(button_clicked, dot, stats, coin)
#     return(button_clicked)

# def undo(button_clicked, dot, stats, coin):
#     if button_clicked and stats.active and (len(lines)>0) and not stats.undo:
#         stats.undo = True
#         lines.remove(lines[-1])
#         dot.pos = dot.prev
#         coin.center = coin.prev
#         coin.rect.center = coin.center

