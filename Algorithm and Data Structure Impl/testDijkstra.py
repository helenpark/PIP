# import Graph
import myDijkstra



g = myDijkstra.Graph()
g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')
g.add_node('e')
g.add_node('f')

g.add_edge('a', 'b', 1)
g.add_edge('a', 'c', 1)
g.add_edge('b', 'd', 1)
g.add_edge('b', 'e', 1)
g.add_edge('c', 'f', 1)
g.add_edge('c', 'd', 1)
g.add_edge('c', 'f', 1)
g.add_edge('d', 'e', 1)
g.add_edge('e', 'f', 1)

# ////////////////////////////// PSEUDO CODE

#  1  function Dijkstra(Graph, source):
#  2
#  3      create vertex set Q
#  4
#  5      for each vertex v in Graph:             // Initialization
#  6          dist[v] = INFINITY                  // Unknown distance from source to v
#  7          prev[v] = UNDEFINED                 // Previous node in optimal path from source
#  8          add v to Q                          // All nodes initially in Q (unvisited nodes)
#  9
# 10      dist[source] = 0                        // Distance from source to source
# 11      
# 12      while Q is not empty:
# 13          u = vertex in Q with min dist[u]    // Node with the least distance will be selected first
# 14          remove u from Q 
# 15          
# 16          for each neighbor v of u:           // where v is still in Q.
# 17              alt = dist[u] + length(u, v)
# 18              if alt < dist[v]:               // A shorter path to v has been found
# 19                  dist[v] = alt 
# 20                  prev[v] = u 
# 21
# 22      return dist[], prev[]


# /////////////////////////////// TRIAL #2 MY OWN FROM PSEUDO CODE

def dijkstra(graph, source):
	prev = {}
	q = graph.nodes
	dist = {}
	for v in q:
		dist[v] = float('inf')
		prev[v] = None
		q.add(v)
	dist[source] = 0
	while q:
		cur = minimum_distance(dist, q)
		q.remove(cur)

		for neighbor in graph.edges[cur]:
			alt = dist[cur] + graph.distances[(neighbor, cur)]
			if alt < dist[neighbor]:
				dist[neighbor] = alt
				prev[neighbor] = cur
	return prev



#//////////////////////////////// TRIAL #1 ONLINE

# def dijkstra(graph, source):

# 	vertices = graph.nodes
# 	dist = dict() # distance travelled thus far
# 	previous = dict()

# 	for vertex in vertices:
# 	    dist[vertex] = float("inf") # infinitely large amount
# 	    previous[vertex] = None

# 	dist[source] = 0
# 	Q = set(vertices) # queue!

# 	while len(Q) > 0:
# 	    u = minimum_distance(dist, Q) # calls helper function to find closes path so far -> return node
# 	    print('Currently considering', u, 'with a distance of', dist[u])
# 	    Q.remove(u)

# 	    if dist[u] == float('inf'): # terminate because you know that there are no more nodes that are connected to the source
# 	        break

# 	    n = graph.edges[u]
# 	    for vertex in n:
# 	        alt = dist[u] + dist_between(graph, u, vertex)
# 	        if alt < dist[vertex]:
# 	            dist[vertex] = alt
# 	            previous[vertex] = u

# 	return previous # ???




def minimum_distance(d, s):
	minimum = float("inf")
	minElem = None
	for elem in s:
		minimum = min(d[elem], minimum)
		minElem = elem
	return minElem

print dijkstra(g, 'a')