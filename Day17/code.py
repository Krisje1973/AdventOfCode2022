import math
import os, sys
from itertools import cycle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
rocks = []
def readinput():
    global input
    global rocks
    input = readinput_lines_as_str("Day17\input.txt")
    rs = ["00102030","1201112110","2221001020","03020100","01110010"]
    rocks = []
    for r in rs:
        rock = set()
        for i in range(1,len(r),2):
            rock.add(complex(int(r[i-1]),int(r[i])))
        rocks.append(rock)

def main():
   readinput()
   first_star()
   #second_star()        
          
def first_star():
    move = cycle(m for m in input)
    rock_cycle = cycle(rocks)
    grid =  set(complex(x -1) for x in range(7)) 
    jet = {"<": complex(-1,0j) ,">": complex(1,0j)}
    for _ in range(2022):
        start = complex(2 , 4 + max(r.imag for r in grid))    
        rock = {start + p for p in next(rock_cycle)}
        
        while True:
            j = jet[next(move)]
            new_rock = set(complex(r+j) for r in rock)
           
            if not new_rock & grid and all(0 <= p.real <= 6 for p in new_rock):
                rock = new_rock

            new_rock = {p - 1j for p in rock}
            if grid & new_rock:
                grid.update(rock)
                break

            rock = new_rock

    print("Result First Star")
    print(max(r.imag for r in grid))

def second_star():
    
    move = cycle(m for m in input)
    rock_cycle = cycle(rocks)
    grid =  set(complex(x -1) for x in range(7)) 
    jet = {"<": complex(-1,0j) ,">": complex(1,0j)}
    t=1_000_000_000_000
    for i in range(t):
        height = max(r.imag for r in grid)
        start = complex(2 , 4 + height)    
        rock = {start + p for p in next(rock_cycle)}

        mins = []
        for j in range(6):
            x = {complex(j,0j)}
            while not grid.intersection(x):
                y = x.pop()
                x= {complex(j,y-1j)}
            mins.append(x)

        while True:
            j = jet[next(move)]
            new_rock = set(complex(r+j) for r in rock)
           
            if not new_rock & grid and all(0 <= p.real <= 6 for p in new_rock):
                rock = new_rock

            new_rock = {p - 1j for p in rock}
            if grid & new_rock:
                grid.update(rock)
                break

            rock = new_rock

    print("Result Second Star")
    print(max(r.imag for r in grid))
if __name__ == '__main__':
    main()