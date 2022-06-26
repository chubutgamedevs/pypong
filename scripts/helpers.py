import pygame

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.display.set_caption('Pypong!')
screenWidth = pygame.display.Info().current_w
screenHeight = pygame.display.Info().current_h
screen = pygame.display.set_mode((screenWidth, screenHeight))
canvas = pygame.Surface((screenWidth, screenHeight))
canvas.set_alpha(200)
canvas.fill((0, 0, 0))
clock = pygame.time.Clock()

green = (0, 192, 0)
white = (220, 220, 220)
bgColor = (10, 10, 10)

state = {
    "player1": {"speed": 0,
                "sprite": pygame.Rect(40, screenHeight / 2.4, 10, 100),
                "score": 0},
    "player2": {"speed": 0,
                "sprite": pygame.Rect(screenWidth - 50, screenHeight / 2.4, 10, 100),
                "score": 0},
    "ball": {"sprite": pygame.Rect(screenWidth / 2 - 15, screenHeight / 2 - 15, 15, 15),
                "speed": pygame.math.Vector2(13, 13)},
    "scoreTime": 0
}
