import pygame
import Colors as c
import car
import obstacles
import random
import math

# if you want to see or not the environment
show = True
done = False

# Window size
WIDTH = 800
HEIGHT = 800

def rand():
    return random.uniform(-15, 15)

# Define the agents
mCar = car.Car((WIDTH / 2 - 25 + rand(), HEIGHT / 2 - 25 + rand()))
mEnemy1 = obstacles.Enemy([0 + rand(), 0 + rand()])
mEnemy2 = obstacles.Enemy([WIDTH + rand(), HEIGHT + rand()])
mEnemy3 = obstacles.Enemy([WIDTH + rand(), 0 + rand()])
mEnemy4 = obstacles.Enemy([0 + rand(), HEIGHT + rand()])
mLimits = obstacles.Board_limits(WIDTH, HEIGHT)

# Define the pygame window
pygame.init()
win = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("AVOID ENEMIES")
clock = pygame.time.Clock()
pygame.quit()

def get_state():
    state = [[mCar.x/WIDTH, mCar.y/HEIGHT, mCar.angle/math.pi,
              (mEnemy1.x - mCar.x)/WIDTH, (mEnemy1.y - mCar.y)/HEIGHT,
             (mEnemy2.x - mCar.x)/WIDTH, (mEnemy2.y - mCar.y)/HEIGHT,
             (mEnemy3.x - mCar.x)/WIDTH, (mEnemy3.y - mCar.y)/HEIGHT,
             (mEnemy4.x - mCar.x)/WIDTH, (mEnemy4.y - mCar.y)/HEIGHT]]
    return state

def step(action):

    global done

    if show:
        # mouse click actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()

    if action == 1:
        mCar.turn_left()
    if action == 2:
        mCar.turn_right()

    mCar.move()
    mEnemy1.move((mCar.x, mCar.y))
    mEnemy2.move((mCar.x, mCar.y))
    mEnemy3.move((mCar.x, mCar.y))
    mEnemy4.move((mCar.x, mCar.y))

    if mEnemy1.is_collition((mCar.x, mCar.y)):
        done = True
    if mEnemy2.is_collition((mCar.x, mCar.y)):
        done = True
    if mEnemy3.is_collition((mCar.x, mCar.y)):
        done = True
    if mEnemy4.is_collition((mCar.x, mCar.y)):
        done = True
    if mLimits.is_collition((mCar.x, mCar.y)):
        done = True

    if show:
        win.fill((c.GREEN))
        mLimits.draw(win)
        mEnemy1.draw(win)
        mEnemy2.draw(win)
        mEnemy3.draw(win)
        mEnemy4.draw(win)
        mCar.draw(win)
        pygame.display.flip()
        clock.tick(20)

def close():
    pygame.quit()

def reset():

    # Restart the agents
    global mCar
    mCar = car.Car((WIDTH / 2 - 25 + rand(), HEIGHT / 2 - 25 + rand()))
    global mEnemy1
    mEnemy1 = obstacles.Enemy([0 + rand(), 0 + rand()])
    global mEnemy2
    mEnemy2 = obstacles.Enemy([WIDTH + rand(), HEIGHT + rand()])
    global mEnemy3
    mEnemy3 = obstacles.Enemy([WIDTH + rand(), 0 + rand()])
    global mEnemy4
    mEnemy4 = obstacles.Enemy([0 + rand(), HEIGHT + rand()])

    # Define the pygame window
    pygame.init()
    global win
    win = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("BALANCE")
    global clock
    clock = pygame.time.Clock()

    global done
    done = False

def get_reward():
    if not done:
        return 1
    else:
        return -1000

def sample():
    return random.randint(0, 2)





