import pygame, sys, random


def ballLogic():
    global ballSpeedX, ballSpeedY, player1Score, player2Score, score_time
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # Colisiones
    if ball.top <= 0 or ball.bottom >= screenHeight:
        pygame.mixer.Sound.play(pongSound)
        ballSpeedY *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(scoreSound)
        player2Score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screenWidth:
        pygame.mixer.Sound.play(scoreSound)
        player1Score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player1) or ball.colliderect(player2):
        pygame.mixer.Sound.play(pongSound)
        ballSpeedX *= -1


def playerLogic():
    player1.y += player1Speed
    player2.y += player2Speed

    # Boundary
    if player1.top <= 10:
        player1.top = 10
    if player1.bottom >= screenHeight - 10:
        player1.bottom = screenHeight - 10
    if player2.top <= 10:
        player2.top = 10
    if player2.bottom >= screenHeight - 10:
        player2.bottom = screenHeight - 10


def ballRestart():
    global ballSpeedX, ballSpeedY, score_time

    currentTime = pygame.time.get_ticks()
    ball.center = (screenWidth / 2, screenHeight / 2)

    # Conteo
    if currentTime - score_time < 700:
        number3 = gameFont.render("3", False, green)
        screen.blit(number3, (screenWidth / 2 - 30, screenHeight / 2 - 30))
    if 700 < currentTime - score_time < 1400:
        number2 = gameFont.render("2", False, green)
        screen.blit(number2, (screenWidth / 2 - 30, screenHeight / 2 - 30))
    if 1400 < currentTime - score_time < 2100:
        number1 = gameFont.render("1", False, green)
        screen.blit(number1, (screenWidth / 2 - 30, screenHeight / 2 - 30))

    # Reset
    if currentTime - score_time < 2100:
        ballSpeedX, ballSpeedY = 0, 0
    else:
        ballSpeedY = 13 * random.choice((-1, 1))
        ballSpeedX = 13 * random.choice((-1, 1))
        score_time = None


# Conf. princ.
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mouse.set_visible(0)
score_time = True

# Conf. ventana
displayInfo = pygame.display.Info()
screenWidth = displayInfo.current_w
screenHeight = displayInfo.current_h
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pypong!')

# Variables de veloc.
player1Speed, player2Speed = 0, 0
ballSpeedX, ballSpeedY = 13, 13

# Variables de texto
player1Score, player2Score = 0, 0
gameFont = pygame.font.Font("./font/PressStart2P.ttf", 60)

# Variables de sonido
pongSound = pygame.mixer.Sound("./sound/pong.ogg")
scoreSound = pygame.mixer.Sound("./sound/score.ogg")

# Colores
white = (255, 255, 255)
green = (0, 192, 0)
grey = (220, 220, 220)
bgColor = (0, 0, 0)

# Figuritas
player1 = pygame.Rect(40, screenHeight / 2.4, 10, 100)
player2 = pygame.Rect(screenWidth - 50, screenHeight / 2.4, 10, 100)
ball = pygame.Rect(screenWidth / 2 - 15, screenHeight / 2 - 15, 15, 15)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Conf. teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # Player 1
            if event.key == pygame.K_w:
                player1Speed -= 9
            if event.key == pygame.K_s:
                player1Speed += 9
            # Player 2
            if event.key == pygame.K_i:
                player2Speed -= 9
            if event.key == pygame.K_k:
                player2Speed += 9
        if event.type == pygame.KEYUP:
            # Player 1
            if event.key == pygame.K_w:
                player1Speed += 9
            if event.key == pygame.K_s:
                player1Speed -= 9
            # Player 2
            if event.key == pygame.K_i:
                player2Speed += 9
            if event.key == pygame.K_k:
                player2Speed -= 9

    # Lógica
    ballLogic()
    playerLogic()

    # Gráficos HD
    screen.fill(bgColor)
    for x in range(10, screenHeight, screenHeight // 15):
        if x % 2 == 1:
            continue
        pygame.draw.rect(screen, grey, (screenWidth // 2 - 5, x, 10, screenHeight // 30))
    pygame.draw.rect(screen, grey, player1)
    pygame.draw.rect(screen, grey, player2)
    pygame.draw.rect(screen, white, ball)

    if score_time:
        ballRestart()

    # Render de texto
    playerText1 = gameFont.render(f"{player1Score}", False, grey)
    screen.blit(playerText1, (screenWidth / 4 - 30, 50))
    playerText2 = gameFont.render(f"{player2Score}", False, grey)
    screen.blit(playerText2, (screenWidth / 1.3 - 30, 50))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
