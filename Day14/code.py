import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
grid  = []
xy = [500,0]
end=0
xx,yy = set(),set()
def readinput():
    global input
    global xy
    input = readinput_lines("Day14\input.txt")
    global grid
    global end
    global xx,yy
    xx,yy= set(),set()
    for i in range(1000):
        grid.append([])
        for j in range(700):
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

    end=max(yy)+1

  
def main():
   readinput()
   #first_star()
   second_star()        
          
def first_star():
    x,y = xy
    cnt=0
    while y<end:
        cnt+=1
        x,y = xy
        x,y= drop(x,y)
        grid[y][x] = 2
    
    for idx,row in enumerate(grid[min(yy):max(yy)]):
        print(idx,"".join(".#O"[col] for col in row[min(xx):max(xx)]))

    print("Result First Star")
    print(cnt-1)

def second_star():
    for i in range(len(grid[0])):
        grid[end+1][i] = 1


    x,y = 0,1
    cnt=0
    while y>0:
        cnt+=1
        x,y = xy
        x,y= drop(x,y)
        grid[y][x] = 2

    print("Result Second Star")
    print(cnt)

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

    if y>end + 2 or x+1 == 700:
        return x,y+1

    return drop(x,y)

if __name__ == '__main__':
    main()