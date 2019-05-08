import sys
from edge import Edge
import node
import pprint

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


    def create_undirected_edges(self):

        done = [] #already checked nodes, used to avoid including reverse edges


        for node in self.nodes:

            for neighbour in node.neighbours:

                if not neighbour in done:
                    cur_edge = Edge(node, neighbour)
                    self.edges.add(cur_edge)

            done.append(node)









    #creates the edges from the nodes if edges are neither labelled nor directed







    def __str__(self):
        return "{} ;\n {};\n Nodes labelled? {}\n Edges labelled? {}\n Directed graph? {}".format(self.nodes, self.edges, self.nodes_are_labelled, self.edges_are_labelled, self.is_directed)



    def __repr__(self):
        return self.__str__()

"""
if __name__ == "__main__" :

    G = Graph(sys.argv[1])

    pprint.pprint(G)
"""
