import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
se,be=[],[]
def readinput():
    global input
    global se,be
    input = readinput_lines("Day15\input_ex.txt")
    
    for s in input:
        se.append((int(s.split("x=")[1].split(",")[0]),int(s.split("y=")[1].split(",")[0].split(":")[0])))
        be.append((int(s.split("x=")[2].split(",")[0]),int(s.split("x=")[2].split(",")[1].split("=")[1])))
    print(se,be)
        
   
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