import sys
import pygame
from pygame import mixer

import config

pygame.mixer.init()

class game_screen:
    def __init__(self, screen):
        self.screen = screen

        self.doit_sfx = pygame.mixer.Sound('SFX/doit_sfx.mp3')

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE, MENU OPENED")
                    self.doit_sfx.play()
                    return "MENU"
                elif event.key == pygame.K_q:
                    return "QUIT"

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0,0,0))