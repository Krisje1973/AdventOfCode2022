import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
grid = {}
def readinput():
    global input,grid
    input = readinput_lines("Day24\input_ex.txt")
    lines = [row[1:-1] for row in input[1:-1]]
    grid = {(i, j): cell for i, row in enumerate(lines) for j, cell in enumerate(row)}


def main():
   readinput()
   first_star()
   #second_star()        
          
def first_star():
    print(grid)
    g = BfsGraph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
    g.BFS(2)
    print("Result First Star")

def second_star():
    return "NYI"

    print("Result Second Star")

if __name__ == '__main__':
    main()

