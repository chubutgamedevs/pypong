import pygame, sys


def playerController(event, player, upKey, downKey, speed=10):
    if event.type == pygame.KEYDOWN:
        if event.key == upKey:
            player["speed"] -= speed

        if event.key == downKey:
            player["speed"] += speed

    if event.type == pygame.KEYUP:
        if event.key == upKey:
            player["speed"] += speed

        if event.key == downKey:
            player["speed"] -= speed


def gameExit():
    pygame.quit()
    sys.exit()
