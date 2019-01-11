# !/usr/local/python
# coding: utf-8

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, setting, screen):

        super(Alien, self).__init__()
        self.setting = setting
        self.screen = screen

        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return False

    def update(self):

        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x