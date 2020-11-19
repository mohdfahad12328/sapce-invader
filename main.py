import pygame
import random

# INITIALIZE THE PYGAME
pygame.init()

# SETTING UP THE SCREEN
screen = pygame.display.set_mode((800, 600))

# ADDING WINDOWS_NAME AND WINDOWS_ICON
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('resources/icon.png')
pygame.display.set_icon(icon)

# PLAYER
playerImg = pygame.image.load('resources/player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerX_speed = 1

# ENEMY
enemyImg = pygame.image.load('resources/enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.5
enemyY_change = 40

# ENEMY
bulletImg = pygame.image.load('resources/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = 'loaded'


# PLAYER MOVEMENT
def player(x, y):
    screen.blit(playerImg, (x, y))


# PLAYER MOVEMENT
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


#  BULLET MOVEMENT
def bullet_fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


# LOOP FOR RUNNING THE GAME
running = True
while running:
    # COLOR
    screen.fill((0, 0, 0))

    # GETTING ALL THE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # CHECKING KEY PRESS AND RELEASE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -playerX_speed
            if event.key == pygame.K_RIGHT:
                playerX_change = playerX_speed
            # IF SPACE IS PRESSED CALL BULLET_FIRE FUNCTION AND GIVE IN THE X VALUE OF PLAYER
            if event.key == pygame.K_SPACE:
                if bullet_state == 'loaded':
                    bulletX = playerX
                    bullet_fire(bulletX, enemyY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # INCREMENTATION FOR PLAYER MOVEMENT
    playerX += playerX_change

    # STOP PLAYER GETTING OUT OF SCREEN
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # ENEMY MOVEMENT CHANGE IN OPPOSITE SIDE AND MOVES DOWN WHEN IT HITS THE BOUNDARY
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    if bullet_state == 'fire':
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'loaded'

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # UPDATING WINDOW
    pygame.display.update()
