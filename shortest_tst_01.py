from Graph import Graph
from GraphSolution import GraphSolution

w = (1, 2)
x = (1, 3)
y = (2, 3)
a = (3, 4)
t = (4, 5)
c = (4, 7)
d = (8,11)
e = (11, 5)

sol = GraphSolution()
stu = Graph()

stu.construct_edge(w)
stu.construct_edge(x)
stu.construct_edge(y)
stu.construct_edge(a)
stu.construct_edge(t)
stu.construct_edge(c)
stu.construct_edge(d)
stu.construct_edge(e)

sol.construct_edge(w)
sol.construct_edge(x)
sol.construct_edge(y)
sol.construct_edge(a)
sol.construct_edge(t)
sol.construct_edge(c)
sol.construct_edge(d)
sol.construct_edge(e)
#print("Your Graph structure:")
#for k, v in stu.adj_list.items():
#    print(k, v, [repr(e) for e in v.edges])

sturesult = stu.get_shortest_path(1,11)
solresult = sol.get_shortest_path(1,11)

print(sturesult)
assert(sturesult == solresult)

