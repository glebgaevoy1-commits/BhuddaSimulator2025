import sys
import pygame

import config

class title_screen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.title_text = self.font.render("Bhudda Simulator 2025", True, (0, 0, 0))
        self.instruction_caption = self.font.render("PRESS SPACE TO START // PRESS Q TO QUIT", True, (255, 0, 0))

        self.instruction_caption_rect = self.instruction_caption.get_rect()
        self.instruction_caption_rect.centerx = config.SCREEN_WIDTH // 2
        self.instruction_caption_rect.bottom = config.SCREEN_HEIGHT - 30
        self.instruction_caption_center = (self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.highlight_rect = self.instruction_caption_rect.inflate(20, 20)


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
        self.screen.blit(pygame.image.load("backgrounds/titlescreen_bg_1.jpg"), (0, 0))
        self.screen.blit(self.title_text, (10, 10))
        pygame.draw.rect(self.screen,(255, 255, 0), self.highlight_rect)
        self.screen.blit(self.instruction_caption, self.instruction_caption_rect)