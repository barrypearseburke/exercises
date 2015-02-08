__author__ = 'Barry'

import pygame
import  time
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
fps =30
lead_x = width/2
lead_y  = height/2
lead_y_change =0
lead_x_change =0
speed =10
blockw = 10
blockh = 10
font =pygame.font.SysFont(None,25)
def Message_to_user(msg,colour):
    screen_text = font.render(msg,True,colour)
    screen.blit(screen_text, [width/2 , height/2])

while not gameExit:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit =True

        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change -= speed
                lead_y_change =0

            elif event.key == pygame.K_RIGHT:
                lead_x_change  += speed
                lead_y_change =0



            elif event.key == pygame.K_UP:
                lead_y_change -= speed
                lead_x_change =0

            elif event.key == pygame.K_DOWN:
                lead_y_change  += speed
                lead_x_change =0

            #hold and press  button
            # if event.type ==pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or pygame.K_RIGHT :
            #         lead_x_change =0
            #     if event.key == pygame.K_UP or pygame.K_DOWN :
            #         lead_y_change =0

    if (lead_x >= width or lead_x <= 0) or (lead_y >= height or lead_y <=0):
        gameExit = True

    lead_x+= lead_x_change
    lead_y += lead_y_change
    screen.fill(white)
    #pygame.draw.rect(screen,black,[400,300,10,100]) #where,colour, in list coriates (top left, width,height) is the parameters
    #pygame.draw.rect(screen,red,[400,300,10,10]) #where,colour, in list coriates (top left, width,height) is the parameters

    #use fill to draw rect
    screen.fill(red,rect =[lead_x,lead_y,blockw,blockh]) # alterative too draw rect #fill can be graphicly accelrated

    pygame.display.update()
    clock.tick(fps)
Message_to_user("you lose",black)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()


#commite to git test after pycharm upgrade