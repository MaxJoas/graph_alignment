#!/bin/python3

import sys
import pprint
from node import Node
from edge import Edge
from graph import Graph



def parse_graph(doc):

    check_list = [] #contains #nodes #edges, if they are labelled and if graph is directed
    nodes = set()
    edges = set()

    with open(doc) as d:

        indicator = 0 #counts the empty lines (0: check_list, 1: nodes, 2: edges)

        for line in d:
            line = line.replace("\n", "")
            split_list = line.split(";")
            
            #if line is empty
            if not line:
                indicator += 1
                continue



            #building check_list
            elif indicator == 0:
                
                arg = split_list[-1]  #last element in row is interpreted

                if line.upper().startswith( "AUTHOR" ):
                    print( "Reading {} from {}".format( sys.argv[1].split("/")[-1], line.split(" ")[1:]) )
                    continue

                elif arg.upper() in ( "TRUE", "FALSE" ):
                    check_list.append( arg.upper()  == "TRUE" )
                
                else:
                    try:
                        check_list.append( int(arg) ) #indicates number of nodes/edges
            
                    except:
                        print( "Something's wrong with the first paragraph. Please check and try again." )
                        print( "Aborting..." )
                        return


            #building nodes
            elif indicator == 1:

                cur_node = Node( *split_list )
                nodes.add( cur_node )


            #building labeled and/or directed edges
            elif indicator == 2: 
                
                #is there a better way to do this?
                
                for node in nodes:
                    if node.id == split_list[0]:
                        split_list[0] = node
                    
                    elif node.id == split_list[1]:
                        split_list[1] = node
                    
                cur_edge = Edge( *split_list )
                edges.add( cur_edge )

            else:
                print( "Wrong input file format. File contains too many empty lines." )
                print( "Aborting..." )
                return
    
    

    #Some illegalities are tested
    issues = ""
    
    if check_list[0] != len(nodes):
        issues += "Indicated number of nodes ({}) doesn't fit actual number of nodes ({}). \n".format(check_list[0], len(nodes))

    if check_list[1] != len(edges):
        issues += "Indicated number of edges ({}) doesn't fit actual number of edges ({}). \n".format(check_list[1], len(edges))
    
    if not check_list[2]:
        for node in nodes:
            if node.label != "":
                issues += "One or more nodes are labelled. If this is intended, please indicate this at the beginning of the graph file \n"
                break

    if not check_list[3]:
        for edge in edges:
            if edge.label != "":
                issues += "One or more edges are labelled. If this is intended, please indicate this at the beginning of the graph file \n"
                break
    
    if not check_list[4]:  #if graph is undirected
        if edges_contain_doubles( edges ):  #(a,b) and (b,a)
            issues += "Undirected graph can contain any edge only once. \n" 
            

    
    #evaluates if any issues have been detected. If not, parsing continues.
    if issues == "":
        nodes = get_node_neighbours(nodes, edges)
        
        print( "Successfully parsed " + sys.argv[1].split("/")[-1] )
        g = Graph( check_list[2], check_list[3], check_list[4], nodes, edges)
        return g

    else:
        print( "There are some issues with the input file: \n" )
        print( issues )
        print( "Aborting..." )
        return



#This function works, because is_reverse_of only checks {(n1,n2) and (n2,n1}, not {(n1,n2) and (n1,n2)} (second case is sorted out because edges is a set)
def edges_contain_doubles( edges ):
    for edge1 in edges:
        for edge2 in edges:
            if edge1.is_reverse_of(edge2):
                return True
    return False



def get_node_neighbours(nodes, edges):
    
    nodes_w_neighbours = set()
    
    for cur_node in nodes:

        for cur_edge in edges:

            if cur_node.id == cur_edge.node1.id:
                cur_node.neighbours.add( cur_edge.node2 )
            
            if cur_node.id == cur_edge.node2.id:
                cur_node.neighbours.add( cur_edge.node1 )
    
        nodes_w_neighbours.add(cur_node)

    return nodes_w_neighbours



if __name__ == "__main__":
    
    G = parse_graph(sys.argv[1])
    
    pprint.pprint( G )
