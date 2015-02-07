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
clock =pygame.time.Clock()
fps =10
lead_x =300
lead_y =300
lead_y_change =0
lead_x_change =0

while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit =True

        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change -= 10

            if event.key == pygame.K_RIGHT:
                lead_x_change  += 10

        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lead_y_change -= 10

            if event.key == pygame.K_DOWN:
                lead_y_change  += 10
    lead_x+= lead_x_change
    lead_y += lead_y_change
    screen.fill(white)
    #pygame.draw.rect(screen,black,[400,300,10,100]) #where,colour, in list coriates (top left, width,height) is the parameters
    #pygame.draw.rect(screen,red,[400,300,10,10]) #where,colour, in list coriates (top left, width,height) is the parameters

    #use fill to draw rect
    screen.fill(red,rect =[lead_x,lead_y,10,10]) # alterative too draw rect #fill can be graphicly accelrated

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()


#commite to git test after pycharm upgrade