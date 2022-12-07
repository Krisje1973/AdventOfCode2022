import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
from pathlib import Path,PurePosixPath
input = []
def readinput():
   global input
   input = readinput_lines("Day7\input.txt")
  
def main():
   readinput()
   #first_star()
   second_star()   

def first_star():
    #1128900 = to low
    #1642503
    dirs = defaultdict(int)
    p= Path("/")
    for line in input:
        s = line.split()
        if line.find("$") > -1:
            if line.find("cd") > -1 or line.find("dir") > -1:
                p = p / s[2]
                p = p.resolve()
               
        if s[0].isnumeric():
            dirs[p] += int(s[0])
            for path in p.parents:
                dirs[path] += int(s[0])
    
    print(sum(x for x in dirs.values() if x <= 100000))

def second_star():
    dirs = defaultdict(int)
    p= Path("/")
    for line in input:
        s = line.split()
        if line.find("$") > -1:
            if line.find("cd") > -1 or line.find("dir") > -1:
                p = p / s[2]
                p = p.resolve()
               
        if s[0].isnumeric():
            dirs[p] += int(s[0])
            for path in p.parents:
                dirs[path] += int(s[0])

    p = p / "/"
    h= dirs[p.resolve()]
    d=abs(70000000-h-30000000)
    
    print("Result Second Star")
    print(list(x for x in sorted(dirs.values()) if x>= d)[0])

if __name__ == '__main__':
    main()