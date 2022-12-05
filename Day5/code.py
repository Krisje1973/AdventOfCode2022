import math
import os, sys
import string
from collections import deque,OrderedDict
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []

def readinput():
    global input
    input = readinput_lines_no_strip("Day5\input.txt")
  
def main():
   readinput()
   first_star()
   second_star()    

def fix_data():
    stacks = defaultdict(deque)
    instructions = []
    e=False
    for line in input:
        if not e:
            for idx,s in enumerate(line):
                if string.ascii_uppercase.count(s) > 0:
                    stacks[math.floor(idx/4)+1].append(s)

        if e:
            s = line.strip().split(" ")
            a,b,c = int(s[1]),int(s[3]),int(s[5])
            instructions.append([a,b,c])

        if line.count("[") == 0:
            e = True 
    return stacks,instructions

def first_star():
    stacks,instructions = fix_data()
    for inst in instructions:
        a, b, c = inst
        for i in range(a):
            stacks[c].appendleft(stacks[b].popleft())
 
    print("Result First Star")
    print("".join(st[0] for st in OrderedDict(sorted(stacks.items())).values() if len(st) > 0))

def second_star():
    stacks,instructions = fix_data()
    for inst in instructions:
        a, b, c = inst
        li=deque()
        for i in range(a):
            li.appendleft(stacks[b].popleft())
        stacks[c].extendleft(li)

    print("Result Second Star")
    print("".join(st[0] for st in OrderedDict(sorted(stacks.items())).values() if len(st) > 0))

if __name__ == '__main__':
    main()