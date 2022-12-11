import math
import os, sys
from collections import deque,OrderedDict
from math import prod
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines_as_str("Day11\input.txt")
   
class Monkey():
    def __init__(self, id:int):
        self.id = id
        self.items:Item = []  
        self.operation:str = ""
        self.mod:int = 0
        self.throw_if_true:int = 0
        self.throw_if_false:int = 0

class Item():
    def __init__(self, worry:int):
        self.worry = worry

    def operate(self,inst:str):
        inst = inst.split("=")[1].replace("new", str(self.worry)).replace("old",str(self.worry))
        self.worry = math.floor(eval(inst) / 3)

    def operate_part2(self,inst:str,mod:int):
        inst = inst.split("=")[1].replace("new", str(self.worry)).replace("old",str(self.worry))
        self.worry = math.floor(eval(inst)) % mod

def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():
    monkeys = defaultdict(int)
    inspected = defaultdict(int)
    for monkey in input.split("Monkey")[1:]:
        t= monkey.split("Test: divisible by ")[1].split("If")[1:]
        o= monkey.split("Operation: ")[1].split("Test")[0]
        items= monkey.split("Starting items: ")[1].split(":")[0].split("Operation")[0].split(",")
        m= int(monkey.split("Starting items: ")[0].split(":")[0].strip())
        mo = Monkey(m)
        mo.mod=t
        mo.throw_if_true = int(t[0].split("monkey")[1])
        mo.throw_if_false = int(t[1].split("monkey")[1]) 
        mo.operation = o
        mo.mod = int(monkey.split("Test: divisible by ")[1].split("If")[0])
        for i in items:
            it = Item(int(i))
            mo.items.append(it)
        monkeys[m] = mo
        inspected[m] = 0
    for i in range(20):
        for monkey in monkeys.values():
            for item in monkey.items:
                inspected[monkey.id] += 1
                item.operate(monkey.operation)   
                if eval("" + str(item.worry) + " % " + str(monkey.mod)):
                    monkeys[monkey.throw_if_false].items.append(item)
                else : 
                    monkeys[monkey.throw_if_true].items.append(item)
            monkey.items = []

    print("Result First Star")
    res = sorted(inspected.values(), reverse=True)
    print(res[0] * res[1])

def second_star():
    monkeys = defaultdict(int)
    inspected = defaultdict(int)
    mods = []
    for monkey in input.split("Monkey")[1:]:
        t= monkey.split("Test: divisible by ")[1].split("If")[1:]
        o= monkey.split("Operation: ")[1].split("Test")[0]
        items= monkey.split("Starting items: ")[1].split(":")[0].split("Operation")[0].split(",")
        m= int(monkey.split("Starting items: ")[0].split(":")[0].strip())
        mo = Monkey(m)
        mo.mod=t
        mo.throw_if_true = int(t[0].split("monkey")[1])
        mo.throw_if_false = int(t[1].split("monkey")[1]) 
        mo.operation = o
        mo.mod = int(monkey.split("Test: divisible by ")[1].split("If")[0])
        mods.append(mo.mod)
        for i in items:
            it = Item(int(i))
            mo.items.append(it)
        monkeys[m] = mo
        inspected[m] = 0

    # https://www.geeksforgeeks.org/modular-exponentiation-python/
    mod = prod(m for m in mods)

    for i in range(10000):
        for monkey in monkeys.values():
            for item in monkey.items:
                inspected[monkey.id] += 1
                item.operate_part2(monkey.operation,mod) 
                if item.worry  %  monkey.mod:
                    monkeys[monkey.throw_if_false].items.append(item)
                else : 
                    monkeys[monkey.throw_if_true].items.append(item)
            monkey.items = []

    print("Result Second Star")
    res = sorted(inspected.values(), reverse=True)
    print(res[0] * res[1])
    

if __name__ == '__main__':
    main()