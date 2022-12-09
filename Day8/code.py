import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []

def readinput():
   global input
   input = readinput_lines("Day8\input_ex.txt")
  
def main():
   readinput()
   #first_star()
   #second_star()   
   try_out()

  
def first_star():
    t=0
    for ir,r in enumerate(input):
        for ic,c in enumerate(r):
            v1,v2,v3,v4=True,True,True,True 
            for i in range(0, ic):
                val = int(input[ir][i])
                if val >= int(c):
                    v1=False
           
            for i in range(ic+1, len(r)):
                val = int(input[ir][i])
                if val >= int(c):
                    v2=False
            
            for i in range(0, ir):
                val = int(input[i][ic])
                if val >= int(c):
                    v3=False
          
            for i in range(ir+1, len(input)):
                 val = int(input[i][ic])
                 if val >= int(c):
                    v4=False
            if v1 or v2 or v3 or v4:
                t+=1
                
    print("Result First Star")
    print(t)
   
def second_star():
    t=[]
    for ir,r in enumerate(input):
        for ic,c in enumerate(r):
            v1,v2,v3,v4=0,0,0,0 
            for i in range(ic - 1, -1, -1):
                val = int(input[ir][i])
                v1+=1
                if val >= int(c):                   
                    break
           
            for i in range(ir - 1, -1, -1):
                val = int(input[i][ic])
                v2+=1
                if val >= int(c):
                    break
            
            for i in range(ic + 1, len(r)):
                val = int(input[ir][i])
                v3+=1
                if val >= int(c):
                    break
          
            for i in  range(ir + 1, len(r)):
                 val = int(input[i][ic])
                 v4+=1
                 if val >= int(c):
                    break
            t.append(v1*v2*v3*v4)
           
    print("Result Second Star")
    print(max(t))

def try_out():
    start = len(input)
    t=0
    s = readinput_lines_as_str("Day8\input_ex.txt")
    r= ''.join(s[i] for i in range(start,len(s)-start) if (i+1)%start and (i)%start)
    for i,c in enumerate(r):
        row=(math.floor(i/(start-2)) + 1) * start
        t+= (all(s[j] <= c for j in range(i,start+(i+1),start))
          or all(s[j] <= c for j in range(start+(i+1),len(s)-start,start))
          or all(s[j] <= c for j in range(row,row+i+1))
          or all(s[j] <= c for j in range(row+i+2,row+start)))
        for j in range(i-start,start+(i+1),start):
            print(c, s[j],all(s[j] <= c for j in range(i,start+(i+1),start)))
            print("-----")

           
    print("Result Second Star")
    print(t)
if __name__ == '__main__':
    main()