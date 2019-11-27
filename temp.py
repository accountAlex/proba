# -*- coding: utf-8 -*-
import pygame
pygame.init()
n = int(input())
size = width, heigth = 300, 300
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
step = 300 / (n * 2)


def draw_sphere():
    pi = 22 / 7.0
    x_start = 0
    y_start = 0
    x_finish = 300
    y_finish = 300
    for i in range(n):
        pygame.draw.arc(screen, (255, 255, 255), (x_start, y_start, x_finish, y_finish), 0, pi * 2, 1)
        y_start += step
        y-finish += step
        
        
draw_sphere()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()