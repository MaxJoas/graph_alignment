from vf2_beauty import VF2
from modular_product import *
from bk_pivot_class import BK
from parser import parse_graph
from graph import Graph
import sys


# TODO: Change graph_list to dict with g.id as key
def upgma( graph_list, align_algo ):

    if len( graph_list ) == 1:
        return graph_list[0]

    alignment = Graph('0')
    max = 0

    for g1 in graph_list[:]:
        for g2 in graph_list[:]:

            if g1.id == g2.id:
            #or g2.id + "." + g1.id in dist_dict

                continue

            # if align_algo == "VF2":
            #     vf2 = VF2( g1, g2 )
            #     vf2.match()
            #
            #     g1g2 = Graph( g1.id + "." + g2.id, vf2.results[0])
            #     g1g2.create_undirected_edges()
            #
            #     dist_dict[ g1g2 ] = len(g1.nodes) - len(g1g2.nodes)

            if align_algo == "BK":

                modp = mod_product( cart_product( g1.nodes, g2.nodes))

                bk = BK()

                x = set()
                r = set()
                p = list(modp.nodes)

                bk.bk_pivot( r, p, x)

                g1g2 = Graph( g1.id + "." + g2.id, bk.results[0])
                g1g2.create_undirected_edges()
                print(bk.results)

                if len(g1g2.nodes) > max:
                        alignment = g1g2
                        max = len(g1g2.nodes)



    id_list = alignment.id.split(".")
    for id in id_list:
        for graph in graph_list:

            if graph.id == id:
                print("{} removed from list!".format(graph.id))
                graph_list.remove(graph)

    graph_list.append( alignment )
    upgma(graph_list, align_algo)


if __name__ == '__main__':

    g_list = []

    for arg in sys.argv[1:]:
        g = parse_graph(arg)
        g_list.append( g )

    #print(g_list)
    upgma( g_list, "BK" )
