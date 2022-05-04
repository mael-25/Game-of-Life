from constants import *
from grid import Grid

try:
    if __name__ == "__main__":
        g = Grid(NCOLS, NROWS)
        # for x in g.grid:
        #     for y in x:
        #         print(" " if not y else '█', end="")
        #     print("")
        # time.sleep(1)
        # print(g.grid)
        g.startingGrid([[2,2],[2,3],[2,4], [2,5]], True)
        # for x in g.grid:
        #     for y in x:
        #         print("  " if not y else '█', end="")

        #     print("")
        # print("--------------------------------")
        # time.sleep(1)
        while 1:
            lst  = g.update()
            # for x in g.grid:
            #     for y in x:
            #         print(" " if not y else '.', end="")

            #     print("")
            # print("-------------------------------- Generation number {}".format(g.generation))
            # time.sleep(0.2)

    ### Rules: If a square has 1 
except KeyboardInterrupt:
    # print(g.startgrid)
    # copy = True
    # if copy: pyperclip.copy(str(g.startgrid))
    print("PROGRAM QUITTED")