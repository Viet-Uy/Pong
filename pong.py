from turtle import left
import pygame
pygame.init()



score_value_1 = 0
score_value_2 = 0

font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

textX2 = 350
textY2 = 10

BLACK = (0,0,0)
WHITE = (255,255,255)

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pong")

PADDLEINSET = 20
PADDLEWIDTH = 10
PADDLEHEIGHT = 60
BALLSIZE = 10

clock = pygame.time.Clock()

box = pygame.Rect(100, 100, 20, 20)
leftPaddleY = 50
rightPaddleY = 50
ballX = 250
ballY = 250
ballXMomentum = 3
ballYMomentum = 3

leftPaddleRect = pygame.Rect(PADDLEINSET, leftPaddleY, PADDLEWIDTH, PADDLEHEIGHT)
rightPaddleRect = pygame.Rect(500 - PADDLEINSET - PADDLEWIDTH, rightPaddleY, PADDLEWIDTH, PADDLEHEIGHT)



def show_score(x, y):
        score = font.render("Score :" + str(score_value_1), True, (255, 255, 255))
        screen.blit(score, (x, y))

def show_score2(x, y):
        score = font.render("Score :" + str(score_value_2), True, (255, 255, 255))
        screen.blit(score, (x, y))




while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill("black")    

    pygame.draw.line(screen, WHITE, (250, 0), (250,500))


    pygame.draw.rect(screen, "red", leftPaddleRect)
    pygame.draw.rect(screen, "red", rightPaddleRect)
    pygame.draw.circle(screen, "blue", ((ballX), (ballY)), BALLSIZE)

    pressed = pygame.key.get_pressed()
    

    if (pressed[pygame.K_w]) :
        leftPaddleRect.y -= 8

    if (pressed[pygame.K_s]) :
        leftPaddleRect.y +=8

    if (pressed[pygame.K_UP]):
        rightPaddleRect.y -= 8

    if (pressed[pygame.K_DOWN]):
        rightPaddleRect.y += 8    




    if leftPaddleRect.y > 500 - PADDLEHEIGHT :
        leftPaddleRect.y = 500 - PADDLEHEIGHT

    if leftPaddleRect.y < 0:
        leftPaddleRect.y = 0

    if rightPaddleRect.y > 500 - PADDLEHEIGHT :
        rightPaddleRect.y = 500 - PADDLEHEIGHT

    if rightPaddleRect.y < 0:
        rightPaddleRect.y = 0

    if ballY < BALLSIZE:
        ballYMomentum = 3

    if ballY > 500 - BALLSIZE:
        ballYMomentum = -3

    ballX = ballX + ballXMomentum
    ballY = ballY + ballYMomentum

    if ballX <= BALLSIZE :
      ballX = 250
      ballY = 250
      ballYMomentum = 3
      ballXMomentum = -3
      score_value_2 += 1
      

    if ballX >= 500 - BALLSIZE : 
      ballX = 250
      ballY = 250
      ballYMomentum = 3
      ballXMomentum = -3
      score_value_1 += 1

    if ballX <= PADDLEINSET + PADDLEWIDTH and ballX > PADDLEINSET:
        print("første er sann")
        
        print(score_value_1)

        if leftPaddleRect.y < ballY and leftPaddleRect.y + PADDLEHEIGHT > ballY:
            ballXMomentum = 3

        

    if ballX >= 500 - PADDLEINSET - PADDLEWIDTH and ballX < 500 - PADDLEINSET: 
        print("første er sann")
        


        if rightPaddleRect.y < ballY and rightPaddleRect.y + PADDLEHEIGHT > ballY:
            ballXMomentum = -0



    show_score(textX, textY)
    show_score2(textX2, textY2)
    pygame.display.update()    
    clock.tick(60)
