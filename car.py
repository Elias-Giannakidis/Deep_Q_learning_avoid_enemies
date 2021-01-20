import pygame
import math
import Colors as c

class Car:

    def __init__(self, start_position):
        self.x = start_position[0]
        self.y = start_position[1]
        self.width = 50
        self.hight = 50
        self.speed = 15
        self.angle = 0
        self.dth = math.pi * (1 / 6)

    def move(self):
        self.y -= self.speed * math.cos(self.angle)
        self.x += self.speed * math.sin(self.angle)

    def turn_right(self):
        self.angle += self.dth
        if self.angle > 2 * math.pi:
            self.angle -= 2*math.pi

    def turn_left(self):
        self.angle -= self.dth
        if self.angle < -2 * math.pi:
            self.angle += 2*math.pi

    def draw(self, win):
        pygame.draw.rect(win, c.BLACK, (self.x, self.y, self.width, self.hight), 0)