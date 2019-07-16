from Graph import Graph
#test cases

#test 1: vertex test
vertex = Graph.Vertex(1)
vertex.add_edge(2)
vertex.add_edge(3)
vertex.add_edge(4)
vertex.add_edge(2)
edge1 = vertex.get_edge(2)
edge_none = vertex.get_edge(5)
assert(edge1.source == vertex and edge1.destination == 2)
assert(edge_none is None)

#test 2: path test
path = Graph.Path([])
assert(path.is_empty() is True)
path.remove_vertex()
assert(path.is_empty() is True)
vertex = Graph.Vertex(47)
path.add_vertex(vertex)
path.remove_vertex()
assert(path.is_empty() is True)
for i in range(5):
    vertex = Graph.Vertex(i)
    path.add_vertex(vertex.ID)
assert(path.is_empty() is False)
assert(path.last_vertex() == 4)
for i in range(3):
    path.remove_vertex()
assert(path.is_empty() is False)
path.remove_vertex()
path.remove_vertex()
assert(path.is_empty() is True)

#test 3: all subclasses
#path
assert(path.is_empty() is True)
assert(path.last_vertex() is None)
path.add_vertex(Graph.Vertex(8).ID)
assert(path.last_vertex() == 8)
assert(path.is_empty() is False)
path.add_vertex(Graph.Vertex(9).ID)
assert(path.last_vertex() == 9)
path.remove_vertex()
assert(path.last_vertex() == 8)
path.remove_vertex()
assert(path.is_empty() is True)
#vertex
vertex = Graph.Vertex(3)
assert vertex.ID == 3

assert vertex.pred_vertex == 0
assert vertex.distance == 0
assert vertex.get_edges() == []
assert vertex.get_edge(8) is None
vertex.add_edge(7)
vertex.add_edge(4)
vertex.add_edge(3)

assert vertex.get_edge(8) is None
assert vertex.get_edge(7) == Graph.Edge(vertex, 7)
#graph
graph = Graph()
assert graph.get_vertex(5) is None
graph.construct_edge((1,2))
graph.construct_edge((1,2))
one = graph.get_vertex(1)
two = graph.get_vertex(2)
assert one is not None
assert two is not None
assert one.get_edge(2) == Graph.Edge(one, 2)
assert two.get_edge(1) is None
assert len(graph.adj_list) == 2
assert len(one.edges) == 1
graph.construct_edge((1, 1))
assert len(graph.adj_list) == 2
assert len(one.edges) == 2
graph.construct_edge((2, 8))
assert(len(graph.adj_list) == 3)
graph.construct_edge((8, 1))
assert(len(graph.adj_list) == 3)
