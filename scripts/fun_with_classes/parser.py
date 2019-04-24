#!/bin/python3

import sys
import pprint
from node import Node

def parse_graph(doc):
    check_list = [] #contains #nodes #edges, if they are labelled and if graph is directed
    nodes = {}
    edges = {}

    with open(doc) as d:
    
        indicator = 0 #counts the empty lines to indicate which list/dict is being filled
        made_nodes_real = False
        for line in d:
            line = line.replace("\n", "")
            split_list = line.split(";")
   
            if not line:
                indicator += 1
                continue

            elif indicator == 0:
                try:
                    check_list.append(int(split_list[1]))
                except:
                    check_list.append(split_list[-1] == "True")
            
            elif indicator == 1:
                if check_list[2]:    #if nodes are labelled
                    cur_node = Node(split_list[0], split_list[1])   
                    nodes[cur_node] = split_list[2:]
                else:   #if nodes are not labelled
                    cur_node = Node(split_list[0], "") 
                    nodes[cur_node] = split_list[1:]
            
                            
            elif check_list[3] == "False" and check_list[4] == "False":
                #nodes = make_nodes_tupels(nodes)
                createUndirectedEdges(nodes, edges)
                break

            elif indicator == 2:
                break
            
            else:
                print("Oh no, something went wrong here! File contains too many empty lines.")
                return
            '''
                if not made_nodes_real:
                        #nodes = make_nodes_tupels(nodes)
                        made_nodes_real = True
                    if check_list[3]:    #if edges are labelled
                        if check_list[4]:    #if graph is directed and edges labelled
                            edges[(split_list[0], split_list[1])] = split_list[2:]
                        else:   #if graph is not directed but edges labelled
                            edges[(split_list[0], split_list[1])] = ["", split_list[2]]
                    else:
                        if check_list[4]:    #if graph is directed but edges not labelled
                            edges[(split_list[0], split_list[1])] = [split_list[2], ""]
                        else:   #if graph is not directed and edges not labelled
                            edges[(split_list[0], split_list[1])] = ["", ""]
            '''
            


    make_neighbours_real(nodes)
    #irgendwas mit edges

    pprint.pprint(check_list)
    pprint.pprint(nodes)
    #pprint.pprint(edges)
    print("Successfully parsed " + sys.argv[1].split("/")[-1])
    return (check_list, nodes, edges)


def make_neighbours_real(nodes_with_stringlist):
    
    node_id_dict = {}
    final_dict = {}

    for node in nodes_with_stringlist:
        node_id_dict[node.id] = node

    for node in nodes_with_stringlist:
        for neighbour_id in nodes_with_stringlist[node]:
            for  node_id in node_id_dict.keys():
                if neighbour_id == node_id:
                    node.add_neighbour(node_id_dict[node_id])







def createUndirectedEdges(nodes, edges):
    done = []
    for node in nodes:

        for neighbour in nodes[node]:
            if not neighbour in done:
                edges[(node, neighbour)] = ["", ""]
        done.append(node)


#get neighbours in nodes labels
def make_nodes_tupels(nodes): 
    tupelHelperList = list(nodes.keys()) #list of (id, label) for building dictionary
    tupelHelperDict = {}        

    for node in tupelHelperList:    
        tupelHelperDict[node[0]] = node[1] #dictionary which contains (id, label)
    #changes the neighbours to labelled neighbours for every node in nodes
    for node in nodes:
        #d = nodes[node]
        for neighbour in nodes[node]:
            temp = (neighbour, tupelHelperDict[neighbour])
            location = nodes[node].index(neighbour)
            nodes[node][location] = temp
    #pprint.pprint(nodes)
    
    return nodes


#EXECUTION ROAD#

parse_graph(sys.argv[1])
