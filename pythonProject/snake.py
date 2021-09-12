import copy
import sys
import pygame
import random


def main():
    # set the frame
    pygame.init()
    pygame.display.set_caption("Snake Game")

    screen = pygame.display.set_mode((700, 500))
    clock = pygame.time.Clock()

    # where the food going to appear
    x = random.randint(10, 690)
    y = random.randint(10, 490)
    food_point = [x, y]

    # snake initial position
    snake_list = [[350, 250]]

    # set the direction
    up = False
    down = True
    left = False
    right = False
    pygame.mixer.init()
    pygame.mixer.music.load('Dog and Pony Show.wav')
    pygame.mixer.music.play(-1)

    # game loop
    running = True
    gameOver = False

    while running:
        pygame.init()
        pygame.display.set_caption("Snake Game")

        screen = pygame.display.set_mode((700, 500))
        clock = pygame.time.Clock()

        clock.tick(8)
        screen.fill([0, 0, 0])
        font = pygame.font.SysFont("Arial", 25)
        text = font.render("Welcome to My Snake World!", True, (50, 50, 50))
        screen.blit(text, (200, 0))

        pygame.display.flip()

        # place the food
        food_display = pygame.draw.circle(screen, [200, 100, 0], food_point, 10)
        snake_display = []

        # the body of the snake
        for pos in snake_list:
            snake_display.append(pygame.draw.circle(screen, [30, 200, 100], pos, 10))

            # set the new position of the food
            if food_display.collidepoint(pos):
                snake_list.append(food_point)
                food_point = [random.randint(5, 695), random.randint(5, 495)]
                food_display = pygame.draw.circle(screen, [200, 100, 0], food_point, 10)
                break

        # control the move of the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                print(event)
                if event.key == pygame.K_UP:
                    up = True
                    down = False
                    left = False
                    right = False
                elif event.key == pygame.K_DOWN:
                    up = False
                    down = True
                    left = False
                    right = False
                elif event.key == pygame.K_RIGHT:
                    up = False
                    down = False
                    left = False
                    right = True
                elif event.key == pygame.K_LEFT:
                    up = False
                    down = False
                    left = True
                    right = False
                elif event.key == pygame.k_SPACE:
                    continue

        # the head of the snake
        pos = len(snake_list) - 1
        while pos > 0:
            snake_list[pos] = copy.deepcopy(snake_list[pos - 1])
            pos -= 1

        pos = snake_list[0]
        if right:
            pos[0] = pos[0] + 20
            if pos[0] > 700:
                pos[0] = 0
        elif left:
            pos[0] = pos[0] - 20
            if pos[0] < 0:
                pos[0] = 700
        elif up:
            pos[1] = pos[1] - 20
            if pos[1] < 0:
                pos[1] = 500
        elif down:
            pos[1] = pos[1] + 20
            if pos[1] > 500:
                pos[1] = 0

        # snake head bump with the body
        # head_display = snake_display[0]
        # count = len(snake_display)
        # while count > 1:
        #     if head_display.colliderect(snake_display[count - 1]):
        #         running = False
        #         gameOver = True
        #     count -= 1

        if snake_display[0].x not in range(6, 744):
            gameOver = True
        elif snake_display[0].y not in range(6, 494):
            gameOver = True
        elif snake_display[0] in snake_display[1:]:
            gameOver = True

        while gameOver:
            screen.fill([100, 100, 100])
            font = pygame.font.SysFont("Arial", 25)
            text = font.render("You are DEAD! Please press r to restart", True, (200, 200, 200))
            screen.blit(text, (150, 210))
            pygame.display.update()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            main()

            pygame.display.flip()
            break
        pygame.display.update()


main()
