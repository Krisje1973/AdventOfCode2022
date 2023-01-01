import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
from math import prod
from functools import total_ordering

input = []
compares = {}
def readinput():
   global input
   input = readinput_as_pairs("Day13\input.txt")
  
   compares[(int,int)] = lambda a,b: a-b
   compares[(list,int)] = lambda a,b: compares[list,list](a, [b])
   compares[(int,list)] = lambda a,b: compares[list,list]([a], b)
   compares[(list,list)] = lambda a,b: zip_list(a,b)

def main():
   readinput()
   #first_star()
   second_star() 

def zip_list(a,b):
    for x, y in zip(a, b):
        if result := compares[(type(x),type(y))](x,y):
            return result
    return len(a) - len(b)

@total_ordering
class order:
    def __init__(self, x):
            self.x = x
    def __lt__(self, other):
        return compares[(type(self.x),type(other.x))](self.x,other.x) < 0

    def __eq__(self, other):
        return compares[(type(self.x),type(other.x))](self.x,other.x) == 0


def first_star():
    #1523 = to low
    t=0
    for i, (a, b) in enumerate( [[eval(x) for x in line] for line in input]):
        if compares[(type(a),type(b))](a,b) < 0:
            t+=i+1

    print("Result First Star")
    print(t)    


def second_star():
    #33580 to high
    #24805
    li=[]
    input = readinput_lines_skip_enters("Day13\input.txt")
    for line in input:
        li.append(eval(line))
    li.append([2])
    li.append([6])
    li = sorted(li,key=order)
    
    print("Result Second Star")
    print((li.index([2])+1)*(li.index([6])+1))
    #print((li.index([2])+1)*(li.index([6])+1))


if __name__ == '__main__':
    main()

 






