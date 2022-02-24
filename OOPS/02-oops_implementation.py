import pygame
import random

pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

#r,g,b
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

class Ball:
    #constructor
    def __init__(self):
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        self.radius = 50
        self.moveX = random.random()
        self.moveY = random.random()
        self.color = random.randint(1,255),random.randint(1,255),random.randint(1,255)

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - self.radius:
            self.moveX = -random.random()
        elif self.x < self.radius:
            self.moveX = random.random()

        if self.y > height - self.radius:
            self.moveY = -random.random()
        elif self.y < self.radius:
            self.moveY = random.random()

# ball_1 = Ball()
# ball_2 = Ball()
ballsList = []
for i in range(50):
    ball = Ball()
    ballsList.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)

    # pygame.draw.circle(screen,red, [ball_1.x,ball_1.y], ball_1.radius)
    # ball_1.update()
    #
    # pygame.draw.circle(screen, red, [ball_2.x, ball_2.y], ball_2.radius)
    # ball_2.update()

    for i in range(len(ballsList)):
        pygame.draw.circle(screen, ballsList[i].color, [ballsList[i].x,
                                         ballsList[i].y],
                           ballsList[i].radius)
        ballsList[i].update()

    pygame.display.update()