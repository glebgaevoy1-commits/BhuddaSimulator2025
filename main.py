import cv2
import numpy as np
import mediapipe as mp
import pygame
import time
import sys

import config

from scenes.titlescreen import title_screen
from scenes.menuscreen import menu_screen
from scenes.gamescreen import game_screen

pygame.init()

icon = pygame.image.load("window_icons/default_icon.jpg")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Bhudda Simulator 2025")

current_scene = "TITLE"

scenes = {
    "TITLE": title_screen(screen),
    "MENU": menu_screen(screen, current_scene),
    "GAME": game_screen(screen),
}

def main_loop():
    global current_scene

    while True:
        if current_scene == "QUIT":
            pygame.quit()
            sys.exit()

        next_scene = scenes[current_scene].handle_event()

        if next_scene == "QUIT":
            print("NAMASTE")
            pygame.quit()
            sys.exit()

        if next_scene:
            previous_scene = current_scene
            current_scene = next_scene

        scenes[current_scene].update()

        scenes[current_scene].draw()
        pygame.display.flip()

        pygame.time.Clock().tick(config.FPS)

if __name__ == "__main__":
    main_loop()