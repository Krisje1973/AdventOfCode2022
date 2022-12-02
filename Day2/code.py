import math
import os, sys
from itertools import permutations 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines("Day2\input.txt")
  
def main():
   readinput()
   first_star()
   second_star()

def first_star():
    result=0
    
    for line in input:
        elf,me = line.split()
        score = int(shift_string("360",-"ABC".index(elf))["XYZ".index(me)]) + " XYZ".index(me)
        result+=score

    print("Result First Star")
    print(result)
            
def second_star():
    result=0
    
    for line in input:
        elf,me = line.split()
        score = int("036"["XYZ".index(me)])
        score += int(shift_string("123","YZX".index(me))["ABC".index(elf)])
        result+=score

    print("Result Second Star")
    print(result)


if __name__ == '__main__':
    main()