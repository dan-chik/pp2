import pygame
 
pygame.init()
  
# create the display surface object   
win = pygame.display.set_mode((500, 500))
  
pygame.display.set_caption("Ball")
  
  
# dimensions of the object 
width = 40
height = 40
  
# object current co-ordinates 
x = 200
y = 200
# speed of movement
spd = 20

run = True
  
 
while run:
    # creates time delay of 10ms 
    pygame.time.delay(10)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
      
    
    if keys[pygame.K_LEFT] and x>40:
        x -= spd
          
    if keys[pygame.K_RIGHT] and x<500-width:
        x += spd
           
    if keys[pygame.K_UP] and y>40:
        y -= spd
           
    if keys[pygame.K_DOWN] and y<500-height:
        y += spd
         
              
    # completely fill the surface object  
    win.fill((255, 255, 255))
      
    # drawing object on screen which is rectangle here 
    pygame.draw.circle(win, (255, 0, 0), (x, y), 25)
      
    # it refreshes the window
    pygame.display.flip() 
  

pygame.quit()