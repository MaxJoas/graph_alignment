import sys

from parser import parse_graph
from node import Node
from graph import Graph


class VfTwo():

    def __init__(self, g, h):

        self.null_n = Node('0', '')


        # make sure that smaller graph has always the same name
        self.small_g, self.large_g = h, g

        if g.int_size() < h.int_size():
            self.small_g = g
            self.large_g = h

        # determine if to look for subgraph isomorphism or graph isomorphism
        self.type = 'subgraph'
        if h.int_size() == g.int_size():
            self.type = 'isomorphism'

        # make sure that edges are labelled
        if not self.small_g.is_directed:
            self.small_g.create_fake_directions()
        if not self.large_g.is_directed:
            self.large_g.create_fake_directions()

        # Initialiazing the two core dictionaries that store each node of the
        # Corresponding graph as key and the node of the other graph where it maps
        # As soon as it mapps for now we use self.null_n as inital value
        self.core_s_g = self.small_g.gen_dict( self.null_n )
        self.core_l_g = self.large_g.gen_dict( self.null_n )

        # initialiazing the terminal sets for each graph. These are dictionaries
        # that store the node as values and the recursion depth as keys where the
        # nodes entered the corresponding set. For now we initialiazing them with 0 '''
        self.t_in_s = self.t_out_s = self.small_g.gen_dict(0)
        self.t_in_l = self.t_out_l = self.large_g.gen_dict(0)

        self.t_len = {"in_l": 0, "out_l": 0, "in_s": 0, "out_s": 0}


    def match( self, depth=0, last_mapped=(Node("0", ""), Node("0", "")), ):
        """ vf2 according to cordella paper """
        if self.matching_covers_g2():

            print("\nEND_RESULT: \nType: {} \n\n{}\n".format( self.core_s_g ))
            self.restore_ds( last_mapped, last_mapped[1], depth )
            return self.core_s_g

        self.compute_len_terminal_sets(last_mapped[0], last_mapped[1], depth)
        p = self.compute_p()

        for tup in p:

            if self.feasable(tup[0], tup[1], depth):
                self.compute_state( tup )
                self.match( depth + 1, tup)
        self.restore_ds( last_mapped[0], last_mapped[1], depth )

    def matching_covers_g2(self):
        """
        checks if every node of the small graph is mapped to a node in the
        large graph and return True or False accordingly
        """
        for vert in self.core_s_g:
            if self.core_s_g[vert] == self.null_n:
                return False
        return True

    def compute_p(self):
        ''' computes the canditates p by the rules defined in the paper'''
        val = [self.t_len[x] for x in self.t_len]  # list of vals in dict

        if all( [ self.t_len['out_l'], self.t_len['out_s'] ] ):

            min = self.my_max(self.t_out_s)
            t_help = {n for n in self.t_out_l if self.t_out_l[n] != self.null_n}
            return self.cart_prod(t_help, min)

        #  checks if both t_outs are empty and both t_ins are note empty
        elif not any( [ val[1], val[3]]) and all([val[0], val[2] ]) :

            help = {n for n in self.t_in_l if self.t_in_l[n] != self.null_n}
            return self.cart_prod(help, my_max(self.t_in_s))

        elif all( [ val == 0 for val in self.t_len.values() ] ):

            m_l = {n for n in self.core_l_g if self.core_l_g[n] != self.null_n}
            m_s = {n for n in self.core_s_g if self.core_s_g[n] != self.null_n}
            # In diff_l are all nodes that are in the large graph, but not mapping
            diff_l = self.large_g.nodes - m_l
            diff_s = self.small_g.nodes - m_s  # see above
            return self.cart_prod(diff_l, max(diff_s))
        return set()

    def cart_prod(self, nodes, my_max):
        cart_p = set()
        for v in nodes:
            cart_p.add((v, my_max))
        return cart_p

    def my_max(self, t_dict):
        max_node = self.null_n
        for v in t_dict:
            if t_dict[v] > 0 and self.core_s_g[v] != self.null_n:
                continue
            elif v > max_node:
                max_node = v
        return max_node


    def compute_len_terminal_sets( self, n, m, depth ):
        self.t_len = { "in_l":0, "out_l":0, "in_s":0, "out_s":0 }

        # Compute terminal_dicts and length for the large graph
        for v in n.neighbours:

            if not self.core_l_g[v] == self.null_n :
                continue

            elif v in n.in_neighbours:
                # saves current depth for terminal node in case it hasn't depth yet
                if self.t_in_l[v] == 0: self.t_in_l[v] = depth
                self.t_len[ 'in_l' ] += 1

            elif v in n.out_neighbours :
                self.t_len[ 'out_l' ] += 1
                if self.t_out_l[v] == 0: self.t_out_l[v] = depth


        # compute terminal_dicts for the small graph
        for v in m.neighbours:

            if self.core_s_g[v] == self.null_n:
                continue

            elif v in m.in_neighbours:
                if self.t_in_s[v] == 0: self.t_in_s[v] = depth
                self.t_len[ 'in_s' ] += 1

            elif v in m.out_neighbours:
                self.t_len[ 'out_s' ] += 1
                if self.t_out_s[v] == 0: self.t_out_s[v] = depth



    def feasable( self, n, m, depth ):

        lens = [self.t_len[x] for x in self.t_len]  # list of vals in dict
        bool_l = self.zero_look_ahead( n, m, self.core_l_g )
        bool_s = self.zero_look_ahead( m, n, self.core_s_g )

        if not all( [ bool_l, bool_s ] ):
            return False

        elif self.type == 'isomorphism' :
            if not ( lens[0] == lens[2] or lens[1] == lens[3] ):
                return False

        elif self.type == 'subgraph':
            if not ( lens[0] >= lens[2] or lens[1] >= lens[3] ):
                return False

        elif not self.two_look_ahead( depth, lens ):
            return False
        return self.check_semantics()

    def zero_look_ahead( self, n, m, core ):

        for n_ in n.neighbours:
            m_ = core[n_] # Mapping of v
            if m_ == self.null_n : # If mapping does'n exist take next neighbour
                continue

            # If n_ is an in neighbour of n m_ must be an in neighbour of m
            elif n_ in n.in_neighbours
                print('n:')
                print(n)
                print(n.in_neighbours)
                if not m_ in m.in_neighbours:
                    return False

            # Since we only contemplating neighbours of n n_ has to be an in or
            # An out neighbour, it is sufficient to only check it m_ is out
            # Neighbour of m
            elif not  m_ in m.out_neighbours:
                return False
        return True

    def two_look_ahead( self ,depth, lens ):
        free_large_g = self.large_g.int_size() -  depth - lens[0] -lens[1]
        free_small_g = self.small_g.int_size() - depht - lens[2] - lens[3]

        if self.type == 'subgraph' and free_large_g >= free_small_g:
            return True
        elif self.type == 'isomorphism' and free_large_g == free_small_g:
            return True
        return False

    def check_semantics( self ):
        return True

    def compute_state ( self, tupel ):

        '''
        computes current state of mapping by adding the last feasable nodes to
        the cores
        '''
        self.core_l_g[ tupel[0] ] = tupel[1]
        self.core_s_g[ tupel[1] ] = tupel[0]

    def restore_ds( self, n, m, depth ):

        self.restore_terminals(self.t_in_l, "in_l", self.core_l_g, depth)
        self.restore_terminals(self.t_out_l, "out_l", self.core_l_g, depth)
        self.restore_terminals(self.t_in_s, "in_s", self.core_s_g, depth)
        self.restore_terminals(self.t_out_s, "out_s", self.core_s_g, depth)

        self.core_l_g[n] = self.null_n
        self.core_s_g[m] = self.null_n

    def restore_terminals(self, t_dict, dict_key, core, depth):

        for node in t_dict:
            if core[node] == self.null_n and t_dict[node] == depth:
                t_dict[node] = 0


if __name__ == "__main__":

    g = parse_graph( sys.argv[1] )
    h = parse_graph( sys.argv[2] )
    vf2 = VfTwo( g, h )
    vf2.match()
