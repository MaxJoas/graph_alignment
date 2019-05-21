from node import Node
from graph import Graph
import sys

sys.setrecursionlimit(500)


class VF2():


    def __init__( self, g1, g2 ):

        self.null_node = Node( "0", "" )

        if not g1.is_directed:
            g1.create_fake_directions()
        if not g2.is_directed:
            g2.create_fake_directions()


        '''
        TODO: definition of type is not true
        maybe convert to subgraph afterwards if needed?
        '''
        if len(g1.nodes) == len(g2.nodes):
            self.type = "isomorphism"
        else:
            self.type = "subgraph"
        if g1 > g2:
            self.g1 = g1
            self.g2 = g2
        else:
            self.g1 = g2
            self.g2 = g1

        '''
        TODO: There is a more pythonic way (one line) right?
        '''
        self.core1 = {}
        self.core2 = {}

        for node in self.g1.nodes:
            self.core1[node] = self.null_node

        for node in self.g2.nodes:
            self.core2[node] = self.null_node

        self.in1 = {}
        self.out1 = {}
        self.in2 = {}
        self.out2 = {}

        for node in self.g1.nodes:
            self.in1[node] = 0
            self.out1[node] = 0

        for node in self.g2.nodes:
            self.in2[node] = 0
            self.out2[node] = 0




    def match(
                self,
                last_mapped=( Node("0",""),Node("0","") ),
                depth=0
            ):

        if self.s_in_g2():
            print("\n\nEND_RESULT: \nType: {} \n\n{}\n\n".format(self.type, self.core2))
            return self.core2

        t_lengths = self.set_inout( last_mapped, depth )
        p = self.compute_p( t_lengths )


        for tuple in p :

            if self.is_feasible( tuple, depth, t_lengths ):
                self.compute_s_( tuple )

                print("\n Call! \n\n last_mapped: {} \n\n t_lengths: {} \n\n depth: {} \n\n core1: {} \n\n core2 {} \n\n".format(tuple, t_lengths, depth, self.core1, self.core2))

                self.match( tuple, depth+1 )

                last_mapped = tuple

        self.restore_ds( last_mapped, t_lengths, depth )




    def s_in_g2( self ):

        for node in self.core2:
            if self.core2[node] == self.null_node:
                return False
        return True




    def compute_p( self, t_lengths ):

        if t_lengths["out1"] and t_lengths["out2"]:

            p = self.cartesian_product( self.out1, self.legal_max(self.out2) )

            print("OUT Candidates: {}".format(p))
            return p

        elif not t_lengths["out1"] and not t_lengths["out2"] and t_lengths["in1"] and t_lengths["in2"]:

            p = self.cartesian_product( self.in1,  self.legal_max(self.in2) )

            print("IN Candidates: {}".format(p))
            return p

        elif not any( (t_lengths["in1"], t_lengths["in2"], t_lengths["out1"], t_lengths["out2"]) ):

            g1_starter_set = self.g1.nodes - set( n for n in self.core1.keys() if self.core1[n] != self.null_node )
            g2_starter_set = self.g2.nodes - set( m for m in self.core2.keys() if self.core2[m] != self.null_node )

            p = set()

            '''
            TODO: Does cp work here now?
            '''
            for node in g1_starter_set:
                p.add( (node, max(g2_starter_set)) )
            return p

        elif not any( (t_lengths["in1"], t_lengths["in2"], t_lengths["out1"]) ) and t_lengths["out2"]:
            print( "This situation should have been caught." )
            return

        else : #state is not part of matching

            p = set()
            return p



    '''
    TODO:
    Unused ifs?
    Summarize them at least!

    condition not sufficient for subgraph...
    some edges are missing
    '''
    def is_feasible( self, tuple, depth, t_lengths ):

        n = tuple[0]
        m = tuple[1]

        print("Tested tuple: {}".format(tuple))

        '''
        if self.type == "isomorphism" and len(n.neighbours) != len(m.neighbours):
            print("Wrong neighbour number in isomorphism!")
            return False

        elif self.type == "subgraph" and len(n.neighbours) < len(m.neighbours):
            print("Wrong neighbour number in subgraph!")
            return False
        '''


        if self.type == "isomorphism":

            '''0-look-ahead'''
            if not all(
                        (self.zero_look_ahead( n, self.in1, self.core1, self.in2, self.core2),
                        self.zero_look_ahead(m, self.in2, self.core2, self.in1, self.core1),
                        self.zero_look_ahead(n, self.out1, self.core1, self.out2, self.core2),
                        self.zero_look_ahead(m, self.out2, self.core2, self.out1, self.core1))
                    ):

                print("0-look-ahead error")
                return False

            '''1-look-ahead'''
            if not t_lengths["in1"] == t_lengths["in2"] or not t_lengths["out1"] == t_lengths["out2"]:
                print("1-look-ahead error")
                return False

        elif self.type == "subgraph":

            '''0-look-ahead'''
            if not all(
                        (self.zero_look_ahead( n, self.in1, self.core1, self.in2, self.core2),
                        self.zero_look_ahead(m, self.in2, self.core2, self.in1, self.core1),
                        self.zero_look_ahead(n, self.out1, self.core1, self.out2, self.core2),
                        self.zero_look_ahead(m, self.out2, self.core2, self.out1, self.core1)
                    )):

                print("0-look-ahead error")
                return False

            '''1-look-ahead'''
            if not t_lengths["in1"] >= t_lengths["in2"] or not t_lengths["out1"] >= t_lengths["out2"]:
                print("1-look-ahead-error")
                return False

        else:
            raise ValueError("!!!WARNING: Matching type has not been set!!!")

        '''2-look-ahead'''
        if not self.two_look_ahead( depth, t_lengths ):
            print("2-look-ahead-error")
            return False


        return True

        '''
        if self.type == "isomorphism" and len(n.neighbours) != len(m.neighbours):
            print("Wrong neighbour number in isomorphism!")
            return False

        elif self.type == "subgraph" and len(n.neighbours) < len(m.neighbours):
            print("Wrong neighbour number in subgraph!")
            return False

        for node1 in n.neighbours:

            for node2 in m.neighbours:

                if self.core1[node1] == node2:
                    if self.core2[node2] != node1:
                        print("Wrong association in core2!")

                        return False

                elif self.core2[node2] == node1:
                    if self.core1[node1] != node2:
                        print("Wrong association in core1!")

                        return False


        if not self.is_diff_okay( depth, t_lengths ):
            print("diff not okay")
            return False
        '''

        if self.semantic_attributes():
            print(depth)
            print("IS OKAY CONTINUE")
            print(self.core2)
            return True




    def compute_s_( self, tuple ):

        self.core1[tuple[0]] = tuple[1]
        self.core2[tuple[1]] = tuple[0]




    '''
    TODO:
    when backtracking, the nodes are being used
    multiple times
    '''
    def restore_ds( self, last_mapped, t_lengths, depth ):

        n = last_mapped[0]
        m = last_mapped[1]

        #if not self.null_node in (n,m):
        self.core1[n] = self.null_node
        self.core2[m] = self.null_node

        self.restore_terminals(self.in1, t_lengths, "in1", self.core1, depth)
        self.restore_terminals(self.out1, t_lengths, "out1", self.core1, depth)
        self.restore_terminals(self.in2, t_lengths, "in2", self.core2, depth)
        self.restore_terminals(self.out2, t_lengths, "out2", self.core2, depth)







# HELPER FUNCTIONS -------------------------------------------------------------



    def set_inout( self, last_mapped, depth ):

        t_lengths={"in1":0, "out1":0, "in2":0, "out2":0}

        n = last_mapped[0]
        m = last_mapped[1]

        for edge in self.g1.edges:

            if n == edge.node1 and self.core1[edge.node2] == self.null_node:
                t_lengths["out1"] += 1

                if self.out1[edge.node2] == 0:
                        self.out1[edge.node2] = depth

            elif n == edge.node2 and self.core1[edge.node1] == self.null_node:
                t_lengths["in1"] += 1

                if self.in1[edge.node1] == 0:
                    self.in1[edge.node1] = depth


        for edge in self.g2.edges:

            if m == edge.node1 and self.core2[edge.node2] == self.null_node:
                t_lengths["out2"] += 1

                if self.out2[edge.node2] == 0:
                    self.out2[edge.node2] = depth

            elif m == edge.node2 and self.core2[edge.node1] == self.null_node:
                t_lengths["in2"] += 1

                if self.in2[edge.node1] == 0:
                    self.in2[edge.node1] = depth

        print(t_lengths)
        return t_lengths




    def cartesian_product( self, t_dict, t_max ):

        cp = set()

        for node in t_dict:
            if t_dict[node] > 0:
                if self.core1[node] == self.null_node :
                    cp.add( (node, t_max) )

        return cp




    def legal_max( self, t_dict ):

        max_node = self.null_node

        for node in t_dict:
            if t_dict[node] > 0:
                if self.core2[node] == self.null_node:
                    if node > max_node:
                        max_node = node

        return max_node





    def zero_look_ahead( self, node, t_dict_a, core_a, t_dict_b, core_b ):

        #for n_ in node.neighbours:
        for n_ in t_dict_a:

            if t_dict_a[n_] != 0 and core_a[n_] != self.null_node:

                m_ = core_a[n_]

                if t_dict_b[m_] == 0 :
                    return False
                '''or core_b[m_] == self.null_node'''
        return True



    def two_look_ahead( self, depth, t_lengths ):

        free_n1 = len(self.g1.nodes) - depth - t_lengths["in1"] - t_lengths["out1"]
        free_n2 = len(self.g2.nodes) - depth - t_lengths["in2"] - t_lengths["out2"]


        if self.type == "isomorphism":
            return free_n1 == free_n2

        elif self.type == "subgraph":
            return free_n1 >= free_n2




    def semantic_attributes( self ):
        return True




    def restore_terminals( self, t_dict, t_lengths, dict_key, core, depth ):

        for node in t_dict:
            if core[node] == self.null_node and t_dict[node] == depth:
                t_dict[node] = 0
                t_lengths[dict_key] -= 1

        return t_lengths


    '''
    TODO: to_String?
    '''


if __name__ == "__main__":
    from parser import parse_graph


    g1 = parse_graph(sys.argv[1])
    g2 = parse_graph(sys.argv[2])

    vf2 = VF2(g1, g2)
    vf2.match()
