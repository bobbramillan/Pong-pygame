#bb3323 Bavanan Bramillan
#below is my main class I have some comments explaining game mechanics

import pygame
from ball import Ball
from paddle import Paddle
from text import Text

pygame.init()

scr_wide = 800
scr_height = 600
surface = pygame.display.set_mode((scr_wide, scr_height))
pygame.display.set_caption("Dynamic Pong")


colors = [(135, 206, 235), (255, 165, 0), (255, 0, 255), (144, 238, 144)]
current_color_index = 0

red = (255, 10, 14)
ball = Ball(scr_wide // 2, scr_height // 2, red)

paddle1 = Paddle(400, 550, 200, 30, red)  # Bottom paddle
paddle2 = Paddle(400, 50, 200, 30, red)   # Top paddle

scoreBoard = Text("Score: 0", 10, 10, (255, 255, 255))
numHits = 0
clock = pygame.time.Clock()
run = True

while run:
    surface.fill(colors[current_color_index])
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Move the paddle according to mouse position
    paddle1.update_position(pygame.mouse.get_pos()[0])
    paddle2.update_position(pygame.mouse.get_pos()[0])

    

    ball.move()

    # check for collision with walls
    if ball.check_collision(scr_wide, scr_height) == True:
        numHits-=1 #lose pts if hits top or bottom wall
        if numHits == 10:
            scoreBoard.setMessage("Score: You Win")
        elif numHits < 0:
            scoreBoard.setMessage("Score: You Lose")
        else:
            scoreBoard.setMessage("Score: " + str(numHits))


    # check for collisions with paddles
    if ball.isTouching(paddle1) or ball.isTouching(paddle2):
        ball.setYSpeed(-ball.getYSpeed())
        numHits += 1 #gain pts if hits top or bottom paddle
        current_color_index = (current_color_index + 1) % len(colors) #changes the color for each pt made
        if numHits == 10:
            scoreBoard.setMessage("Score: You Win")
        elif numHits < 0:
            scoreBoard.setMessage("Score: You Lose")
        else:
            scoreBoard.setMessage("Score: " + str(numHits))
    

    ball.draw(surface)
    paddle1.draw(surface)
    paddle2.draw(surface)
    scoreBoard.draw(surface)

    
    pygame.display.flip()
    clock.tick(60)

    if numHits >= 10:
        run = False
    elif numHits < 0:
        run = False


pygame.quit()
