from constants import *
from grid import Grid

try:
    if __name__ == "__main__":
        g = Grid(NCOLS, NROWS)
        
        g.startingGrid([[2,2],[2,3],[2,4], [2,5]], True)
        
        while 1:
            g.update()
            
    ### Rules: If a square has 1 
except KeyboardInterrupt:
    print("PROGRAM QUITTED")
