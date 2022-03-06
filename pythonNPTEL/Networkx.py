import networkx as nx
import matplotlib.pyplot as plt

# Creating a normal graph
G = nx.Graph()

l = [1,2,3]
G.add_nodes_from(l)

'''G.add_node(1)
G.add_node(2)
G.add_node(3)'''

G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

print(G.nodes())
print(G.edges())

nx.draw(G)
plt.show()

# Creating a complete graph
G = nx.complete_graph(21)

nx.draw(G)
plt.show()

# Creating a random graph

G = nx.gnp_random_graph(20,0.2)
print(G.edges())
nx.draw(G)
plt.show()

nx.write_gexf(G,"test.gexf")
