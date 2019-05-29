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


    def get_inout_neighbours( self ):

        for cur_node in self.nodes:

            for cur_edge in self.edges:

                if cur_node == cur_edge.node1:
                    cur_node.out_neighbours.add( cur_edge.node2 )

                if cur_node == cur_edge.node2:
                    cur_node.in_neighbours.add( cur_edge.node1 )





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



    '''allow comparing graphs (number of nodes!) to each other ( ==, >=, <=, <, > )'''
    def __eq__( self, other):
        if not isinstance(other, Graph):
            return NotImplemented
        else:
            return len(self.nodes) == len(other.nodes)


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

    def int_size ( self ):
        return len(self.nodes)

    def gen_dict( self,  value ):
        _dict = {}
        for key in self.nodes:
            _dict[key] = value
        return _dict



    # def generate_in_and_out_neigh( self ):
    #     ''' saves the in neighbour and out neighbourt of every node in a dict '''
    #     for edge in self.edges:
    #         self.in_neighbours[edge.node2].add( edge.node1.id )
    #         self.out_neighbours[edge.node1].add( edge.node2.id )


    # def is_in_neigh(  self,node_to_check, node_reference ):

    #     if node_to_check.id in self.in_neighbours[node_reference] :
    #         return True
    #     return False

    # def is_out_neigh( self, node_to_check, node_reference ):
    #     if node_to_check.id in self.out_neighbours[node_reference] :
    #         return True
    #     return False
