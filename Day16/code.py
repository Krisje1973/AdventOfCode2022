import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 

input = []
def readinput():
    global input
    regex = r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w ,]+)$"
    input = re.findall(regex,open_file("Day16\input_ex.txt"),re.MULTILINE)
  
def main():
   readinput()
   first_star()
   #second_star()        


def first_star():
    valves = defaultdict(str)
    

    for line in input:
        valves[line[0]] = Valve(line[0],int(line[1]),line[2])

    graph = Graph()
    G = defaultdict(list)
    for valve in valves:
        for tunnel in valves[valve].tunnels:
            #graph.add_edge({valve,tunnel})
            G[valve].append(tunnel)
   
   
    print(dag_shortest_path(G,"AA","FF"))
    print("Result First Star")
    

def second_star():
    return "NYI"

    print("Result Second Star")

class Valve():
    def __init__(self, id, rate, tunnels=""):
        self.id:str = id
        self.rate:int = rate
        self.tunnels = {}
        if tunnels != "":
            for tunnel in tunnels.split(", "):
                self.add_tunnel(tunnel)

    def add_tunnel(self,tunnel):
        self.tunnels[tunnel] = Valve(tunnel,0)

if __name__ == '__main__':
    main()