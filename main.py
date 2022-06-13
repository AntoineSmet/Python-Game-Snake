import pygame
import time
import random


#INIT THE GAME
pygame.init()

#COLOR
color_snake = (45, 114, 20)
color_background = (73, 71, 71)
color_food = (228, 202, 183)
color_font = (255, 255, 255)

#SETTING SNAKE
size_snake = 10
speed_snake = 13

#SCENE SETTING
width = 600
height = 400
message_font = pygame.font.SysFont('Aerial', 25)
score_font = pygame.font.SysFont('Aerial', 25)
game_display = pygame.display.set_mode((width, height))
time = pygame.time.Clock()
pygame.display.set_caption("Python Game")


#FUNCTION PRINT THE SCORE
def print_score(score):
    text = score_font.render("Score : " + str(score), True, color_font)
    game_display.blit(text, [0, 0])

#FUNCTION CREATE SNAKE
def print_snake(size_snake, pixels_snake):
    for pixel in pixels_snake:
        pygame.draw.rect(game_display, color_snake, [pixel[0], pixel[1], size_snake, size_snake])

#FUNCTION DEFINE AND START THE GAME
def game_start():
    finish = False
    close = False
    x = width/2
    y = height/2
    speed_x = 0
    speed_y = 0
    pixels_snake = []
    length_snake = 1
    target_x = round(random.randrange(0, int((width-size_snake) / 10))) * 10
    target_y = round(random.randrange(0, int((height-size_snake) / 10))) * 10

#ALGO of the Game
    while not finish:

        while close:
            game_display.fill(color_background)
            finish_message = message_font.render("Tap space to retry", True, color_font)
            game_display.blit(finish_message, [width / 2.7, height / 5])
            print_score(length_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        finish = True
                        close = False
                    if event.key == pygame.K_SPACE:
                        game_start()
                if event.type == pygame.QUIT:
                    finish = True
                    close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed_y = -size_snake
                    speed_x = 0
                if event.key == pygame.K_LEFT:
                    speed_x = -size_snake
                    speed_y = 0
                if event.key == pygame.K_RIGHT:
                    speed_x = size_snake
                    speed_y = 0
                if event.key == pygame.K_DOWN:
                    speed_y = size_snake
                    speed_x = 0

        if x >= width or x < 0 or y >= height or y < 0:
            close = True

        x += speed_x
        y += speed_y

        game_display.fill(color_background)
        pygame.draw.rect(game_display, color_food, [target_x, target_y, size_snake, size_snake])
        pixels_snake.append([x, y])

        if len(pixels_snake) > length_snake:
            del pixels_snake[0]

        for pixel in pixels_snake[:-1]:
            if pixel == [x, y]:
                close = True

        print_snake(size_snake, pixels_snake)
        print_score((length_snake - 1))

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, int((width-size_snake) / 10))) * 10
            target_y = round(random.randrange(0, int((height-size_snake) / 10))) * 10
            length_snake += 1

        time.tick(speed_snake)

    pygame.quit()
    quit()

game_start()






