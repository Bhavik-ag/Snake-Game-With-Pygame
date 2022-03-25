import pygame
import random


pygame.mixer.init()
'''pygame.mixer.music.load('C:/Users/win8/Desktop/over.mp3')
pygame.mixer.music.load('C:/Users/win8/Desktop/beep.mp3')
pygame.mixer.music.load('C:/Users/win8/Desktop/back.mp3')
pygame.mixer.music.play()'''

pygame.init()

#Colors
white = (255, 255, 255)
blue = (67,238,250)
red = (255, 0, 0)
black = (0, 0, 0)
green = (38,245,45)

screen_width = 700
screen_height =500

gamewindow =  pygame.display.set_mode((screen_width,screen_height))

bgimg = pygame.image.load('./snake.jpg')
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

img = pygame.image.load('./start.jpg')
img = pygame.transform.scale(img, (screen_width, screen_height)).convert_alpha()

pygame.display.set_caption("Snake Game")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

def welcome():
    exitgame = False
    while not exitgame:
        gamewindow.fill((233,210,229))
        gamewindow.blit(img, (0, 0))
        text_screen("Welcome to Snakes", blue, 100, 30)
        text_screen("Press Space Bar To Play", blue, 70, 70)
        text_screen("By Bhavik Agarwal", green, 50, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('./back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


def gameloop():


    exitgame = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 15
    velocity_x = 0
    velocity_y = 0
    fps=30
    u=6
    snk_list = []
    snk_length = 1



    food_x = random.randint(10, screen_width/2)
    food_y = random.randint(10, screen_height/2)
    score =  0



    while not exitgame:
        
        if game_over:
            gamewindow.fill(black)
            text_screen("Game Over! ", red, 250, 200)
            text_screen("Press Enter To Continue", red, 150, 250)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True
            
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
            
            
            
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = u
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -u
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -u

                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = u


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score +=1                    
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snk_length +=5
    


        
            gamewindow.fill(black)
            gamewindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score * 10) , red, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('./over.mp3')
                pygame.mixer.music.play()


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('./over.mp3')
                pygame.mixer.music.play()

            plot_snake(gamewindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
welcome()
