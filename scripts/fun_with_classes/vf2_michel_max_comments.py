from node import Node
from graph import Graph
import sys

sys.setrecursionlimit(10000)


class VF2():


    def __init__( self, g1, g2 ):

        self.null_node = Node( "0", "" )

        if not g1.is_directed:
            g1.create_fake_directions()
        if not g2.is_directed:
            g2.create_fake_directions()


        if len(g1.nodes) == len(g2.nodes):
            self.type = "isomorphism"
        else:
            self.type = "subgraph"
        if g1 >= g2:
            self.g1 = g1
            self.g2 = g2
        else:
            self.g1 = g2
            self.g2 = g1


        self.core1 = {}
        self.core2 = {}
# clear until here ---------------------------------------------------

# fill core dictionaries with null node, because we dont have coressponding nodes yet ?
        for node in self.g1.nodes:
            self.core1[node] = self.null_node

        for node in self.g2.nodes:
            self.core2[node] = self.null_node

        self.in1 = {}
        self.out1 = {}
        self.in2 = {}
        self.out2 = {}
# why here 0 and above null node as initialization
        for node in self.g1.nodes:
            self.in1[node] = 0
            self.out1[node] = 0

        for node in self.g2.nodes:
            self.in2[node] = 0
            self.out2[node] = 0



# why last mapped no attribute since it is always the same? smae with init_t_lengths, but it is just a stylistc critic
    def match(
                self,
                last_mapped = ( Node("0",""),Node("0","") ),
                init_t_lengths={"in1":0, "out1":0, "in2":0, "out2":0},
                depth=0
            ):

        #print("last_mapped: {} \n t_lengths: {} \n depth: {} \n".format(last_mapped, init_t_lengths, depth))
        if self.s_in_g2():
            return self.core2 # why core2 ------------------------------------------------------------

        t_lengths = self.set_inout( last_mapped, depth, init_t_lengths )
        #print("Afterwards tl {} {} {}".format(t_lengths, self.core1, self.core2) )
        p = self.compute_p( t_lengths )
        #print("p "+str(p))
        #print("After p {}".format(t_lengths))

        for tuple in p :
            #print("t_lengths {}".format(t_lengths))
            if self.is_feasible( tuple ):
                self.compute_s_( tuple, depth )
                print("Call! " + str(tuple) + str(t_lengths) + str(depth))
                self.match( tuple, t_lengths, depth+1 )

        self.restore_ds( last_mapped, t_lengths, depth )


# clear------------------------

    def s_in_g2( self ):

        for node in self.core2:
            if self.core2[node] == self.null_node:
                return False
        return True

        '''
        for node in self.g2.nodes:
            if not node in s:
                return False

        return True
        '''



    def compute_p( self, t_lengths ):

        if t_lengths["out1"] and t_lengths["out2"]: # does this work is 0 = null = false --------------------------------------
            p = self.cartesian_product( self.out1, self.legal_max(self.out2) )
            return p

        elif not any( (t_lengths["out1"], t_lengths["out2"] ) ) and  all( (t_lengths["in1"], t_lengths["in2"]) ):
            p = self.cartesian_product( self.in1,  self.legal_max(self.in2) )
            return p


            # why no cartesian here---------------------
        elif not any( (t_lengths["in1"], t_lengths["in2"], t_lengths["out1"], t_lengths["out2"]) ):
            g1_starter_set = self.g1.nodes - set( n for n in self.core1.keys() if self.core1[n] != self.null_node )
            g2_starter_set = self.g2.nodes - set( m for m in self.core2.keys() if self.core2[m] != self.null_node )

            p = set()

            for node in g1_starter_set:
                p.add( (node, max(g2_starter_set)) )
            return p

        elif not any( (t_lengths[in1], t_lengths[in2], t_lengths[out1]) ) and t_lengths[out2]:
            print( "This situation should have been caught." )
            return

        else : #state is not part of matching

            p = set()
            return p




    def is_feasible(self, tuple):

        n = tuple[0]
        m = tuple[1]

        for node1 in n.neighbours:

            if not self.core1[node1] == self.null_node:
                print("Hi")
                for node2 in m.neighbours:
                    if not self.core1[node1] == self.core2[node2]:
                        print("neighbours not ok")
                        return False

            elif not self.is_diff_okay():
                print("diff not okay")
                return False

            if self.semantic_attributes():
                return True
            else:
                return False




    '''#TODO: try sth different wht did you try to \'correspond the tuples ?  \''''
    def compute_s_( self, tuple, depth ):

        self.core1[tuple[0]] = tuple[1]
        self.core2[tuple[1]] = tuple[0]




    def restore_ds( self, last_mapped, t_lengths, depth ):

        n = last_mapped[0]
        m = last_mapped[1]

        self.core1[n] = self.null_node
        self.core2[m] = self.null_node

        self.restore_terminals(self.in1, t_lengths, "in1", depth)
        self.restore_terminals(self.out1, t_lengths, "out1", depth)
        self.restore_terminals(self.in2, t_lengths, "in2", depth)
        self.restore_terminals(self.out2, t_lengths, "out2", depth)







# HELPER FUNCTIONS -------------------------------------------------------------


#
    def set_inout( self, last_mapped, depth, t_lengths ):

        n = last_mapped[0]
        m = last_mapped[1]

        for edge in self.g1.edges:

            if n == edge.node1:
                self.out1[edge.node2] = depth
                t_lengths["out1"] += 1

            elif n == edge.node2:
                self.in1[edge.node1] = depth
                t_lengths["in1"] += 1

        for edge in self.g2.edges:

            if m == edge.node1:
                self.out2[edge.node2] = depth
                t_lengths["out2"] += 1

            elif m == edge.node2:
                self.in2[edge.node1] = depth
                t_lengths["in2"] += 1

        print(self.in1, self.out1)
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




    '''TODO: This is all pretty damn ugly'''
    def is_diff_okay( self ):

        free_n1 = len(self.g1.nodes) - len([n for n in self.core1 if self.core1[n].id != "0"]) - len(self.in1) - len(self.out1)

        free_n2 = len(self.g2.nodes) - len([n for n in self.core2 if self.core2[n].id != "0"]) - len(self.in2) - len(self.out2)

        if self.type == "isomorphism":
            return free_n1 == free_n2

        elif self.type == "subgraph":
            return free_n1 >= free_n2




    def semantic_attributes( self ):
        return True




    def restore_terminals( self, t_dict, t_lengths, dict_key, depth):

        for node in t_dict.keys():
            if t_dict[node] == depth:
                t_dict[node] = 0
                #if t_lengths[str(t_dict)] > 0:
                t_lengths[dict_key] -= 1




if __name__ == "__main__":
    from parser import parse_graph
    import sys

    g1 = parse_graph(sys.argv[1])
    g2 = parse_graph(sys.argv[2])

    s = {}

    vf2 = VF2(g1, g2)
    print( vf2.match() )
