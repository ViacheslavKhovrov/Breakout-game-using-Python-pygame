import pygame, sys, random

def process(plate, ball):
    
    # to close the window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    # movement

    if keys[pygame.K_d]:
        plate.velx = 10

    elif keys[pygame.K_a]:
        plate.velx = -10

    else:
        plate.velx = 0

        
    # ball launch
    
    if keys[pygame.K_SPACE]:
        ball.launch = True
        ball.velx = random.randint(-10, 10)
        ball.vely = -10
