#! /usr/bin/python3

import pygame
import math
import sys
import os


def angle2D(p1, p2):
    """ takes p1 as origin """
    x1, y1 = p1
    x2, y2 = p2
    ret_angle = math.atan2(-(y2 - y1), (x2 - x1))
    return ret_angle


def distance2D(p1, p2):
    """ p1 and p2 are tuples """
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)  # float


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# this is a comment

screen_width = 1600
screen_height = 900
center_x = screen_width * .5
center_y = screen_height * .5

gameWindow = pygame.display.set_mode((screen_width, screen_height))
img_dir = os.path.join(os.path.dirname(__file__), "img")


class Ball(object):

    # img = pygame.image.load('golfBall.png')
    img = pygame.image.load(os.path.join(img_dir, 'golf_ball.png'))
    img = pygame.transform.scale(img, (40, 40))
    width, height = img.get_size()

    def __init__(self):
        self.name = "Golf Ball"
        self.x = screen_width * .5
        self.y = screen_height - 50

    def drawCenter(self, window):
        """ Draw a Ball object using self.x and self.y as
         center coordinations """
        _x = self.x - self.width * .5
        _y = self.y - self.height * .5
        window.blit(self.img, (_x, _y))

    @property
    def center(self):
        return (self.x, self.y)


font = pygame.font.Font('freesansbold.ttf', 32)


def game_loop():
    ball = Ball()
    gameExit = False
    clock = pygame.time.Clock()
    fly = False
    check = False
    fire = False

    while not gameExit:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN and not fly:
                fly = True
                fire = True

        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()  # a tuple

        if (keys[pygame.K_ESCAPE]):
            gameExit = True

        clock.tick(60)
        gameWindow.fill((64, 64, 64))

        if fly and fire:

            fire = False
            g = 1
            angle = angle2D(ball.center, mouse_pos)
            norm = distance2D(ball.center, mouse_pos)
            norm /= 18
            vectX = math.cos(angle) * norm
            vectY = math.sin(angle) * norm
            y_i = ball.y
            dy = vectY / 1
            dx = vectX / 2

        if fly:
            ball.x += dx
            dy += -g
            ball.y -= dy
            if ball.y >= y_i:
                fly = False
                ball.y = y_i

        else:
            pass

        power = distance2D(ball.center, mouse_pos)
        angletmp = angle2D(ball.center, mouse_pos)
        text1 = font.render("Theta = {}".format(angletmp), True, blue)
        text2 = font.render("Power = {}".format(power), True, green)
        textRect1 = text1.get_rect()
        gameWindow.blit(text1, textRect1)
        textRect2 = text2.get_rect()
        gameWindow.blit(text2, (screen_width - textRect2[2], 0))
        pygame.draw.circle(gameWindow, blue, tuple(
            map(int, ball.center)), 40, 1)
        pygame.draw.line(gameWindow, red, ball.center, mouse_pos)
        ball.drawCenter(gameWindow)
        pygame.display.update()


game_loop()
pygame.quit()
raise SystemExit
# sys.exit()
