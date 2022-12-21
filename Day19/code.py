from itertools import compress, product
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
blueprints = [] 
def readinput():
    global input
    global blueprints
    input = readinput_lines("Day19\input.txt")
   
    for line in input:
        id = int(line.split("Blueprint")[1].split(":")[0])
        ore = int(line.split("Each ore robot costs")[1].split(" ")[1])
        clay = int(line.split("Each clay robot costs")[1].split(" ")[1])
        obsidian_ore = int(line.split("Each obsidian robot costs")[1].split(" ")[1])
        obsidion_clay = int(line.split("Each obsidian robot costs")[1].split(" and ")[1].split(" ")[0])
        geode_ore = int(input[0].split("Each geode robot costs")[1].split(" ")[1])
        geode_obsidian = int(input[0].split("Each geode robot costs")[1].split(" and ")[1].split(" ")[0])
        blueprints.append(Blueprint(id,ore,clay,obsidian_ore,obsidion_clay,geode_ore,geode_obsidian))
 

def main():
   readinput()
   first_star()
   #second_star()        
          
def first_star():
    print(list(combinations(range(3))))
    #calculate(1,blueprints[0])
    print("Result First Star")

def combinations(items):
    return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )
    # alternative:   

def second_star():
    return "NYI"

    print("Result Second Star")

def calculate(time,blueprint,ore,clay,):
    ore,clay,obsidian,geode = 0,0,0,0,0
    for i in range(time):
        for _ in range(blueprint.ore_robots):
            ore+=1
        for _ in range(blueprint.clay_robots):
            clay+=1
        for _ in range(blueprint.obsidian_robots):
            obsidian+=1
        for _ in range(blueprint.geode_robots):
            geode+=1
        

        if ore % blueprint.cost_ore_robot == 0 and blueprint.ore_robots < idx_ore:
            ore-=blueprint.cost_ore_robot
            blueprint.ore_robots+= 1
        for idx_ore in range(3):
            print(idx_ore)

        

class Blueprint():
    def __init__(self, id, ore,clay,obsidian_ore,obsidian_clay,geode_ore,geode_obsidian):
        self.id:int = id
        self.cost_ore_robot:int = ore
        self.cost_clay_robot:int = clay
        self.cost_obsidian_robot_ore:int = obsidian_ore
        self.cost_obsidian_robot_clay:int = obsidian_clay
        self.cost_geode_robot_ore:int = geode_ore
        self.cost_geode_robot_obsidian:int = geode_obsidian
        self.ore_robots = 0
        self.clay_robots = 0
        self.obsidian_robots = 0
        self.geode_robots = 0
        self.ore_inventory = 0
        self.clay_inventory  = 0
        self.obsidian_inventory  = 0
        self.geode_inventory = 0  

if __name__ == '__main__':
    main()