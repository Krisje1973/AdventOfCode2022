import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
import string
from queue import PriorityQueue
input = []
def readinput():
   global input
   input = readinput_lines("Day12\input_ex.txt")
  
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
        
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

def main():
   readinput()
   first_star()
   #second_star()        
          
def first_star():
    graph = defaultdict(dict)
    
    grid = {
        (i, j): x
        for i, row in enumerate(input)
        for j, x in enumerate(row)
    }
    for g in grid:
        graph[g] = add_tuples(g,Compass())

    graph = {
        'a': {'b': 5, 'c': 2},
        'b': {'a': 5, 'c': 7, 'd': 8},
        'c': {
            'a': 2,
            'b': 7,
            'd': 4,
            'e': 8,
            },
        'd': {
            'b': 8,
            'c': 4,
            'e': 6,
            'f': 4,
            },
        'e': {'c': 8, 'd': 6, 'f': 3},
        'f': {'e': 3, 'd': 4},
        }

    source = 'a'
    destination = 'f'

    unvisited = graph
    shortest_distances = {}
    route = []
    path_nodes = {}

    for nodes in unvisited:
        shortest_distances[nodes] = math.inf
    shortest_distances[source] = 0

    while unvisited:
        min_node = None
        for current_node in unvisited:
            if min_node is None:
                min_node = current_node
            elif shortest_distances[min_node] \
                > shortest_distances[current_node]:
                min_node = current_node
        for (node, value) in unvisited[min_node].items():
            if value + shortest_distances[min_node] \
                < shortest_distances[node]:
                shortest_distances[node] = value \
                    + shortest_distances[min_node]
                path_nodes[node] = min_node
        unvisited.pop(min_node)
    node = destination

    while node != source:
        try:
            route.insert(0, node)
            node = path_nodes[node]
        except Exception:
            print('Path not reachable')
            break
    route.insert(0, source)

    if shortest_distances[destination] != math.inf:
        print('Shortest distance is ' + str(shortest_distances[destination]))
        print('And the path is ' + str(route))
    print("Result First Star")

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths    	
   
   

def second_star():

    #nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    nodes = []
    init_graph = defaultdict(dict)
    rows=len(input)
    for y,line in enumerate(input):
        for x, s in enumerate(line):
            nodes.append((x,y))
    for y,line in enumerate(input):
        l=len(line)
        for x, s in enumerate(line):
            if s =="E":
                e=y*1000+x+1
            if s =="S":
                start=y*1000+x+1

            if x < l-1:
                if abs(string.ascii_lowercase.index(s.lower()) - string.ascii_lowercase.index(line[x+1].lower())) < 2 or string.ascii_lowercase.index(s.lower()) > string.ascii_lowercase.index(line[x+1].lower()) :
                    init_graph[(x,y)][(x+1,y)] = 1
                    #init_graph[(x+1,y)][(x,y)] = 1

            if y < rows -1:
                if abs(string.ascii_lowercase.index(s.lower()) - string.ascii_lowercase.index(input[y+1][x].lower())) < 2 or string.ascii_lowercase.index(s.lower()) > string.ascii_lowercase.index(input[y+1][x].lower()):
                     init_graph[(x,y)][(x,y+1)] = 1
                     #init_graph[(x,y+1)][(x,y)] = 1
            
   
    start_vertex = (0,0)
    end_vertex= (5,2)
    dijkstra = Dijkstra(nodes, init_graph)
    p, v = dijkstra.find_route(start_vertex, end_vertex)
    print("Distance from %s to %s is: %.2f" % (start_vertex, end_vertex, v[end_vertex]))
    se = dijkstra.generate_path(p, start_vertex, end_vertex)
    print("Path from %s to %s is: %s" % (start_vertex, end_vertex, " -> ".join(str(se))))   

    # distances = {
    #     'B': {'A': 5, 'D': 1, 'G': 2},
    #     'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    #     'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    #     'G': {'B': 2, 'D': 1, 'C': 2},
    #     'C': {'G': 2, 'E': 1, 'F': 16},
    #     'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    #     'F': {'A': 5, 'E': 2, 'C': 16}}

    

    print("Result Second Star")
class Dijkstra:
    
    def __init__(self, vertices, graph):
        self.vertices = vertices  # ("A", "B", "C" ...)
        self.graph = graph  # {"A": {"B": 1}, "B": {"A": 3, "C": 5} ...}

    def find_route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0  # set start vertex to 0
        visited = {}  # list of all visited nodes
        parents = {}  # predecessors
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)  # get smallest distance
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                new_distance = unvisited[min_vertex] + self.graph[min_vertex].get(neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == end:
                break
        return parents, visited

    @staticmethod
    def generate_path(parents, start, end):
        path = [end]
        while True:
            key = parents[path[0]]
            path.insert(0, key)
            if key == start:
                break
        return path

# modified BFS
def find_all_parents(G, s):
    Q = [s]
    parents = defaultdict(set)
    while len(Q) != 0:
        v = Q[0]
        Q.pop(0)
        for w in G.get(v, []):
            parents[w].add(v)
            Q.append(w) 
    return parents

# recursive path-finding function (assumes that there exists a path in G from a to b)   
def find_all_paths(parents, a, b): 
    return [a] if a == b else [y + b for x in list(parents[b]) for y in find_all_paths(parents, a, x)]
if __name__ == '__main__':
    main()