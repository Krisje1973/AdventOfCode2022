import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
from collections import deque
input = []
def readinput():
   global input
   input = readinput_lines_as_ints("Day20\input.txt")
   
def main():
   readinput()
   first_star()
   #second_star()        
          
def first_star():
    que = deque((id, int(x)) for id, x in enumerate(input))
    init = list(que)
 
    for idx, i in enumerate(init):
        while que[0][0] != idx:
            que.rotate(-1)
 
        que.popleft()
        que.rotate(-i[1])
        que.appendleft(i)
       

    while que[0][1] != 0:
        que.rotate(-1)   
    
    print("Result First Star")
    print(que[1000 % len(que)][1] + que[2000 % len(que)][1] + que[3000 % len(que)][1])
   
def second_star():
    que = deque((id, int(x)*811589153) for id, x in enumerate(input))
    init = list(que)
 
    for _ in range(10):
        for idx, i in enumerate(init):
            while que[0][0] != idx:
                que.rotate(-1)
    
            que.popleft()
            que.rotate(-i[1])
            que.appendleft(i)
       

    while que[0][1] != 0:
        que.rotate(-1)   
    
    print("Result First Star")
    print( que[1000 % len(que)][1] + que[2000 % len(que)][1] + que[3000 % len(que)][1])
 
    print("Result Second Star")
 
if __name__ == '__main__':
    main()
