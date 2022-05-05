import random
from constants import *
import pygame
from pygame.locals import *


class Grid:
    def __init__(self, w, h, pauseTime=100) -> None:
        pygame.init()
        pygame.display.set_caption("Game of Life") # tell pygame to name the screen "Game Of Life"
        self.grid = [[ 0 for _ in range(w)] for _ in range(h)]
        self.generation = 0
        self.size: tuple[int, int] = w,h
        self.screen = pygame.display.set_mode((w*TILEWIDTH, h*TILEHEIGHT)) # size of the game
        pygame.Surface.fill(self.screen, (255,255,255))
        pygame.display.update()
        self.pause = 0
        self.clock = pygame.time.Clock()
        self.pauseTime = pauseTime

    def getNeighbours(self, index:tuple[int, int]|list[int, int]):
        rv = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                if x != 0 or y != 0:
                    if index[0]+y >= 0 and index[1]+x >= 0 and \
                       index[0]+y < NROWS and index[1]+x < NCOLS: 
                        rv.append(self.grid[index[0]+y][index[1]+x])
                    else: pass

        return  sum( rv)

    def update(self, draw=True, ep=False):
        if  self.pause == 0 and not self.isBlanc() or (ep and not self.isBlanc() ): 
            nextGeneration  = [[0 for _ in range(self.size[0])]for _ in range(self.size[1])]
            for y in range(len(self.grid)):
                for x in range(len(self.grid[y])):
                    nb = self.getNeighbours((y,x))
                    if nb == 2:
                        nextGeneration[y][x] =self.grid[y][x]
                    elif nb == 3:
                        nextGeneration[y][x] = 1
                    else: 
                        nextGeneration[y][x] = 0
            self.generation += 1
            self.grid = nextGeneration
            self.clock.tick(1000/self.pauseTime)
        if draw: self.draw()
                
    def startingGrid(self, cells:list|tuple, randomGrid:bool=False, usePygame:bool=True):
        if not usePygame:
            if randomGrid:
                lst = [[y, x] for y in range(self.size[0]) for x in range(self.size[0])]
                random.shuffle(lst)
                cells = lst[0:500]
                # print(cells[0])
            
            for x in cells:
                print(x)
                try:    self.grid[x[0]][x[1]] = 1
                except: pass
            
            self.startgrid  = cells

        else:
            # tmp = self.grid
            f  = False
            while not f:
                changes = False
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    if event.type == KEYDOWN:
                        #print(2)
                        print(event.key, K_KP_ENTER)
                        if event.key == 13: ## ENTER
                            f = True
                            print("YES")
                        # if event.key == 100: ## Key d
                        #     self.grid = tmp
                        # if event.key == 109:
                        #     self.grid = self.grid ## temporary for the moment before adding pre-structures
                        # # if event.key == 
                    if event.type == MOUSEBUTTONDOWN:
                        posx, posy = pygame.mouse.get_pos()
                        posx, posy = posx//TILEHEIGHT, posy//TILEWIDTH
                        self.grid[posy][posx] = 1-self.grid[posy][posx]
                        # tmp[posy][posx] = 1-tmp[posy][posx]
                        changes = True
                if changes: self.draw(False, False)#;print(1)

    def draw(self, showGeneration:bool=True, showIsScreenBlanc=True, isStarting=False):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and not isStarting:
                    self.pause = 1- self.pause

        
                if event.key == K_RIGHT :
              
                    if self.pause == 1 :
                       
                        if not isStarting:
                      
                            self.update(False, True)
                       

                if event.key == K_ESCAPE:
                    pass
                
        pygame.Surface.fill(self.screen, (255,255,255))
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 1:
                    pygame.draw.polygon(self.screen, (0,0,0), ((x*TILEHEIGHT, y*TILEWIDTH), ((x+1)*TILEHEIGHT, y*TILEWIDTH), ((x+1)*TILEHEIGHT, (y+1)*TILEWIDTH), (x*TILEHEIGHT, (y+1)*TILEWIDTH), ))

        if showGeneration:
            self.screen.blit(pygame.font.Font("Arial.ttf", 25).render(str(self.generation), 1, (0,0,0)), (2,2))

        if showIsScreenBlanc and self.isBlanc():
            self.screen.blit(pygame.font.Font("Arial.ttf", 50).render("THE SCREEN IS BLANC!!", 1, (0,0,0)), (0,self.size[1]//2*TILEHEIGHT))

        pygame.display.update()

    def isBlanc(self):
        return self.grid == [[ 0 for _ in range(self.size[0])] for _ in range(self.size[1])]
