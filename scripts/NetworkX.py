###python -m pip install -U pip
#sudo apt install python3-pip
#pip3 install networkx
#sudo apt-get install python3-matplotlib
#python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
#sudo apt-get install python3.6-tk

import networkx as nx
import math
import matplotlib.pyplot as plt

G = nx.Graph()
elist = [(1, 2), (2, 3), (1, 4), (4, 2)]
G.add_edges_from(elist)
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
G.add_weighted_edges_from(elist)

#___________________________________________________________________
#funktioniert noch nicht die Darstellung
G = nx.cubical_graph()
plt.subplot(121)
nx.draw(G)# default spring_layout
plt.subplot(122)
nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b') #10.1  Matplotlib
