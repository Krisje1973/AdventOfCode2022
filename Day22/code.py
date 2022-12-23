import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
compas = Compass()
path = list()
grid = {}
def readinput():
    global input,max_x,max_y,path,grid
    input = readinput_lines_no_strip_no_enter("Day22\input.txt")
    path = re.split(r"(?<=\d)(?=[LR])|(?<=[LR])(?=\d)", input[-1])
    grid = {(j, i): ".#".index(cell) for i, row in enumerate(input[:-1]) for j, cell in enumerate(row) if cell != " "}

def main():
   readinput()
   #first_star()
   second_star()        

def move(pos,di):
    dir = compas.compasspoints[di]
    rev = compas.compasspoints_reversed[di]
    new = tuple(sum(tup) for tup in zip(pos,  dir))
    if new not in grid:
        new = tuple(sum(tup) for tup in zip(new, rev))
        while new in grid:
            new = tuple(sum(tup) for tup in zip(new, rev))
        new = tuple(sum(tup) for tup in zip(new,  dir))
 
    if not grid[new]:
        return new
    
    return pos

def move_2(pos,di):
    dir = compas.compasspoints[di]
    new = tuple(sum(tup) for tup in zip(pos,  dir))
    ndi=di
    if new not in grid:
        x,y = new
        
        match di, y, x:
            case "E", _, 150 if y in range(50):
                ndi, y, x = "W", 149 - y, 99
            case "E", _, 100 if y in range(50, 100):
                ndi, y, x = "N", 49, 50 + y
            case "E", _, 100 if y in range(100, 150):
                ndi, y, x = "W", 149 - y, 149
            case "E", _, 50 if y in range(150, 200):
                ndi, y, x = "N", 149, y - 100

            case "S", 200, _ if x in range(50):
                ndi, y, x = "S", 0, x + 100
            case "S", 150, _ if x in range(50, 100):
                ndi, y, x = "W", x + 100, 49
            case "S", 50, _ if x in range(100, 150):
                ndi, y, x = "W", x - 50, 99

            case "W", _, 49 if y in range(0, 50):
                ndi, y, x = "E", 149 - y, 0
            case "W", _, 49 if y in range(50, 100):
                ndi, y, x = "S", 100, y - 50
            case "W", _, -1 if y in range(100, 150):
                ndi, y, x = "E", 149 - y, 50
            case "W", _, -1 if y in range(150, 200):
                ndi, y, x = "S", 0, y - 100

            case "N", 99, _ if x in range(50):
                ndi, y, x = "E", 50 + x, 50
            case "N", -1, _ if x in range(50, 100):
                ndi, y, x = "E", x + 100, 0
            case "N", -1, _ if x in range(100, 150):
                ndi, y, x = "N", 199, x - 100

        new = (x,y)

    if not grid[new]:
        return new, ndi
    
    return pos, di

def first_star():
    curpos = list(grid.items())[0][0]
    direct = "E"
    for p in path:
        if p.isnumeric():
            for _ in range(int(p)):
                curpos = move(curpos,direct)
        else:
            direct = compas.turnCompassPoint(direct,p,90)
    
    x,y = curpos
    print("Result First Star")
    print((y+1)* 1000 + (4*(x+1)) + "ESWN".index(direct))

def second_star():
    curpos = list(grid.items())[0][0]
    direct = "E"
    for p in path:
        if p.isnumeric():
            for _ in range(int(p)):
                curpos,direct = move_2(curpos,direct)
        else:
            direct = compas.turnCompassPoint(direct,p,90)
    
    x,y = curpos

    print("Result Second Star")
    print((y+1)* 1000 + (4*(x+1)) + "ESWN".index(direct))

if __name__ == '__main__':
    main()