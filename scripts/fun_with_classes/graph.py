from parser import parse_graph
import sys
import edge
import node
import pprint

class Graph():

    """ idea: get nodes from a parser and get edges from nodes """

    def __init__( self,  doc ):

        parsed = parse_graph(doc)

        raw_bools = parsed[0]
        self.nodes = parsed[1]
        raw_edges = parsed[2]
        
        self.nodes_are_labelled = raw_bools[2]
        self.edges_are_labelled = raw_bools[3]
        self.is_directed = raw_bools[4]

        #self.edges = get_edges(parsed[2])


        
    '''
    def get_edges ( self ):

        edges = []

        for node in nodes:
            for neighbour in neighbours:
                cur_edge = Edge( node, neighbour, "direction", "label" )
                reverse_edge = Edge( neighbour, node, "direction", "label" )

                if not reverse_edge in edges: # prevents duplicates
                    edges.append(cur_edge)
    '''

    def __str__(self):
        return "[" + str(self.nodes) + "]; Nodes labelled? " + str(self.nodes_are_labelled) + ", Edges labelled? " + str(self.edges_are_labelled) + ", Directed graph? " + str(self.is_directed) 

    def __repr__(self):
        return self.__str__()

#EXECUTION ROAD#

G = Graph(sys.argv[1])
pprint.pprint(G)
