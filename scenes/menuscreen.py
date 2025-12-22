import sys
import pygame
from pygame import mixer

import config

pygame.mixer.init()

class menu_screen():
    def __init__(self, screen, previous_scene):
        self.previous_scene = previous_scene

        self.screen = screen
        self.font = pygame.font.SysFont('comicsans', 30)
        self.title_text = self.font.render('Menu', True, (0, 0, 0))

        self.doit_sfx = pygame.mixer.Sound('SFX/doit_sfx.mp3')
        self.doit_rev_sfx = pygame.mixer.Sound('SFX/doit_rev_sfx.mp3')

        print(f"previous: {self.previous_scene}")


    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE, MENU CLOSED")
                    self.doit_rev_sfx.play()
                    return self.previous_scene
                elif event.key == pygame.K_q:
                    return "QUIT"

    def update(self):
        pass

    def draw(self):
        overlay = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))