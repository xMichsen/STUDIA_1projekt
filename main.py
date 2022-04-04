import pygame,numpy,graphics
while True:
    print("1. Program na LAB1 - Rysunek")
    print("2. Program na LAB2 - Gra")
    print("3. Program na LAB3 - Krzywe Beziera")
    print("4. Program na LAB4 - Płaty (czajnik)")
    print("0. EXIT")
    choice = (int)(input("Wybierz co chcesz wyswietlic\n"))
    if choice == 1:
        height = 600
        width = 800

        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Rysuneczek")

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((255, 255, 255))
            # chmury z kolek
            pygame.draw.circle(screen, (135, 206, 235), (50, 40), 70)
            pygame.draw.circle(screen, (135, 206, 235), (140, 30), 60)
            pygame.draw.circle(screen, (135, 206, 235), (200, 40), 50)
            # komin i dym z komina
            pygame.draw.rect(screen, (0, 0, 0), (440, 200, 20, 90))
            pygame.draw.circle(screen, (0, 0, 0), (445, 170), 15)
            pygame.draw.circle(screen, (0, 0, 0), (450, 150), 14)
            pygame.draw.circle(screen, (0, 0, 0), (440, 140), 13)
            pygame.draw.circle(screen, (0, 0, 0), (460, 120), 12)
            pygame.draw.circle(screen, (0, 0, 0), (440, 110), 10)
            # dom
            pygame.draw.rect(screen, (139, 69, 19), (330, 300, 150, 260))
            # dach
            pygame.draw.polygon(screen, (205, 133, 63), [(300, 300), (500, 300), (400, 200)])
            # ziemia
            pygame.draw.circle(screen, (50, 205, 50), (400, 900), 500)
            # slonce
            pygame.draw.circle(screen, (255, 255, 0), (800, 10), 100)
            pygame.display.flip()

        pygame.quit()

    elif choice == 2:
        import math
        import random
        import threading
        import time

        # pip install pygame

        HEIGHT = 900
        WIDTH = 1200
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        GREEN = (0, 255, 0)
        WHITE = (255, 255, 255)

        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dodging game")
        running = True
        radius = 20
        positionx = WIDTH / 2
        positiony = 2 * HEIGHT / 3
        positionx_dif = 0
        positiony_dif = 0
        enemyx = [random.randrange(50, WIDTH - 50)]
        enemyy = [random.randrange(50, int((HEIGHT / 2) - 50))]
        enemyx_dif = [5]
        enemyy_dif = [5]
        missilex = [0]
        missiley = [0]
        missilex_dif = [0]
        missiley_dif = [1.5]
        missile_state = ["ready"]
        font = pygame.font.SysFont('Comic Sans MS', 20)
        font1 = pygame.font.SysFont('Comic Sans MS', 60)
        font2 = pygame.font.SysFont('Comic Sans MS', 30)
        seconds = 0
        current_screen = "starting screen"


        def addenemies():
            threading.Timer(5.0, addenemies).start()
            enemyx.append(random.randrange(50, WIDTH - 50))
            enemyy.append(random.randrange(50, int((HEIGHT / 2) - 50)))
            enemyx_dif.append(5)
            enemyy_dif.append(5)
            missilex.append(0)
            missiley.append(0)
            missilex_dif.append(0)
            missiley_dif.append(random.uniform(0.8, 2))
            missile_state.append("ready")


        # detekcja kolizji
        def is_collision(x1, y1, x2, y2):
            distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
            if distance < 30:
                return True
            else:
                return False


        # funkcja wykorzystujaca threading wywoluje siebie sama co 5 sekund dodajac przeciwnikow
        start = time.perf_counter()
        addenemies()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        positionx_dif = 1
                    elif event.key == pygame.K_LEFT:
                        positionx_dif = -1
                    elif event.key == pygame.K_UP:
                        positiony_dif = -1
                    elif event.key == pygame.K_DOWN:
                        positiony_dif = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        positionx_dif = 0
                    elif event.key == pygame.K_LEFT:
                        positionx_dif = 0
                    elif event.key == pygame.K_UP:
                        positiony_dif = 0
                    elif event.key == pygame.K_DOWN:
                        positiony_dif = 0

            if current_screen == "game":
                # aby nie wychodzić poza wyznaczone pole:
                if positionx <= 30:
                    positionx = 30
                if positionx >= WIDTH - 30:
                    positionx = WIDTH - 30
                if positiony >= HEIGHT - 30:
                    positiony = HEIGHT - 30
                if positiony <= HEIGHT / 2:
                    positiony = HEIGHT / 2
                # MOVEMENT PRZECIWNIKOW
                for i in range(len(enemyx)):
                    if enemyx[i] <= 30:
                        enemyx_dif[i] = random.uniform(0.5, 3)
                    if enemyx[i] >= WIDTH - 30:
                        enemyx_dif[i] = random.uniform(-3, 0.5)
                    if enemyy[i] <= 30:
                        enemyy_dif[i] = random.uniform(0.5, 3)
                    if enemyy[i] >= HEIGHT / 2 - 30:
                        enemyy_dif[i] = random.uniform(-3, 0.5)

                screen.fill((255, 255, 255))
                text = font.render("Time: " + str(round(seconds, 2)) + " seconds", True, BLACK, GREEN)
                text_game_over = font1.render("GAME OVER! \n You lasted " + str(round(seconds, 2)) + " seconds", True,
                                              WHITE,
                                              WHITE)
                # DODAWANIE ROZNICY POZYCJI DLA X I Y PRZECIWNIKOW
                for i in range(len(enemyx_dif)):
                    enemyx[i] += enemyx_dif[i]
                    enemyy[i] += enemyy_dif[i]
                    pygame.draw.circle(screen, RED, (enemyx[i], enemyy[i]), radius)

                # SPRAWDZANIE CZY POCISK JEST GOTOWY
                for i in range(len(missile_state)):
                    if missile_state[i] == "ready":
                        missiley[i] = enemyy[i]
                        missilex[i] = enemyx[i]
                        missile_state[i] = "fire"
                    if missile_state[i] == "fire":
                        pygame.draw.line(screen, BLACK, (missilex[i], missiley[i]), (missilex[i], missiley[i] + 20), 10)
                        missiley[i] += missiley_dif[i]
                    # JESLI POCISK WYLECI POZA MAPE JEST ZNOWU PRZEZ PRZECIWNIKA GOTOWY DO WYSTRZELENIA
                    if missiley[i] > HEIGHT + 50:
                        missile_state[i] = "ready"

                end = time.perf_counter()
                seconds = end - start

                # SPRAWDZANIE KOLIZJI POSICK - GRACZ
                for i in range(len(missile_state)):
                    if is_collision(positionx, positiony, missilex[i], missiley[i]):
                        current_screen = "game over"

                positionx += positionx_dif
                positiony += positiony_dif
                pygame.draw.circle(screen, BLUE, (positionx, positiony), radius)
                screen.blit(text, (WIDTH / 2 - 100, 10))
                pygame.display.flip()

            if current_screen == "game over":
                screen.fill(WHITE)
                text_game_over = font1.render("Game over!", True, BLACK, RED)
                text_game_over_2 = font2.render("You lasted " + str(round(seconds)) + " seconds", True, BLACK, WHITE)
                text_restart = font2.render("Press c to continue", True, BLACK, WHITE)
                screen.blit(text_restart, (WIDTH / 2 - 170, 3 * HEIGHT / 5))
                screen.blit(text_game_over, (WIDTH / 2 - 200, HEIGHT / 2 - 100))
                screen.blit(text_game_over_2, (WIDTH / 2 - 190, HEIGHT / 2))
                if pygame.key.get_pressed()[pygame.K_c]:
                    current_screen = "game"
                pygame.display.flip()

            if current_screen == "starting screen":
                screen.fill(WHITE)
                title = font1.render("The dodging game", True, BLACK, WHITE)
                gameinfo_1 = font2.render("Dodge enemy bullets using arrow keys.", True, BLACK, RED)
                gameinfo_2 = font2.render("If you get hit once you lose. The longer you last the harder the game gets.",
                                          True, BLACK, RED)
                gameinfo_3 = font2.render("Press SPACE to start.", True, RED, WHITE)
                screen.blit(gameinfo_1, (WIDTH / 2 - 300, HEIGHT / 4))
                screen.blit(gameinfo_2, (WIDTH / 12, HEIGHT / 4 + 43))
                screen.blit(gameinfo_3, (WIDTH / 3, HEIGHT / 2))
                screen.blit(title, (WIDTH / 2 - 300, HEIGHT / 4 - 100))

                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    current_screen = "game"
                pygame.display.flip()
        pygame.quit()
    elif choice == 3:
        from graphics import *
        import numpy as np


        def factorial(n):
            fact = 1
            for i in range(1, n + 1):
                fact = fact * i
            return fact


        def newton(n, i):
            return factorial(n) / (factorial(i) * factorial(n - i))


        def Bezier(n, px, py):
            pointx = 0
            pointy = 0
            for t in np.arange(0.0, 1.0, 0.001):
                pointx = 0
                pointy = 0
                for i in range(n + 1):
                    pointx = pointx + (newton(n, i) * ((1 - t) ** (n - i)) * (t ** i)) * px[i]
                    pointy = pointy + (newton(n, i) * ((1 - t) ** (n - i)) * (t ** i)) * py[i]
                pt = Point(pointx, pointy)
                pt.draw(win)


        # t - kolejny punkt | n - ilość punktów kontrolnych-1 | i-kolejna wartość
        win = GraphWin('Bezier', 600, 500)
        # rysowanie inicjału M
        px = [26, 50, 126, 132, 217, 223]
        py = [470, 20, 600, 400, 67, 470]
        Bezier(5, px, py)
        # rysowanie inicjału S
        px1 = [488, 302, 480, 480, 569, 483, 408]
        py2 = [266, 290, 372, 372, 433, 493, 473]
        Bezier(6, px1, py2)

        #win.getMouse()
        win.close()
    elif choice == 4:
        print("Pusto :(")
    elif choice == 0:
        break
