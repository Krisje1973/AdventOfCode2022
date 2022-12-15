import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
grid  = []
xy = [500,0]
end=0
def readinput():
   global input
   global xy
   input = readinput_lines("Day14\input.txt")
  
def main():
   readinput()
   first_star()
   #second_star()        
          
def first_star():
    global grid
    global end
    xx,yy= set(),set()
    for i in range(1000):
        grid.append([])
        for j in range(540):
            grid[i].append(0)

    for line in input:
        x,y,s = 0,0,0
       
        for rock in line.split("->"):
            s+=1
            c,r = [int(i) for i in rock.split(",")] 
            
            if s==1:
                x,y = c,r
                continue

            if x==c:
                for i in range(min(y,r),max(y,r)+1):
                    grid[i][x] = 1
            if y==r:
                for i in range(min(x,c),max(x,c)+1):
                    grid[y][i] = 1
                   
            x,y = c,r
            xx.add(x)
            yy.add(y)   

    x,y = 500,0
    end=max(yy)+1
    cnt=0
    while y<end:
        cnt+=1
        x,y = 500,0
        x,y= drop(x,y)
        grid[y][x] = 2
    
   
    for idx,row in enumerate(grid[min(yy):max(yy)]):
        print(idx,"".join(".#O"[col] for col in row[min(xx):max(xx)]))

    print("Result First Star")
    print(cnt-1)

def drop(x,y):
    t=0
   
    if all([grid[y+1][x],grid[y+1][x-1],grid[y+1][x+1]]):
        return x,y

    if not grid[y+1][x]:
        y +=1
    else :

        if not grid[y+1][x-1]:
            x -=1
        else:
            if not grid[y+1][x+1]:
                x +=1

    if y>500 :
        return x,y+1
    return drop(x,y)

def second_star():
    return "NYI"

    print("Result Second Star")

if __name__ == '__main__':
    main()