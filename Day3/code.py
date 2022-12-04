import numpy as np
import string
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
from collections import Counter

input = []
def readinput():
   global input
   global prio 
   input = readinput_lines("Day3\input.txt")
   prio = " " + string.ascii_lowercase + string.ascii_uppercase

def main():
   readinput()
   first_star()
   second_star()        
    
def first_star():
    print("Result First Star")
    print(sum(prio.index((dict.fromkeys(line[:len(line)//2],0).items() & dict.fromkeys(line[len(line)//2:],0).items()).pop()[0]) for line in input))

def second_star():
    result = 0
   
    print("Result Second Star")
    print(sum(prio.index((dict.fromkeys(line[0],0).items() & dict.fromkeys(line[1],0).items() & dict.fromkeys(line[2],0).items()).pop()[0]) 
            for line in np.array_split(input,len(input)//3)))

if __name__ == '__main__':
    main()