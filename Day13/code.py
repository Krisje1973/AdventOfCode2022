import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
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
    li=[]
    input = readinput_lines_skip_enters("Day13\input.txt")
    for line in input:
        #li.append(str(line.replace("[","").replace("]","")))
        li.append(str(line))
    li.append("[[2]]")
    li.append("[[6]]")
    li.sort()
    for l in li:
        print(l)
    print((li.index("[[2]]")+1))
    print("Result Second Star")
 

if __name__ == '__main__':
    main()

 






