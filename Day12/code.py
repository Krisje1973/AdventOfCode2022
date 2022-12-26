import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
import string
from queue import PriorityQueue
from collections import deque
input = []
def readinput():
   global input
   input = readinput_lines("Day12\input.txt")

def main():
   readinput()
   #first_star()
   second_star()        
          
def first_star():
    th = TupleHelper()
    
    grid = {
        (i, j): x
        for i, row in enumerate(input)
        for j, x in enumerate(row)
    }

    start = [k for k,v in grid.items() if v == "S"][0]
    end = [k for k,v in grid.items() if v == "E"][0]
    grid[start] = "a"
    grid[end] = "z" 

    dist = {}
    bfs = deque([(0, start)])

    while len(bfs) > 0:
        t, p = bfs.popleft()
        if p in dist:
            continue
        dist[p] = t

        for q in th.get_neighbours(p):
            # Not in Grid (|) or ascii > 1
            if ord(grid.get(q, "|")) - ord(grid[p]) > 1:
                continue
            # Valid diection 
            bfs.append((t + 1, q))
   
    print("Result First Star")
    print(dist[end])

def second_star():
    th = TupleHelper()
    grid = {
        (i, j): x
        for i, row in enumerate(input)
        for j, x in enumerate(row)
    }

    start = [k for k,v in grid.items() if v == "S"][0]
    end = [k for k,v in grid.items() if v == "E"][0]
    grid[start] = "a"
    grid[end] = "z" 

    starts = [k for k,v in grid.items() if v == "a"]
    ends=[]
    for start in starts:
        dist = {}
        bfs = deque([(0, start)])

        while len(bfs) > 0:
            t, p = bfs.popleft()
            if p in dist:
                continue
            dist[p] = t

            for q in th.get_neighbours(p):
                # Not in Grid (|) or neigbourgh > 1
                if ord(grid.get(q, "|")) - ord(grid[p]) > 1:
                    continue
                # Valid diection 
                bfs.append((t + 1, q))
        if end in dist:
            ends.append(dist[end])
   
    print("Result First Star")
    print(min(ends))

if __name__ == '__main__':
    main()