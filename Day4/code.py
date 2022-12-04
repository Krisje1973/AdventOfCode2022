import math
import numpy as np
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 

input = []
def readinput():
   global input
   input = readinput_lines_with_separator("Day4\input.txt", ",")
  
def main():
   readinput()
   #first_star()
   second_star()        

def first_star():
    result = 0
    for arr in np.array_split(input, len(input)//2):
        pairs=[]
        for a in arr:
            for s in a.split("-"):
                pairs.append(int(s))
        if (pairs[0] <= pairs[2] and pairs[1] >= pairs[3]) or (pairs[0] >= pairs[2] and pairs[1] <= pairs[3]):
            result+=1

    print("Result First Star")
    print(result)

def second_star():
    print("Result Second Star")
    # Stupid but fun :)
    print(sum(list(map(lambda y:len(set(range(int(y[0][0]),int(y[0][1])+1))&set(range(int(y[1][0]),int(y[1][1])+1)))>0,map(lambda x: list(map(lambda s:s.split("-"),x)),np.array_split(input, len(input)//2))))))

if __name__ == '__main__':
    main()