import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines("Day9\input.txt")
  
def main():
   readinput()
   #first_star()
   second_star()        
          
def first_star():
    #6318 to high
    h=(0,0)
    t=(-1,0)
    dirs = defaultdict(tuple)
    dirs["R"] = (1,0)
    dirs["L"] = (-1,0)
    dirs["U"] = (0,1)
    dirs["D"] = (0,-1)
    result = set()
    for line in input:
        d,c = line.split()
        
        for i in range(int(c)):
            move = dirs[d]
            h = tuple(map(sum,zip(h,move)))
            if h == t:
                continue

            s = tuple(a - b for a, b in zip(h, t))
            
            if (abs(s[0]),abs(s[1])) == (1, 1):
                continue

            if abs(s[1]) == 1 and s[0] ==0:
                continue

            if abs(s[0]) == 1 and s[1] ==0:
                continue

            t = tuple(map(sum,zip(h,(-move[0],-move[1]))))
            result.add(t)
    
    print("Result First Star")
    print(len(result)-1)
   
def second_star():
    dirs = defaultdict(tuple)
    dirs["R"] = (1,0)
    dirs["L"] = (-1,0)
    dirs["U"] = (0,1)
    dirs["D"] = (0,-1)
    result = set()
    snakes = [(0, 0) for i in range(10)]

    for line in input:
        d,c = line.split()
        
        for i in range(int(c)):
            move = dirs[d]
            snakes[0] = tuple(map(sum,zip(snakes[0],move)))
          
            for i,snake in enumerate(snakes[1:]):
                h,t=snakes[i],snake
                if h == t:
                    continue

                s = tuple(a - b for a, b in zip(h, t))
                
                if (abs(s[0]),abs(s[1])) == (1, 1):
                    continue

                if abs(s[1]) == 1 and s[0] == 0:
                    continue

                if abs(s[0]) == 1 and s[1] == 0:
                    continue

                a,b = s[0],s[1]
                if a == 2:
                    a = 1
                
                if b == 2:
                    b = 1

                if a == -2:
                        a = -1
                
                if b == -2:
                    b = -1
   
                snakes[i+1] = tuple(map(sum,zip(snakes[i+1],(a,b))))

            result.add(snakes[9])
            
    print("Result Second Star")
    print(len(result))

if __name__ == '__main__':
    main()