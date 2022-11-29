import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines("Day1\input.txt")
  
def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():
    if second_star() != "NYI" : return
    print("Result First Star")

def second_star():
    return "NYI"

    print("Result Second Star")

if __name__ == '__main__':
    main()