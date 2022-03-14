import pygame, sys
from classes import *
from process import *

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 600, 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

clock = pygame.time.Clock()
FPS = 30

for i in range(13):
    Brick(10 + (45 * i), 50, 40, 20)

for i in range(12):
    Brick(30 + (45 * i), 75, 40, 20)

for i in range(13):
    Brick(10 + (45 * i), 100 , 40, 20)

for i in range(12):
    Brick(30 + (45 * i), 125, 40, 20)

for i in range(13):
    Brick(10 + (45 * i), 150 , 40, 20)

plate = Plate(280, 550, 40, 10)
ball = Ball(plate.posx + (plate.width / 2), plate.posy - 10, 10)

while True:

    process(plate, ball)

    screen.fill((0, 0, 0))

    if len(Brick.List) == 0:
        ball.game_over = True

    if not ball.game_over:
        plate.move(SCREENWIDTH, SCREENHEIGHT)
        ball.move(plate, SCREENWIDTH, SCREENHEIGHT)
        
    for brick in Brick.List:
        pygame.draw.rect(screen, (255, 127, 80), (brick.posx, brick.posy, brick.width, brick.height), 0)

    pygame.draw.circle(screen, (255, 255, 0), (ball.posx, ball.posy), ball.radius, 0)
    pygame.draw.rect(screen, (255, 255, 255), (plate.posx, plate.posy, plate.width, plate.height), 0)
    
    pygame.display.flip()
    clock.tick(FPS)
