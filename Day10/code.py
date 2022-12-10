import math
import numpy as np
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 

input = []
def readinput():
   global input
   input = readinput_lines("Day10\input.txt")
  
def main():
   readinput()
   #first_star()
   second_star()        
          
def first_star():
    x=1
    cycle=0
    signal=0
    for line in input:
        i= line.count("addx") + 1
        for j in range(i):
            cycle+=1
            signal += check_cycle(cycle,x)
        if i == 2:
            x += int(line.split()[1])    
        
    print("Result First Star")
    print(signal)

def check_cycle(cycle,x):
    if cycle == 20 or (cycle - 20) % 40 == 0:
        return x * cycle

    return 0

def second_star(): 
    x=1
    cycle=0
    row = -1
    crt =  [[ 0 for _ in range(40)] for _ in range(6)]
    for line in input:
        i= line.count("addx") + 1

        for _ in range(i):
            cm=cycle % 40 
            row += (cm == 0)
            crt[row][cm] = int(cm in (x- 1, x, x + 1))
            cycle+=1

        if i == 2:
            x += int(line.split()[1])    
        
    print("Result Second Star")
    for row in crt:
        print("".join(".#"[col] for col in row))
   
if __name__ == '__main__':
    main()