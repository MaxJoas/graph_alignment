#!/bin/python3

import sys
import pprint
import networkx as nx
import matplotlib.pyplot as plt
from graphParser import parseGraph



'''
yet to be implemented: 
    directions
    edge labels? 
    atm the identifiers are used as labels, must change data structure to lists (multiple times?) edge identifiers? 
    graph name in pic
    graphs change their appearance upon recomputation (do we have to change that?) 
'''
def createGraph(nodes, edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edges)
    plt.show()


#EXECUTION ROAD#

parsed_graph = parseGraph(sys.argv[1])
createGraph(parsed_graph[1], parsed_graph[2])
