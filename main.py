from scripts.helpers import state, screenWidth, screenHeight, screen, clock, bgColor, white, canvas
from scripts.gameLogic import ballLogic, playerLogic, ballRestart, renderScore, initVal
from scripts.controls import playerController, gameExit
from menus import menu, pausedMenu, pygame_menu
import pygame


def mainMenu():
    menu.mainloop(screen)


def startGame():
    initVal()
    isPaused = False
    while True:
        pygame.mouse.set_visible(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                isPaused = not isPaused

            # Conf. teclado
            playerController(event, state["player1"], pygame.K_w, pygame.K_s)
            playerController(event, state["player2"], pygame.K_i, pygame.K_j)

        # Menu de pausa
        if isPaused:
            screen.blit(canvas, (0, 0))
            while isPaused:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        gameExit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        isPaused = False
                if pausedMenu.is_enabled():
                    pausedMenu.update(events)
                    pausedMenu.draw(screen)
                pygame.display.update()
            continue

        # Gráficos HD
        screen.fill(bgColor)
        for x in range(10, screenHeight, screenHeight // 15):
            if x % 2 == 1:
                continue
            pygame.draw.rect(screen, white, (screenWidth // 2 - 5, x, 10, screenHeight // 30))
        pygame.draw.rect(screen, white, state["player1"]["sprite"])
        pygame.draw.rect(screen, white, state["player2"]["sprite"])
        pygame.draw.rect(screen, white, state["ball"]["sprite"])

        # Lógica
        ballLogic()
        playerLogic()

        if state["scoreTime"] > 0:
            ballRestart()

        # Render de texto
        renderScore(state["player1"], 4)
        renderScore(state["player2"], 1.3)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

# Botones del menu
pausedMenu.add.button("SALIR A MENU", mainMenu)
menu.add.button('JUGAR', startGame, selection_color=(0, 255, 134, 0))
menu.add.button('SALIR', pygame_menu.events.EXIT, selection_color=(255, 0, 104, 0))

# Loop del menu princ.
mainMenu()
