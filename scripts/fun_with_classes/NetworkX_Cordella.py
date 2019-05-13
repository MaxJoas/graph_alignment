###python -m pip install -U pip
#sudo apt install python3-pip
#pip3 install networkx
#sudo apt-get install python3-matplotlib
#python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
#sudo apt-get install python3.6-tk

#sudo apt-get install python3-scipy

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import isomorphism

G1 = G2 = nx.Graph()

'''first number is the number of nodes; second is the edge probability, ergo a float between 0 and 1'''

G1 = nx.fast_gnp_random_graph(30, 0.01, seed=None, directed=True)
G2 = nx.fast_gnp_random_graph(30, 0.01, seed=None, directed=True)

'''
this changes the layout of the node display. Planar layout doesn't work with every graph. KK layout is pretty nice
(better than spring_layout) most of the time.
'''
pos1 = nx.kamada_kawai_layout(G1) #nice layout
pos2 = nx.kamada_kawai_layout(G2)
plt.figure(1)
nx.draw(G1, pos1, with_labels = 1)
plt.figure(2)
nx.draw(G2, pos2, with_labels = 1)
'''
The functions below return some properties about the graph
More functions like this can be found here:
https://networkx.github.io/documentation/networkx-1.10/reference/functions.html
'''
print("Graph1: ")
print("Directed? " + str(nx.is_directed(G1)))
print("Number of nodes: " + str(nx.number_of_nodes(G1)))
print("Nodes: " + str(nx.nodes(G1)))
print("Edges: " + str(nx.edges(G1)))
print("Edgetype:" + str(type(G1.edges)))

print("Graph2: ")
print("Directed? " + str(nx.is_directed(G2)))
print("Number of nodes: " + str(nx.number_of_nodes(G2)))
print("Nodes: " + str(nx.nodes(G2)))
print("Edges: " + str(nx.edges(G2)))
print("Edgetype:" + str(type(G2.edges)))

x="n"
#x = input("do you want to see the plot of the both random graphs? (y=yes):\n")
if (x=="y"):
    fig_copy = plt.gcf()
    plt.show() #.show clears the image
    plt.draw()

GM = isomorphism.GraphMatcher(G1,G2)


print("\nis the mapping from G1 and G2 isomporphism? " + str(GM.is_isomorphic()))
#if (str(GM.is_isomorphic()) == "True"):
#    print("\nthe isomporphism mapping from G1 and G2:" + str(GM.mapping)
