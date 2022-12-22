import math
import os, sys
from sympy import *
from operator import add,sub,mul,floordiv,eq
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines("Day21\input.txt")
  
def main():
   readinput()
   first_star()
   #second_star()   
   
def calc(monkeys, monkey):
    m = monkeys[monkey]
    if type(m) == type(0):
         return monkeys[monkey]   

    return m[1](calc(monkeys, m[0]), calc(monkeys,m[2]))       
              

def first_star():
    #152
    oper= { "+" : add, "-":sub,"/" : floordiv,"*":mul}
    monkeys = {}
    for line in input:
        s=line.split(":")
        monkeys[s[0]] = s[1].strip()
        if monkeys[s[0]].isnumeric():
            monkeys[s[0]] = int(monkeys[s[0]])
        else:
            a,o,b = monkeys[s[0]].split()
            monkeys[s[0]] = a,oper[o],b
  
    print("Result First Star")
    print(calc(monkeys,"root"))

def second_star():
    #301
    # Not found :(
    oper= { "+" : add, "-":sub,"/" : floordiv,"*":mul}
    monkeys = {}
    for line in input:
        s=line.split(":")
        monkeys[s[0]] = s[1].strip()
        if monkeys[s[0]].isnumeric():
            monkeys[s[0]] = int(monkeys[s[0]])
        else:
            a,o,b = monkeys[s[0]].split()
            monkeys[s[0]] = a,oper[o],b

    a,o,b = monkeys["root"]
    monkeys["root"] = a,eq,b
    monkeys["humn"] = None
    
    #root: rvrh + hzgl
    #15423341791001.0
    #43583341796964
    #15423341796968
    #5697586809113.0
    #5697586809113.0
    #15423341799501
    
    print(21120928600114*2)

    print(calc(monkeys,"root"))
      
    print("Result Second Star")
    #print(calc(monkeys,"root"))

if __name__ == '__main__':
    main()