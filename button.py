# !/usr/local/python
# coding: utf-8

import pygame.font

class Button():

    def __init__(self, setting, screen, message):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 150
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.pre_message(message)

    def pre_message(self, message):

        self.message_image = self.font.render(message, True, self.text_color, self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)