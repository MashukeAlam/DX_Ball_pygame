import pygame, sys
import random

from ball import Ball
from bar import Bar
from boxes import Boxes
from box import SingleBox
pygame.init()

# Constants
_COLORS = {"black" : (0, 0, 0), "white" : (255, 255, 255)}
_DIM = width, height = 1200, 600
_IMG_HEIGHT = 20
img_res = [(200, _IMG_HEIGHT), (180, _IMG_HEIGHT), (160, _IMG_HEIGHT)]


# screen config
screen = pygame.display.set_mode(_DIM)
pygame.display.set_caption("DX Ball")

# Images
ball = pygame.image.load('_ball.png')
bar = pygame.image.load('_bar.png')
box1 = pygame.image.load('_box1.png')
box2 = pygame.image.load('_box2.png')
box3 = pygame.image.load('_box3.png')
gameover = pygame.image.load('_gameover.png')

boxes = [box1, box2, box3]

RUNNING = True
TIME_SPENT = 1
SCORE = 0

# initital gameobjects
ball_obj = Ball([7, 7], _DIM, ball)
bar_obj = Bar([7, 0], _DIM, bar)
box_arr = []

# Score Texts
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('Scire: ', True, (255, 255, 255), (255, 255, 255))
textRect = text.get_rect()
textRect.center = (_DIM[0] - 80, _DIM[1] - 20)

# Trial Tests
test_ball = pygame.image.load('_ball.png')
test_ball = pygame.transform.scale(test_ball, (50, 50))
tb_rect = test_ball.get_rect()
speed = [7, 7]

# Boxes
def build_full_panel():
    total = int(_DIM[1] / _IMG_HEIGHT)

    for i in range(0, total):
        curr_width = 0
        pos = [0, -(i * _IMG_HEIGHT)]
        while curr_width < _DIM[0]:
            # print(pos)
            img_select = random.randint(0, 2)
            res_select = random.randint(0, 2)
            # print(img_select, res_select)
            curr = boxes[img_select]
            curr = pygame.transform.scale(curr, img_res[res_select])
            box_arr.append(SingleBox(10, _DIM, curr, pos))
            curr_width += img_res[res_select][0]
            pos[0] += img_res[res_select][0]

build_full_panel()

# Game loop
while RUNNING:
    TIME_SPENT += 1
    # print(TIME_SPENT)
    for event in pygame.event.get():
        # onClose
        if event.type == pygame.QUIT:
            RUNNING = False
            # sys.exit()
    screen.fill(_COLORS["black"])
    if(ball_obj.move() == "GAME_OVER"):

        RUNNING = False

    mouseX = pygame.mouse.get_pos()[0]

    bar_obj.move(mouseX)
    if ball_obj.has_collided_with(bar_obj.rect):
        ball_obj.flip_vertical_dir()
    screen.blit(ball_obj.image, ball_obj.rect)
    screen.blit(bar_obj.image, bar_obj.rect)
    if TIME_SPENT % (40 * 5) == 0:
        TIME_SPENT = 1
        for i in box_arr:
            i.move_down()
            screen.blit(i.image, i.rect)
    for i in box_arr:
        screen.blit(i.image, i.rect)
    for i in box_arr:
        if ball_obj.has_collided_with(i.rect):
            # print("Hit!")
            ball_obj.flip_vertical_dir()
            box_arr.remove(i)
            SCORE += 10
            break

    text = font.render('Score: ' + str(SCORE), True, (255, 255, 255), _COLORS["black"])

    screen.blit(text, textRect)
    pygame.display.update()
    pygame.time.delay(25)
    #print('loop running')