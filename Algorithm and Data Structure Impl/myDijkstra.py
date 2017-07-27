from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def getNeighbours(self, vertex):
    return edges[vertex];

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node, from_node)] = distance
  
    # vertices, edges = graph
    # dist = dict() # distance travelled thus far
    # previous = dict()

    # for vertex in vertices:
    #     dist[vertex] = float("inf") # infinitely large amount
    #     previous[vertex] = None

    # dist[source] = 0
    # Q = set(vertices) # queue!

    # while len(Q) > 0:
    #     u = minimum_distance(dist, Q) # calls helper function to find closes path so far
    #     print('Currently considering', u, 'with a distance of', dist[u])
    #     Q.remove(u)

    #     if dist[u] == float('inf'): # ???
    #         break

    #     n = get_neighbours(graph, u)
    #     for vertex in n:
    #         alt = dist[u] + dist_between(graph, u, vertex)
    #         if alt < dist[vertex]:
    #             dist[vertex] = alt
    #             previous[vertex] = u

    # return previous

# def dijsktra(graph, source, target):
#   visited = set() # set of nodes already visited
#   queue = [source] # queue of nodes need to visit
#   paths = {} # dict of node : shortest path contents

#   while queue:
#     vertex = queue.pop()
#     if vertex not in visited:
#       paths
#       if vertex == target: 
#         # return path
#         return ...

#       visited.append(vertex)
#       queue.append(getNeighbours(graph, vertex) - visited)

#   # no path found
#   return ...

# ...........
  def dijkstra(graph, source):

    vertices, edges = graph
    dist = dict() # distance travelled thus far
    previous = dict()

    for vertex in vertices:
        dist[vertex] = float("inf") # infinitely large amount
        previous[vertex] = None

    dist[source] = 0
    Q = set(vertices) # queue!

    while len(Q) > 0:
        u = minimum_distance(dist, Q) # calls helper function to find closes path so far
        print('Currently considering', u, 'with a distance of', dist[u])
        Q.remove(u)

        if dist[u] == float('inf'): # ???
            break

        n = graph.edges[u]
        for vertex in n:
            alt = dist[u] + dist_between(graph, u, vertex)
            if alt < dist[vertex]:
                dist[vertex] = alt
                previous[vertex] = u





def minimum_distance(d, s):
  minimum = float("inf")
  minElem = None
  for elem in s:
    minimum = min(d[elem], minimum)
    minElem = elemm
  return minElem

    # self.nodes = set()
    # self.edges = defaultdict(list)
    # self.distances = {}



















