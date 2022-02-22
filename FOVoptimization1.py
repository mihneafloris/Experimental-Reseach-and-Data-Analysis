import numpy as np
from numpy.linalg import solve,norm
import pygame 
import sys
from random import randint




class Line:
        def __init__(self, pos1, pos2):
                self.vertices = [np.array(pos1),np.array(pos2)]

        def render(self, screen):
                pygame.draw.line(screen,(0,255,255),(self.vertices[0][0],self.vertices[0][1]),(self.vertices[1][0],self.vertices[1][1]))

class Ball:
        def __init__(self, pos, radius, colour):
                self.pos = np.array(pos)
                self.radius = radius
                self.colour = colour
                 
        def render(self,screen):
                p = self.pos
                pygame.draw.circle(screen, self.colour, (int(p[0]),int(p[1])), self.radius)
        def FOV(self,screen):
                p =self.pos
                pygame.draw.polygon(screen,self.colour, ((int(p[0]),int(p[1])),(1,1),(1,width-1)))



#------------------------MAIN CODE-----------------------------
width = 1000
height = 300
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

        
surfs = []
tables = []
#WALLS
surfs.append(Line((1,1),(1,height-1)))
surfs.append(Line((1,5/6*height),(1/7*width, 5/6*height)))
surfs.append(Line((1/7*width, height-1),(6/7*width,height-1)))
surfs.append(Line((6/7*width, 5/6*height),(width-1 , 5/6*height)))
surfs.append(Line((width-1, height-1),(width-1, 1)))
surfs.append(Line((1,1),(3/7*width, 1)))
surfs.append(Line((2/7*width, 1/6*height),(5/7*width, 1/6*height)))
surfs.append(Line((4/7*width,1),(width-1,1)))
#TABLES

surfs.append(Line((1/7*width, 1/3*height),(2/7*width,1/3*height)))
surfs.append(Line((2/7*width, 1/3*height),(2/7*width, 2/3*height)))
surfs.append(Line((2/7*width,2/3*height),(1/7*width, 2/3*height)))
surfs.append(Line((1/7*width,2/3*height),(1/7*width,1/3*height)))

surfs.append(Line((3/7*width, 1/3*height),(4/7*width,1/3*height)))
surfs.append(Line((4/7*width, 1/3*height),(4/7*width, 2/3*height)))
surfs.append(Line((4/7*width,2/3*height),(3/7*width, 2/3*height)))
surfs.append(Line((3/7*width,2/3*height),(3/7*width,1/3*height)))

surfs.append(Line((5/7*width, 1/3*height),(6/7*width,1/3*height)))
surfs.append(Line((6/7*width, 1/3*height),(6/7*width, 2/3*height)))
surfs.append(Line((6/7*width,2/3*height),(5/7*width, 2/3*height)))
surfs.append(Line((5/7*width,2/3*height),(5/7*width,1/3*height)))

balls = []
colours=[]

for i in range(4):
        balls.append(Ball((randint(10,width-10),randint(10, height-10)),5,(randint(0,255),randint(0,255),randint(0,255))))

#Framerate counter
myfont = pygame.font.SysFont("monospace", 30)


lastt = pygame.time.get_ticks()
while True:
        
        currentt =pygame.time.get_ticks()
        dt = (currentt-lastt)/1000
        screen.fill((0,0,0))

        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        

        for ball in balls:
                ball.render(screen)
                ball.FOV(screen)
        for sf in surfs:
                sf.render(screen)
        
        
        
        lastt = currentt
        
        screen.blit(myfont.render(str(round(1/dt if dt > 0 else 60)), 1, (255,255,0)), (50, 50))
        pygame.display.update()
        
        for x in range(1000):
                for y in range(300):
                       colours.append(screen.get_at((x,y)))
print(colours)



