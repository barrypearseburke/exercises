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
lead_x =300
lead_y -300
while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit =True
    screen.fill(white)
    #pygame.draw.rect(screen,black,[400,300,10,100]) #where,colour, in list coriates (top left, width,height) is the parameters
    #pygame.draw.rect(screen,red,[400,300,10,10]) #where,colour, in list coriates (top left, width,height) is the parameters

    #use fill to draw rect
    screen.fill(red,rect =[400,300,10,100]) # alterative too draw rect #fill can be graphicly accelrated

    pygame.display.update()
pygame.quit()
quit()


#commite to git test after pycharm upgrade