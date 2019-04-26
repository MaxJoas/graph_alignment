###python -m pip install -U pip
#sudo apt install python3-pip
#pip3 install networkx
#sudo apt-get install python3-matplotlib
#python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
#sudo apt-get install python3.6-tk

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

'''first number is the number of nodes; second is the edge probability, ergo a float between 0 and 1'''
G = nx.fast_gnp_random_graph(30, 0.1, seed=None, directed=False) 

'''
this changes the layout of the node display. Planar layout doesn't work with every graph. KK layout is pretty nice
(better than spring_layout) most of the time.
'''
#pos = nx.planar_layout(G) #no edge intersections
pos = nx.kamada_kawai_layout(G) #nice layout

nx.draw(G, pos, with_labels = 1) # default spring_layout

'''
The functions below return some properties about the graph
More functions like this can be found here:
https://networkx.github.io/documentation/networkx-1.10/reference/functions.html
'''
print("Directed? " + str(nx.is_directed(G)))
print("Number of nodes: " + str(nx.number_of_nodes(G)))
print("Nodes: " + str(nx.nodes(G)))

plt.show()
