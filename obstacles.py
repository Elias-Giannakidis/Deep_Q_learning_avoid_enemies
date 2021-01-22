import pygame
import math
import Colors as c

class Coin:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.rarius = 20

    def draw(self, win):
        pygame.draw.circle(win, c.OLIVE, (self.x, self.y), self.radius, 0)


class Enemy:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.speed = 5
        self.width = 25
        self.hight = 25

    def move(self, target_pos):
        dx = target_pos[0] - self.x
        dy = target_pos[1] - self.y
        L = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
        cos = dx/L
        sin = dy/L
        self.x += self.speed * cos
        self.y += self.speed * sin

    def is_collition(self, target_pos):
        dx = target_pos[0] - self.x
        dy = target_pos[1] - self.y
        if abs(dx) < self.width and abs(dy) < self.hight:
            return True
        else:
            return False

    def draw(self, win):
        pygame.draw.rect(win, c.WHITE, (self.x, self.y, self.width, self.hight), 0)

class Board_limits:
    def __init__(self, width, hight):
        self.t = 10
        self.width = width - 2 * self.t
        self.hight = hight - 2 * self.t

    def draw(self, win):
        pygame.draw.rect(win, c.BLACK, (self.t, self.t, self.width, self.hight), 5)

    def is_collition(self, target_pos):
        x = target_pos[0]
        y = target_pos[1]
        if x < self.t or x > self.t + self.width - 25 or y < self.t or y > self.t + self.hight - 25:
            return True
        else:
            return False