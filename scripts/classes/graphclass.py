

import edge
import node

class Graph():

    """ idea: get nodes from a parser and get edges from nodes """

    def __init__( self,  doc ):

        self.nodes =  parser[1] # future return value of our yet to be implemented parser method
        self.checklist = parse[0]
        self.doc = doc

    def get_edges ( self ):

        edges = []

        for node in nodes:
            for neighbour in neighbours:
                cur_edge = Edge( node, neighbour, "direction", "label" )
                reverse_edge = Edge( neighbour, node, "direction", "label" )

                if reverse_edge not in edges: # prevents duplicates
                    edges.append(cur_edge)

    def parser (  self ):
        print("I want to be implemented by MICHEL")
        return 1,2
