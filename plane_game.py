# !/usr/local/python
# coding: utf-8

import sys
import pygame
from pygame.sprite import Group
from setting import Setting
from ship import Ship
import functions as func
from alien import Alien
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard


def run_game():

    pygame.init()
    p_setting = Setting()
    screen = pygame.display.set_mode((p_setting.screen_width, p_setting.screen_height))
    pygame.display.set_caption('Plane Game')

    play_button = Button(p_setting, screen, "Start")

    stats = GameStats(p_setting)
    scoreboard = Scoreboard(p_setting, screen, stats)

    ship = Ship(screen, p_setting)
    bullets = Group()
    aliens = Group()

    bg_color = (230,230,230)

    func.create_fleet(p_setting, screen, ship, aliens)

    while True:

        func.check_event(p_setting, screen, ship, bullets, aliens, stats, scoreboard, play_button)
        if stats.game_active:
            ship.update()
            func.update_bullets(p_setting, screen, stats, scoreboard, ship, aliens,bullets)
            func.update_aliens(p_setting, screen, stats, scoreboard, ship, aliens, bullets)

        func.update_screen(p_setting, screen, stats, scoreboard, ship, aliens, bullets, play_button)

run_game()