from node import Node
from graph import Graph


class VF2():

    def __init__(self, g1, g2):

        self.null_node = Node("0", "")

        '''if the graph is undirected, the inverse edges (1,2 -> 2,1) are
        constructed to work with the original VF2 algorithm'''
        if not g1.is_directed:
            g1.create_fake_directions()
        if not g2.is_directed:
            g2.create_fake_directions()

        '''makes sure, that g2 is the smaller graph'''
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

        '''Initialize the core sets which contain the partial mapping'''
        self.core1 = {}
        self.core2 = {}

        for node in self.g1.nodes:
            self.core1[node] = self.null_node

        for node in self.g2.nodes:
            self.core2[node] = self.null_node

        '''initialize the inout sets'''
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

    '''
    TODO: print command should be in main
    '''
    '''main matching function, is called recursively and returns legal matches'''

    def match(
        self,
        last_mapped=(Node("0", ""), Node("0", "")),
        depth=0
    ):

        if self.s_in_g2():

            print("\nEND_RESULT: \nType: {} \n\n{}\n".format(self.type, self.core2))
            self.restore_ds(last_mapped, depth)

            return self.core2

        t_lengths = self.set_inout(last_mapped, depth)
        p = self.compute_p(t_lengths)

        for tuple in p:

            if self.is_feasible(tuple, depth, t_lengths):

                self.compute_s_(tuple, depth)
                self.match(tuple, depth+1)

                # print("\n Call! \n\n last_mapped: {} \n\n t_lengths: {} \n\n
                # depth: {} \n\n core1: {} \n\n core2 {} \n\n".format(
                # tuple, t_lengths, depth, self.core1, self.core2 ) )

        self.restore_ds(last_mapped, depth)

    def s_in_g2(self):

        for node in self.core2:
            if self.core2[node] == self.null_node:
                return False
        return True

    def compute_p(self, t_lengths):

        if t_lengths["out1"] and t_lengths["out2"]:

            p = self.cartesian_product(self.out1, self.legal_max(self.out2))

            return p

        elif not t_lengths["out1"] and not t_lengths["out2"] and t_lengths["in1"] and t_lengths["in2"]:

            p = self.cartesian_product(self.in1,  self.legal_max(self.in2))

            return p

        elif not any((t_lengths["in1"], t_lengths["in2"], t_lengths["out1"], t_lengths["out2"])):

            # checks current mapping of g1 equals M1(s)
            g1_starter_set = self.g1.nodes - \
                set(n for n in self.core1.keys() if self.core1[n] != self.null_node)
            g2_starter_set = self.g2.nodes - \
                set(m for m in self.core2.keys() if self.core2[m] != self.null_node)  # see above

            p = set()

            # analogous to cartesian product with different max function because of different data structure
            for node in g1_starter_set:
                p.add((node, max(g2_starter_set)))

            return p

        else:  # state is not part of matching

            p = set()
            return p

    def is_feasible(self, tuple, depth, t_lengths):

        #print("Tested tuple: {}".format(tuple))

        n = tuple[0]
        m = tuple[1]

        if self.type == "isomorphism":

            '''0-look-ahead'''
            if not all((
                self.zero_look_ahead(n, m, self.in1, self.core1, self.in2, self.core2),
                self.zero_look_ahead(m, n, self.in2, self.core2, self.in1, self.core1),
                self.zero_look_ahead(n, m, self.out1, self.core1, self.out2, self.core2),
                self.zero_look_ahead(m, n, self.out2, self.core2, self.out1, self.core1)
            )):

                #print("0-look-ahead error")
                return False

            '''1-look-ahead'''
            if not t_lengths["in1"] == t_lengths["in2"] or not t_lengths["out1"] == t_lengths["out2"]:
                #print("1-look-ahead error")
                return False

        elif self.type == "subgraph":

            '''0-look-ahead'''
            if not all(
                    (  # self.zero_look_ahead( n, m, self.in1, self.core1, self.in2, self.core2),
                        self.zero_look_ahead(m, n, self.in2, self.core2, self.in1, self.core1),
                        # self.zero_look_ahead(n, m, self.out1, self.core1, self.out2, self.core2),
                        self.zero_look_ahead(m, n, self.out2, self.core2, self.out1, self.core1)
                    )):

                #print("0-look-ahead error")
                return False

            '''1-look-ahead'''
            if not t_lengths["in1"] >= t_lengths["in2"] or not t_lengths["out1"] >= t_lengths["out2"]:
                # print("1-look-ahead-error")
                return False

        else:
            raise ValueError("!!!WARNING: Matching type has not been set!!!")
            exit()

        '''2-look-ahead'''
        if not self.two_look_ahead(depth, t_lengths):
            # print("2-look-ahead-error")
            return False

        '''compares label-specific information, if needed for the specific
        application. As is, always returns True.'''
        if self.semantic_attributes():

            # print(depth)
            #print("IS OKAY CONTINUE")
            # print(self.core2)

            return True

        else:

            return False

    def compute_s_(self, tuple, depth):

        n = tuple[0]
        m = tuple[1]

        self.core1[tuple[0]] = tuple[1]
        self.core2[tuple[1]] = tuple[0]

    def restore_ds(self, last_mapped, depth):

        n = last_mapped[0]
        m = last_mapped[1]

        self.restore_terminals(self.in1, "in1", self.core1, depth)
        self.restore_terminals(self.out1, "out1", self.core1, depth)
        self.restore_terminals(self.in2, "in2", self.core2, depth)
        self.restore_terminals(self.out2, "out2", self.core2, depth)

        self.core1[n] = self.null_node
        self.core2[m] = self.null_node

        #print("Depth: {} \n Restored tuple: {}".format(depth, last_mapped))


# HELPER FUNCTIONS -------------------------------------------------------------

    '''
    Saves number of nodes for each terminal set in t_lengths and sets ssr /
    recursion depth, if not set. Used for computing candidate set p.
    '''

    def set_inout(self, last_mapped, depth):

        t_lengths = {"in1": 0, "out1": 0, "in2": 0, "out2": 0}

        n = last_mapped[0]
        m = last_mapped[1]

        '''makes sure, the first selescted node gets depth'''
        try:  # This is needed, because the very first try will fail
            if self.in1[n] == 0 and self.out1[n] == 0:
                self.in1[n] = depth
                self.out1[n] = depth

            if self.in2[m] == 0 and self.out2[m] == 0:
                self.in2[m] = depth
                self.out2[m] = depth

        except:
            pass

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

        # print("\n in2: {} \n\n out2: {} \n\n {} \n
        # \n".format(self.in2, self.out2, t_lengths))
        return t_lengths

    '''creates the cartesian product of every g1 node with max(id) node in g2'''

    def cartesian_product(self, t_dict, t_max):

        cp = set()

        for node in t_dict:

            if t_dict[node] > 0:
                if self.core1[node] == self.null_node:  # is node in terminal set

                    cp.add((node, t_max))

        return cp

    '''returns node from t_dict with max id'''

    def legal_max(self, t_dict):

        max_node = self.null_node

        for node in t_dict:
            if t_dict[node] > 0:
                if self.core2[node] == self.null_node:  # checks if cur node is mapped
                    if node > max_node:
                        max_node = node

        return max_node

    '''every neighbour of n ( tested tuple: (n,m) ) has to be mapped to a
    neighbour of m'''

    def zero_look_ahead(self, node1, node2, t_dict_a, core_a, t_dict_b, core_b):

        for n_ in node1.neighbours:

            if t_dict_a[n_] != 0 and core_a[n_] != self.null_node:

                m_ = core_a[n_]  # m_ is the node mapped on n_

                if not m_ in node2.neighbours or t_dict_b[m_] == 0:
                    return False

        return True

    def two_look_ahead(self, depth, t_lengths):

        free_n1 = len(self.g1.nodes) - depth - t_lengths["in1"] - t_lengths["out1"]
        free_n2 = len(self.g2.nodes) - depth - t_lengths["in2"] - t_lengths["out2"]

        if self.type == "isomorphism":
            return free_n1 == free_n2

        elif self.type == "subgraph":
            return free_n1 >= free_n2

    def semantic_attributes(self):
        return True

    def restore_terminals(self, t_dict, dict_key, core, depth):

        for node in t_dict:
            if core[node] == self.null_node and t_dict[node] == depth:
                t_dict[node] = 0

    '''
    TODO: to_String?
    '''


if __name__ == "__main__":

    from parser import parse_graph
    import sys

    g1 = parse_graph(sys.argv[1])
    g2 = parse_graph(sys.argv[2])

    vf2 = VF2(g1, g2)
    vf2.match()
