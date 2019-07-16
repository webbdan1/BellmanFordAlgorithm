from Graph import Graph
from GraphSolution import GraphSolution

stu = Graph()
w = (1,2)
x = (1,3)
y = (2,3)
z = (2,4)
a = (3,4)

stu.construct_edge(w)
stu.construct_edge(x)
stu.construct_edge(y)
stu.construct_edge(z)
stu.construct_edge(a)
print("Your Graph structure:")
for k, v in stu.adj_list.items():
    print(k, v, [repr(e) for e in v.edges])

print("\n")

solution = GraphSolution()
print("Solution Graph structure:")
solution.construct_edge(w)
solution.construct_edge(x)
solution.construct_edge(y)
solution.construct_edge(z)
solution.construct_edge(a)
for k, v in solution.adj_list.items():
    print(k, v, [repr(e) for e in v.edges])
    
assert(solution.adj_list == stu.adj_list)
