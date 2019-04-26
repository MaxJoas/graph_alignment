###python -m pip install -U pip
#sudo apt install python3-pip
#pip3 install networkx
#sudo apt-get install python3-matplotlib
#python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
#sudo apt-get install python3.6-tk

import networkx as nx
import math
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import json

G = nx.Graph()
elist = [(1, 2), (2, 3), (1, 4), (4, 2)]
G.add_edges_from(elist)
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
G.add_weighted_edges_from(elist)
#___________________________________________________________________________


G = nx.fast_gnp_random_graph(30, 0.25, seed=None, directed=False) #fast_gnp_random_graph(n, p, seed=None, directed=False)[source]

#G = nx.balanced_tree(3, 3) #balanced_tree(r, h[, create_using]) #nx.random_tree(6[, 1]) #nx.random_tree(n[, seed])
#___________________________________________________________________
#funktioniert noch nicht die Darstellung
#G = nx.cubical_graph()
#plt.subplot(121)
nx.draw(G, with_labels = 1) # default spring_layout
plt.show()
#plt.subplot(122)
#nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b') #10.1  Matplotlib
data = json_graph.tree_data(G,root=1) #only saves directed Tree Graphs :/

#nx.complete _graph(10) #all with all
#.order() #Kanten
#.size()  #Label
