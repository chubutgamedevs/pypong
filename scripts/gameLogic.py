from .helpers import state, screenWidth, screenHeight, screen, green, white
import pygame, random

scoreSound = pygame.mixer.Sound("./res/Sounds/score.ogg")
pongSound = pygame.mixer.Sound("./res/Sounds/pong.ogg")
wallSound = pygame.mixer.Sound("./res/Sounds/wall.ogg")
gameFont = pygame.font.Font("./res/Fonts/PressStart2P.ttf", 60)


def ballLogic():
    ball = state["ball"]["sprite"]
    ball.x += state["ball"]["speed"].x
    ball.y += state["ball"]["speed"].y

    # Colisiones
    if ball.top <= 0 or ball.bottom >= screenHeight:
        pygame.mixer.Sound.play(wallSound)
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


def renderScore(player, pos):
    playerText = gameFont.render(f"{player['score']}", False, white)
    screen.blit(playerText, (screenWidth / pos - 30, 50))


def initVal():
    state["player1"]["score"], state["player2"]["score"] = 0, 0
    state["scoreTime"] = pygame.time.get_ticks()
