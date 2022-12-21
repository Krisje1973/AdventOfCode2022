import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 

input =set()
def readinput():
    global input
    input = readinput_lines("Day18\input_ex.txt")
    pos =set()
    for line in input:
        x,y,z = line.split(',')
        x,y,z = map(int,[x,y,z])
        pos.add((x,y,z))
    input = pos
    

def main():
   readinput()
   #first_star()
   second_star()        
          
def first_star():
    h = GridHelper()
    sur = [(0, 0, 1),(0, 1, 0),(1, 0, 0),
           (0, 0, -1),(0, -1, 0),(-1, 0, 0)]
    t=0
    for pos in input:
        for side in sur:
            if tuple(sum(tup) for tup in zip(pos, side)) not in input:
                t+=1       

    print("Result First Star")
    print(t)
    
def second_star():
    h = GridHelper()
    sur = [(0, 0, 1),(0, 1, 0),(1, 0, 0),
           (0, 0, -1),(0, -1, 0),(-1, 0, 0)]
    
    neigh=set()
    all= set
    sides=defaultdict(set)
    t=0
    for pos in input:
        for side in sur:
            nei = tuple(sum(tup) for tup in zip(pos, side))
            neigh.add(nei)
            sides[pos].add(nei)

    others = set()
    for x in range(max(x for x, y, z in input) + 1):
        for y in range(max(y for x, y, z in input) + 1):
            for z in range(max(z for x, y, z in input) + 1):
                if (x, y, z) not in input:
                    others.add((x, y, z))

    min_coords = tuple(min(x) - 1 for x in zip(*input))
    max_coords = tuple(max(x) + 1 for x in zip(*input))
    print(max_coords)
      
    # for idx,nei in enumerate(input):
          
    #     print(sum(n in sides for n in nei))
       


   
    print("Result Second Star")
    print(t,len(input),len(neigh))
if __name__ == '__main__':
    main()