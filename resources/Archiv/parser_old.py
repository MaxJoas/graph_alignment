#!/bin/python3

import sys
import pprint
from node import Node
from edge import Edge


def parse_graph(doc):

    check_list = [] #contains #nodes #edges, if they are labelled and if graph is directed
    nodes = {}
    edges = []

    with open(doc) as d:

        indicator = 0 #counts the empty lines (0: check_list, 1: nodes, 2: edges)
        made_neighbours_real = False    #checks if neighbours were converted to Node objects

        for line in d:
            line = line.replace("\n", "")
            split_list = line.split(";")

            #if line is empty
            if not line:
                indicator += 1
                continue



            #building check_list
            elif indicator == 0:

                try:
                    check_list.append(int(split_list[1])) #indicates number of nodes/edges
                except:
                    check_list.append(split_list[-1] == "True")



            #building nodes
            elif indicator == 1:

                if check_list[2]:    #if nodes are labelled
                    cur_node = Node(split_list[0], split_list[1])
                    nodes[cur_node] = split_list[2:]

                else:   #if nodes are not labelled
                    cur_node = Node(split_list[0], "") 
                    nodes[cur_node] = split_list[1:]
            


            #building labeled and/or directed edges
            elif indicator == 2: 
                
                if not made_neighbours_real:
                    nodes = make_neighbours_real(nodes)
                    made_neighbours_real = True
                
                #if edges are labelled but not directed a spare element must be inserted. 
                if check_list[3] and not check_list[4]:
                    cur_edge = Edge(split_list[0], split_list[1], "O", split_list[2]) #0:node1, 1:node1, 2:label
                    edges.append(cur_edge)
                else:    
                    cur_edge = Edge(*split_list)   
                    edges.append(cur_edge) 


            else:
                print("Oh no, something went wrong here! File contains too many empty lines.")
                return
    

    if not made_neighbours_real:
        nodes = make_neighbours_real(nodes)
        made_neighbours_real = True
    

    #if edges are neither labeled nor directed, they are built from the nodes
    if check_list[3] == False and check_list[4] == False:
            
            edges = create_undirected_edges(nodes)

    
    
    print("Successfully parsed " + sys.argv[1].split("/")[-1])
    return (check_list, nodes, edges)





#converts nodes neighbours (str) to list of Node objects
def make_neighbours_real(nodes_with_stringlist):
    
    node_id_dict = {}
    final_list = []
    
    for node in nodes_with_stringlist: #creates a dict {node.id : Node}
        node_id_dict[node.id] = node


    for node, neighbour_stringlist in nodes_with_stringlist.items():
        final_list.append(node)
        
        for neighbour_id in neighbour_stringlist:
            
            for node_id in node_id_dict.keys():
                
                if neighbour_id == node_id:
                    node.add_neighbour(node_id_dict[node_id]) #converts str(neighbour.id) to Node object of neighbour
            
    return final_list


#creates the edges from the nodes if edges are neither labelled nor directed
def create_undirected_edges(nodes):

    done = [] #already checked nodes, used to avoid including reverse edges
    edges = []

    for node in nodes:

        for neighbour in node.neighbours:

            if not neighbour in done:
                cur_edge = Edge(node, neighbour)
                edges.append(cur_edge)
        
        done.append(node)
    
    return edges


if __name__ == "__main__":
    
    test = parse_graph(sys.argv[1])
    
    pprint.pprint(test[0])
    pprint.pprint(test[1])
    pprint.pprint(test[2])
