import pygame
import sys
import random

# Conf. princ.
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mouse.set_visible(0)


# Conf. ventana
displayInfo = pygame.display.Info()
screenWidth = displayInfo.current_w
screenHeight = displayInfo.current_h
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pypong!')


# Variables de texto
gameFont = pygame.font.Font("./font/PressStart2P.ttf", 60)

# Variables de sonido
pongSound = pygame.mixer.Sound("./sound/pong.ogg")
scoreSound = pygame.mixer.Sound("./sound/score.ogg")

# Colores
white = (255, 255, 255)
green = (0, 192, 0)
grey = (220, 220, 220)
bgColor = (0, 0, 0)

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


def ballLogic():
    ball = state["ball"]["sprite"]
    ball.x += state["ball"]["speed"].x
    ball.y += state["ball"]["speed"].y

    # Colisiones
    if ball.top <= 0 or ball.bottom >= screenHeight:
        pygame.mixer.Sound.play(pongSound)
        state["ball"]["speed"].y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(scoreSound)
        state["player2"]["score"] += 1
        state["scoreTime"] = pygame.time.get_ticks()

    if ball.right >= screenWidth:
        pygame.mixer.Sound.play(scoreSound)
        state["player1"]["score"] += 1
        state["scoreTime"] = pygame.time.get_ticks()

    if ball.colliderect(state["player1"]["sprite"]) or ball.colliderect(state["player2"]["sprite"]):
        pygame.mixer.Sound.play(pongSound)
        state["ball"]["speed"].x *= -1


def playerLogic():
    _playerLogic(state["player1"])
    _playerLogic(state["player2"])


def _playerLogic(player):
    sprite = player["sprite"]
    sprite.y += player["speed"]

    # Boundary
    if sprite.top <= 10:
        sprite.top = 10

    if sprite.bottom >= screenHeight - 10:
        sprite.bottom = screenHeight - 10


def ballRestart():

    currentTime = pygame.time.get_ticks()
    state["ball"]["sprite"].center = (screenWidth / 2, screenHeight / 2)

    # Conteo
    if currentTime - state["scoreTime"] < 700:
        number3 = gameFont.render("3", False, green)
        screen.blit(number3, (screenWidth / 2 - 30, screenHeight / 2 - 30))

    if 700 < currentTime - state["scoreTime"] < 1400:
        number2 = gameFont.render("2", False, green)
        screen.blit(number2, (screenWidth / 2 - 30, screenHeight / 2 - 30))

    if 1400 < currentTime - state["scoreTime"] < 2100:
        number1 = gameFont.render("1", False, green)
        screen.blit(number1, (screenWidth / 2 - 30, screenHeight / 2 - 30))

    # Reset
    if currentTime - state["scoreTime"] < 2100:
        state["ball"]["speed"] = pygame.math.Vector2(0, 0)
    else:
        state["ball"]["speed"] = 13 * pygame.math.Vector2(
            random.choice((-1, 1)), random.choice((-1, 1)))
        state["scoreTime"] = 0


def gameExit():
    pygame.quit()
    sys.exit()


def playerController(event, player, upKey, downKey, speed=10):
    if event.type == pygame.KEYDOWN:
        # Player 2
        if event.key == upKey:
            player["speed"] -= speed
        if event.key == downKey:
            player["speed"] += speed
    if event.type == pygame.KEYUP:
        if event.key == upKey:
            player["speed"] += speed
        if event.key == downKey:
            player["speed"] -= speed


def renderScore(player, pos):
    playerText = gameFont.render(f"{player['score']}", False, grey)
    screen.blit(playerText, (screenWidth / pos - 30, 50))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            gameExit()
        # Conf. teclado
        playerController(event, state["player1"], pygame.K_w, pygame.K_s)
        playerController(event, state["player2"], pygame.K_i, pygame.K_j)

    # Lógica
    ballLogic()
    playerLogic()

    # Gráficos HD
    screen.fill(bgColor)
    for x in range(10, screenHeight, screenHeight // 15):
        if x % 2 == 1:
            continue
        pygame.draw.rect(screen, grey, (screenWidth //
                         2 - 5, x, 10, screenHeight // 30))
    pygame.draw.rect(screen, grey, state["player1"]["sprite"])
    pygame.draw.rect(screen, grey, state["player2"]["sprite"])
    pygame.draw.rect(screen, white, state["ball"]["sprite"])

    if state["scoreTime"] > 0:
        ballRestart()

    # Render de texto
    renderScore(state["player1"], 4)
    renderScore(state["player2"], 1.3)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
