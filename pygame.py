import pygame  
import random
import math
import sys
import os

#inicializar pygame
pygame.init()

#establece el tamaño de la pantalla
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width,screen_height))

#funcion para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path,relative_path)
    
    #cargar imagen de fondo
    asset_background = resource_path('assets/images/background.png')
    background = pygame.image.load(asset_background)
    
    #cargar icono de ventana
    asset_icon = resource_path('assets/images/ufo.png')
    icon = pygame.image.load(asset_icon)

    #cargar sonido de fondo
    asset_sound = resource_path('assets/audio/background_music.mp3')
    background_sound = pygame.mixer.music.load(asset_sound)

    #cargar imagen del jugador
    asset_playering = resource_path('assets/images/space-invaders.png')
    playering = pygame.image.load(asset_playering)

    #cargar imagen de bala
    asset_bulletimg = resource_path('assets/images/bullet.png')
    bulletimg = pygame.image.load(asset_bulletimg)

    #cargar fuente para texto de game over
    asset_over_font = resource_path('assets/fonts/RAVIE.TTF')
    over_fon = pygame.font.Font(asset_over_font)

    #cargar texto para puntuaje
    asset_font = resource_path('assets/fonts/comicbd.ttf')
    font = pygame.font.Font(asset_font)

    #establecer titulo de ventana
    pygame.display.set_caption('space invader')

    #establecer icono de ventana
    pygame.display.set_icon(icon)

    #reproducir sonido de fondo en loop
    pygame.mixer.music.play(-1)

    #crear reloj para controlar la velocidad del juego
    clock = pygame.time.clock()

    #posicion inicial del jugador
    playerX = 370
    playerY = 470
    playerx_change = 0
    playery_change = 0


    #lista para almacenar posiciones de los enemigos
    enemyimg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_Change = []
    no_of_enemies = 10 

    #se inicializan las variables para guardar las posiciones de los enemigos
    for i in range(no_of_enemies):
    #se carga la imagen del enemigo 1
        enemy1 = resource_path('assets/images/enemy1.png')
        enemyimg.append(pygame.image.load(enemy1))
        #se carga la imagen del enemigo 2
        enemy2 = resource_path('assets/images/enemy2.png')
        enemyimg.append(pygame.image.load(enemy2))

    #se asigna una posicion aleatoria en X y Y para el enemigo
        enemyX.append(random.randint(0,736))
        enemyY.append(random.randint(0,150))

        #se establece la velocidad de movimiento del enemigo X e Y
        enemyX_change.append(5)
        enemyY_Change.append(20)

        #se inicializan las variables para guardar la posicion de la bala
        bulletX = 0
        bulletY = 480
        bulletX_change = 0
        bulletY_change = 10
        bullet_state = "ready"

        #se inicializa la puntuacion en 0
        score = 0

        #funcion para mostrar la puntuacion en la pantalla
        def show_score ():
            score_value = font.render("score" + str(score), True, (255, 255, 255))
            screen.blit(score_value, (10,10))

        #funcion para dibujar al jugador en la pantalla
            def player(x , y):
                screen.blit(playering, (x , y))

                #funcion para dibujar al enemigo en la pantalla
                def enemy(x , y , i):
                    screen.blit(enemyimg[i], (x , y))

                    #funcion para disparar la bala
                    def fire_bullet(x , y):
                        global bullet_state

                        bullet_state = "fire"
                        screen.blit(bulletimg, (x + 16, y + 10) )

                        #funcion para comprobar si ha habido una colision entre la bala y el enemigo
                        def isCollision(enemyX , enemyY, bulletX, bulletY):
                            distance = math.sqrt((math.pow(enemyX-bulletX, 2)) +
                                                 (math.pow(enemyY-bulletY, 2)))
                            
                            if distance < 27:
                                return True
                            else:
                                return False
                            
                            #funcion para mostrar el texto de game over en pantalla
                            def game_over_text():
                                over_text = over_font.render("Game Over", True, (255, 255, 255))
                                text_rect = over_text.get_rect(
                                    center=(int(screen_width/2), int (screen_height/2)))
                                screen.blit(over_text, text_react)


                                #funcion principal del juego
                                def gameloop():

                                    #declara variables globales
                                    global score
                                    global playerX
                                    global playerx_change
                                    global bulletX
                                    global bulletY
                                    global Collison
                                    global bullet_state

                                    int_game = True
                                    while in_game:
                                        #maneja eventos, actualiza y renderiza el juego
                                        #limpia la pantalla
                                        screen.fill(0, 0 ,0)
                                        screen.blit(background, (0, 0))

                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                                if event.type == pygame.KEYDOWN:
                                                    #Maneja el movimiento del jugador y el disparo
                                                    if event.key == pygame.K_LEFT:
                                                        playerx_change = -5

                                                        if event.key == pygame.K_RIGHT:
                                                            playerx_change = 5

                                                            if event.key == pygame.K_SPACE:
                                                                if bullet_state == "ready":
                                                                    bulletX = playerX
                                                                    fire_bullet(bulletX, bulletY)

                                                                    if event.type == pygame.KEYUP:
                                                                        playerx_change = 0

                                        #aqui se esta actualizando la posicion del jugador
                                        playerX += playerx_change

                                        if playerX <= 0:
                                            playerX = 0
                                        elif playerX >= 736:
                                            playerX = 736

                                        #bucle que se ejecuta para cada enemigo
                                        for i in range(no_of_enemies):
                                            if enemyY[i] > 440:
                                                for j in range(no_of_enemies):
                                                    enemyY[j] = 2000
                                                game_over_text()

                                                enemyX[i] += enemyX_change[i]
                                                if enemyX[i] <= 0:
                                                    enemyX_change[i] = 5
                                                    enemyY[i] += enemyY_Change[i]
                                                elif enemyX[i] >= 736:
                                                    enemyX_change[i] = -5
                                                    enemyY[i] += enemyY_Change[i]

                                            #aqui se comprueba si ha habido una colision entre un enemigo y una bala
                                            
                                            collison = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                                            if collison:
                                                bulletY = 454
                                                bullet_state = "ready"
                                                score += 1
                                                enemyX[i] = random.randint(0, 736)
                                                enemyY[i] = random.randint(0, 150)
                                            enemy(enemyX[i], enemyY[i], i)

                                        if bulletY < 0:
                                            bulletY = 454
                                            bullet_state = "ready"
                                        if bullet_state == "fire":
                                            fire_bullet(bulletX, bulletY)
                                            bulletY -= bulletY_change

                                        player(playerX, playerY)
                                        show_score()

                                        pygame.display.update()

                                        clock.tick(120)

gameloop()


                                    








