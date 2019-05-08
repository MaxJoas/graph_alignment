import sys
import edge
import node
import pprint

class Graph():

    def __init__( 
                    self,  
                    nodes_labelled=False,
                    edges_labelled=False,
                    is_directed=False,
                    nodes=set(),
                    edges=set() 
                ):

        self.nodes_are_labelled = nodes_labelled
        self.edges_are_labelled = edges_labelled
        self.is_directed = is_directed

        self.nodes = nodes
        self.edges = edges



    def __str__(self):
        return "{} ;\n {};\n Nodes labelled? {}\n Edges labelled? {}\n Directed graph? {}".format(self.nodes, self.edges, self.nodes_are_labelled, self.edges_are_labelled, self.is_directed)



    def __repr__(self):
        return self.__str__()

"""
if __name__ == "__main__" :
    
    G = Graph(sys.argv[1])
    
    pprint.pprint(G)
"""
