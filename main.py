import cv2
import numpy as np
import mediapipe as mp
import pygame
import time
import sys

from scenes.titlescreen import title_screen

import config

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Tqqitle Screen")

scenes = {
    "TITLE": title_screen(screen),
}

current_scene = "TITLE"

running = True
while running:
    next_scene = scenes[current_scene].handle_event()

    if next_scene:
        current_scene = next_scene

    scenes[current_scene].update()
    scenes[current_scene].draw()
    pygame.display.flip()
    pygame.time.Clock().tick(60)