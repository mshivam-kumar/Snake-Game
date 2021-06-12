import pygame
import random
pygame.mixer.init()
pygame.init()
# pygame.mixer.music.play()

#Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

screen_width=900
screen_height=600
#Game title
pygame.display.set_caption("SnakeGame")

#Create window
gameWindow=pygame.display.set_mode((screen_width,screen_height))
# bgimg=pygame.image.load("snake_image.jpeg")
#Background image
bgimg=pygame.image.load("bg_img1.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
pygame.display.update()

font=pygame.font.SysFont(None,55)
clock=pygame.time.Clock()

with open("highscore.txt") as f:
    highscore=f.read()


def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plot_snake(gameWindow,color,snk_list,snake_size):
    i=0
    for x,y in snk_list:
        if(i<1):
            pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
        else:
            pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
        i+=1


def welcome():
    pygame.mixer.music.load("start_game.mp3")
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        gameWindow.fill((230,250,120))
        text_screen("Welcome to Snakes Game", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("play_sound.mp3")
                    pygame.mixer.music.play()
                    game_loop()
                if event.key==pygame.K_q:
                    exit_game=True
                    break

        pygame.display.update()
        clock.tick(60)

def game_loop():
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    snake_size=30
    velocity_x=0
    velocity_y=0
    fps=40


    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_height/2)
    score=0
    snk_list=[]
    snk_length=1
    with open("highscore.txt") as f:
        highscore=f.read()
        
    while not exit_game:
        prev_head=(snake_x,snake_y)
        if(game_over):
            gameWindow.fill(white)
            text_screen("Game over! press enter to continue",black,200,400)
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    exit_game=True
                if(event.type==pygame.KEYDOWN):
                    if(event.key==pygame.K_RETURN):
                        # game_over=False
                        welcome()
                    if(event.key==pygame.K_q):
                        exit_game=True
                        break
        else:
            for event in pygame.event.get():
                    if(event.type==pygame.QUIT):
                        exit_game=True
                    if(event.type==pygame.KEYDOWN):
                        if(event.key==pygame.K_RIGHT):
                            # snake_x+=5
                            velocity_x=5
                            velocity_y=0
                        if(event.key==pygame.K_LEFT):
                            # snake_x+=5
                            velocity_x=-5
                            velocity_y=0
                        if(event.key==pygame.K_UP):
                            velocity_y=-5
                            velocity_x=0
                        if(event.key==pygame.K_DOWN):
                            velocity_y=5
                            velocity_x=0
                        if(event.key==pygame.K_i):
                            score+=7
                            # snk_length+=1
                        if(event.key==pygame.K_q):
                            exit_game=True
                            break
            snake_x+=velocity_x
            snake_y+=velocity_y
            if(abs(snake_x-food_x)<=30 and abs(snake_y-food_y)<=30):
                        score+=5
                        if(score>int(highscore)):
                            highscore=score
                            with open("highscore.txt",'w') as f:
                                f.write(str(score))
                            # text_screen("High Score: "+str(score),red,800,5)

                            # highscore=score

                        # print("Score: ",score*5)
                        food_x=random.randint(20,screen_width/2)
                        food_y=random.randint(20,screen_height/2)
                        snk_length+=12
                        # snk_length+=5

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score: "+str(score),red,5,5)
            text_screen("High Score: "+str(highscore),red,600,5)
            text_screen("press q to exit",black,180,560)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if(len(snk_list)>snk_length):
                del snk_list[0]
        # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            if(head in snk_list[:-1]):
                game_over=True
            # for x in snk_list[:-1]:
                # if x == head:
                    # game_over = True
                    # break
                
            # for p in snk_list[:-1]:
                # if(p[0]==head[0] and p[1]==head[1]):
                    # if(prev_head[0]!=head[0] or prev_head[1]!=head[1]):
                        # game_over=True
                    # break
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

                game_over = True
                # break

            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()