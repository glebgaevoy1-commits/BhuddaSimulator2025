import sys
import pygame
from pygame import mixer

import config

pygame.mixer.init()

class menu_screen():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('comicsans', 30)
        self.title_text = self.font.render('Menu', True, (0, 0, 0))

        self.doit_sfx = pygame.mixer.Sound('SFX/doit_sfx.mp3')
        self.doit_rev_sfx = pygame.mixer.Sound('SFX/doit_rev_sfx.mp3')

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE, MENU CLOSED")
                    self.doit_rev_sfx.play()
                    return "TITLE" #SHOULD BE PREVIOUS SCENE

    def update(self):
        pass

    def draw(self):
        overlay = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))