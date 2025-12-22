import sys
import pygame

import config

class title_screen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 20)
        self.title_text = self.font.render("Bhudda Simulator 2025", True, (255, 255, 255))

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE, MENU OPENED")
                elif event.key == pygame.K_SPACE:
                    print("SPACE, GAME STARTED")
                elif event.key == pygame.K_q:
                    print("QUIT, GAME CLOSED")
                    pygame.quit()
                    sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        text_rect = self.title_text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2))
        self.screen.blit(self.title_text, text_rect)