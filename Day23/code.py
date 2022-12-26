import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
from collections import Counter, deque
input = []
grid = {}
compas = Compass()
def readinput():
    global input,grid,compas
    input = readinput_lines_no_strip_no_enter("Day23\input.txt")   
    grid = {(x, y): ".#".index(cell) for y, row in enumerate(input) for x, cell in enumerate(row) if cell != " "}
  
def main():
   readinput()
   #first_star()
   second_star()        

def check(pos,checks):
    # If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
    # If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
    # If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
    # If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.  
    for d in checks:
        nb=False
        for n in compas.getHexasPoints(d):
            new = add_tuples(pos,n)
            if new in grid and grid[new]:
                nb= True
        if not nb: 
            return add_tuples(pos,compas.compasspoints[d])

    return pos

def first_star():
    checks = deque("NSWE")
    for _ in range(10):
        elves = {k for k in grid if grid[k]}
        newelves = defaultdict(list)

        for elf in elves:
            newelves[check(elf,checks)].append(elf)

        new = {elf for elf in newelves if len(newelves[elf]) == 1} 
        old = [newelves[elf] for elf in newelves if len(newelves[elf]) > 1]
        
        grid.clear()
        for n in new:
            grid[n] = 1
        for ol in old:
            for o in ol:
                grid[o] = 1
        
        checks.rotate(-1)
    
    elves = {k for k in grid if grid[k]}
    xs, ys = zip(*elves)
 
    print("Result First Star")    
    print(sum((i, j) not in elves for i in range(min(xs)-1, max(xs) + 1) for j in range(min(ys), max(ys) + 1))+1)

def second_star():
    checks = deque("NSWE")
    t=0
    for _ in range(10000):
        t+=1
        elves = {k for k in grid if grid[k]}
        newelves = defaultdict(list)

        for elf in elves:
            newelves[check(elf,checks)].append(elf)

        new = {elf for elf in newelves if len(newelves[elf]) == 1} 
        old = [newelves[elf] for elf in newelves if len(newelves[elf]) > 1]           

        grid.clear()
        for n in new:
            grid[n] = 1
        for ol in old:
            for o in ol:
                grid[o] = 1

        ch = {k for k in grid if grid[k]}
        if not elves.difference(ch):
            print(t)
            break

        
        checks.rotate(-1)
    
    elves = {k for k in grid if grid[k]}
    
    print("Result Second Star")
    print(t)
if __name__ == '__main__':
    main()