import pygame
import math
import Colors as c

class Car:

    def __init__(self, start_position):
        self.x = start_position[0]
        self.y = start_position[1]
        self.width = 25
        self.hight = 25
        self.speed = 7.5
        self.angle = 0
        self.dth = math.pi * (1 / 6)
        self.line = 200

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
        pygame.draw.line(win, c.WHITE, (self.x + self.width/2, self.y + self.hight/2),
                                        (self.x + self.width/2 + self.line * math.cos(self.angle - math.pi/2),
                                         self.y + self.hight/2 + self.line * math.sin(self.angle - math.pi/2)))