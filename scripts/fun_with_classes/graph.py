import sys
from edge import Edge
import node

class Graph():


    def __init__(
                    self,
                    nodes = set(),
                    edges =set(),
                    nodes_labelled=False,
                    edges_labelled=False,
                    is_directed=False
                ):

        self.nodes = nodes
        self.edges = edges
        self.nodes_are_labelled = nodes_labelled
        self.edges_are_labelled = edges_labelled
        self.is_directed = is_directed


    def create_undirected_edges( self ):

        done = [] #already checked nodes, used to avoid including reverse edges

        for node in self.nodes:

            for neighbour in node.neighbours:

                if not neighbour in done: #done is for undirected #no bjektion
                    cur_edge = Edge(node, neighbour)
                    self.edges.add(cur_edge)

            done.append(node)



    def create_fake_directions( self ):
        if self.is_directed:
            print( "Fake directions should only be created for undirected graphs!" )
            return False
        else:
            for edge in list(self.edges)[:]:
                rev_edge = Edge( edge.node2, edge.node1, edge.label )
                self.edges.add(rev_edge)



    '''allow comparing graphs (number of nodes!) to each other ( >=, <=, <, > )'''
    def __gt__( self, other ):
        if not isinstance(other, Graph):
            return NotImplemented
        else:
            return len(self.nodes) > len(other.nodes)


    def __lt__( self, other ):
        if not isinstance(other, Graph):
            return NotImplemented
        else:
            return len(self.nodes) < len(other.nodes)


    def __ge__( self, other ):
        if not isinstance(other, Graph):
            return NotImplemented
        else:
            return len(self.nodes) >= len(other.nodes)


    def __le__( self, other ):
        if not isinstance(other, Graph):
            return NotImplemented
        else:
            return len(self.nodes) <= len(other.nodes)




    '''define the way a graph is printed'''
    def __str__( self ):
        return "{} ;\n {};\n Nodes labelled? {}\n Edges labelled? {}\n Directed graph? {}".format(self.nodes, self.edges, self.nodes_are_labelled, self.edges_are_labelled, self.is_directed)


    def __repr__( self ):
        return self.__str__()
