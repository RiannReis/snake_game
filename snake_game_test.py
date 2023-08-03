import pygame, random
from pygame.locals import *
from sys import exit


def draw_grid():
    for x in range(0, 600, 10):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

def on_grid_random():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return (x * 10, y * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
my_direction = LEFT

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake_Game')
clock = pygame.time.Clock()

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0, 255, 0))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255,0,0))

font = pygame.font.Font('Pixeltype.ttf', 40)
game_over_font = pygame.font.Font('Pixeltype.ttf', 75)
game_over_screen = game_over_font.render('Game Over', False, (255, 255, 255))
game_over_rect = game_over_screen.get_rect(midtop = (300, 30))
score = 0

game_active = True
while game_active:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == KEYDOWN:
                if event.key == K_UP and my_direction != DOWN:
                    my_direction = UP
                elif event.key == K_DOWN and my_direction != UP:
                    my_direction = DOWN
                elif event.key == K_LEFT and my_direction != RIGHT:
                    my_direction = LEFT
                elif event.key == K_RIGHT and my_direction != LEFT:
                    my_direction = RIGHT

    if game_active:
        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0,0))
            score += 1
            
        if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
            game_active = False
            break
        
        for i in range(1, len(snake) - 1):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                game_active = False
                break

        if not game_active:
            break
        
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])
            
        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        elif my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        elif my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        elif my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
        
        screen.fill((0,0,0))
        screen.blit(apple, apple_pos)
        
        draw_grid()
        
        score_font = font.render('Score: %s' %(score), False, (255, 255, 255))
        score_rect = score_font.get_rect(topleft = (480, 10))
        screen.blit(score_font, score_rect)

        for pos in snake:
            screen.blit(snake_skin, pos)
            if game_active == False:
                break

    pygame.display.update()
    clock.tick(15)

while not game_active:
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
