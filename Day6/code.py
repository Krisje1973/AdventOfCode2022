import math
import os, sys
from collections import deque,OrderedDict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_as_string("Day6\input.txt")[0]
  
def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():
    sp=deque(input[0:3])
    for idx,s in enumerate(input[3:]):
        sp.append(s)
        if len(set(sp)) == 4:
            break
        sp.popleft()

    print("Result First Star")
    print(idx+4)

def second_star():
    
    sp=deque(input[0:13])
    for idx,s in enumerate(input[13:]):
        sp.append(s)
        if len(set(sp)) == 14:
            break
        sp.popleft()

    print("Result Second Star")
    print(idx+14)
        
if __name__ == '__main__':
    main()