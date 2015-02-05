__author__ = 'Barry'

import pygame
pygame.init()

white = (255,255,255)
black =(0,0,0)
red =(255,0,0)

size =width,height =1280,720

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

#could use pygame.display.flip()
#pygame.display.update()

gameExit =False
while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit =True
    screen.fill(white)

    pygame.display.update()
pygame.quit()
quit()
