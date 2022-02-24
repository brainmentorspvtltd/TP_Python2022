import pygame

pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

#r,g,b
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

def game():
    x = 50
    y = 50
    radius = 50

    moveX = 0.5
    moveY = 0.5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)

        pygame.draw.circle(screen,red, [x,y], radius)
        x += moveX
        y += moveY

        if x > width - radius:
            moveX = -0.5
        elif x < radius:
            moveX = 0.5

        if y > height - radius:
            moveY = -0.5
        elif y < radius:
            moveY = 0.5
        
        pygame.display.update()

game()
