import math
import random

import pygame

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load('resources/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(40)

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
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


#  BULLET MOVEMENT
def bullet_fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((bulletX - enemyX), 2) + math.pow((bulletY - enemyY), 2))
    if distance < 27:
        return True
    else:
        return False


score_value = 0
font = pygame.font.Font('resources/font.ttf', 32)
textX = 10
textY = 10


def show_score(x, y):
    score = font.render('score is:' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


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
                    bullet_fire(bulletX, enemyY[i])
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
    for i in range(number_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'loaded'
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(0, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bullet_state == 'fire':
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'loaded'

    player(playerX, playerY)
    show_score(textX, textY)
    # UPDATING WINDOW
    pygame.display.update()
