
# Dijkstra Shortest Path pseudo code

#  1  function Dijkstra(Graph, source):
#  2
#  3      create vertex set Q
#  4
#  5      for each vertex v in Graph:             // Initialization
#  6          dist[v] ← INFINITY                  // Unknown distance from source to v
#  7          prev[v] ← UNDEFINED                 // Previous node in optimal path from source
#  8          add v to Q                          // All nodes initially in Q (unvisited nodes)
#  9
# 10      dist[source] ← 0                        // Distance from source to source
# 11      
# 12      while Q is not empty:
# 13          u ← vertex in Q with min dist[u]    // Node with the least distance will be selected first
# 14          remove u from Q 
# 15          
# 16          for each neighbor v of u:           // where v is still in Q.
# 17              alt ← dist[u] + length(u, v)
# 18              if alt < dist[v]:               // A shorter path to v has been found
# 19                  dist[v] ← alt 
# 20                  prev[v] ← u 
# 21
# 22      return dist[], prev[]

def dijkstra(graph, source):

    vertices, edges = graph
    dist = dict()
    previous = dict()

    for vertex in vertices:
        dist[vertex] = float("inf") # infinitely large amount
        previous[vertex] = None

    dist[source] = 0
    Q = set(vertices)

    while len(Q) > 0:
        u = minimum_distance(dist, Q)
        print('Currently considering', u, 'with a distance of', dist[u])
        Q.remove(u)

        if dist[u] == float('inf'): 
            break

        n = get_neighbours(graph, u)
        for vertex in n:
            alt = dist[u] + dist_between(graph, u, vertex)
            if alt < dist[vertex]:
                dist[vertex] = alt
                previous[vertex] = u

    return previous

def dijkstra2(graph, source):
	nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
	distances = {
	    'B': {'A': 5, 'D': 1, 'G': 2},
	    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
	    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
	    'G': {'B': 2, 'D': 1, 'C': 2},
	    'C': {'G': 2, 'E': 1, 'F': 16},
	    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
	    'F': {'A': 5, 'E': 2, 'C': 16}}

	unvisited = {node: None for node in nodes} #using None as +inf
	visited = {}
	current = 'B'
	currentDistance = 0
	unvisited[current] = currentDistance

	while True:
	    for neighbour, distance in distances[current].items():
	        if neighbour not in unvisited: continue
	        newDistance = currentDistance + distance
	        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
	            unvisited[neighbour] = newDistance
	    visited[current] = currentDistance
	    del unvisited[current]
	    if not unvisited: break
	    candidates = [node for node in unvisited.items() if node[1]]
	    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

	print(visited)
	return visited









