import pygame
from random import randint

pygame.init()
display = pygame.display.set_mode((320,568))

#Assests
bg = pygame.image.load('bg.png')
bird = pygame.image.load('bird.png')


pole_width = 70
top_pole_height = randint(100, 400)
pole_color = (50,205,50)
pole_gap = 101
pole_x = 320

pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(bird)

bird_y = 150
clock = pygame.time.Clock()



while True:
    pygame.event.get()
     
    
    #control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print('Up Key Pressed')
        bird_y = bird_y - 4

    bird_y += 2
    #elif keys[pygame.K_DOWN]:
       # print('Down Key Pressed')
        #bird_y = bird_y + 5 

    display.blit(bg, (0,0))
    display.blit(bird, (20,bird_y))

    pole_x= pole_x - 2
    if pole_x <= -pole_width:
        pole_x= 320
        top_pole_height = randint(100, 400)

    pygame.draw.rect(display, pole_color, (pole_x,0 , pole_width,top_pole_height )  )
    pygame.draw.rect(display, pole_color, (pole_x,top_pole_height+ pole_gap , pole_width, 568 )  )
    pygame.display.update()
    clock.tick(100) 