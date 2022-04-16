import pygame
from pygame.locals import *
import math


pygame.init()
pygame.display.set_caption("포물선 운동 시뮬레이션")

# 스크린 사이즈
screen_width = 1920
screen_height = 1080

# screen_width x screen_height 사이즈의 스크린 표면을 만듦
screen = pygame.display.set_mode((screen_width, screen_height))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
