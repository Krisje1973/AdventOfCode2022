import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
stacks = {}
instructions = []
def readinput():
    global input
    global stacks
    global instructions
    input = readinput_lines("Day5\input_ex.txt")
    c=0
    for line in input:
        cc=line.count("[") 

        if cc > len(stacks):
            stacks[cc] = []

        if line.count("[") == 0 and line != "":
            s = line.split(" ")
            a,b,c = s[1],s[3],s[5]
            instructions.append([a,b,c])
        print(line)
        print(line.count(" "))
    
    instructions = instructions[2:]

  
def main():
   readinput()
   first_star()
   #second_star()        

def move(q,f,t):
    x = 0     
def first_star():
   
    print(stacks)
    print("Result First Star")

def second_star():
    return "NYI"

    print("Result Second Star")

if __name__ == '__main__':
    main()