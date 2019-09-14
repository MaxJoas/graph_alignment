from node import Node
from graph import Graph
import sys

class V():


    def __init__( self, g, h ):

        sefl.null_node = Node( '0', '' )
        self.g = g
        self.h = h

        # make sure that smaller graph has always the same name
        self.small_g, self.large_g = h, g

        if g.size < h.size:
            self.small_g = g
            self.large_g = h

        # determine if to look for subgraph isomorphism or graph isomorphism
        self.type = 'subgraph'
        if h.size == g.size :
            self.type = 'isomorphism'

        # make sure that edges are labelled
        if not small_g.is_directed:
            small_g.create_fake_directions()
        if not g2.is_directed:
            small_g.create_fake_directions()

        ''' initialiazing the two core dictionaries that store each node of the
        corresponding graph as key and the node of the other graph where it maps
        as soon as it mapps for now we use self.null_node as inital value'''
        core_small_g = dict.fromkeys( small_g.nodes, self.null_node )
        core_large_g = dict.fromkeys( large_g.nodes, self.null_node )

        ''' initialiazing the terminal sets for each graph. These are dictionaries
        that store the node as values and the recursion depth as keys where the
        nodes entered the corresponding set. For now we initialiazing them with 0 '''

        t_in_small = t_out_small = dict.fromkeys( small_g.nodes, 0 )
        t_in_large = t_out_large = dict.fromkeys( large_g.nodes, 0  )


if __name__ == "__main__":
    from parser import parse_graph


    g1 = parse_graph(sys.argv[1])
    g2 = parse_graph(sys.argv[2])
    vf = V(g1,g2)
    print(vf.typeS)
