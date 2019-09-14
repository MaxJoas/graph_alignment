from vf2_beauty import VF2
from modular_product import *
from bk_pivot_class import BK
from parser import parse_graph
from graph import Graph
import sys

if __name__ == '__main__':

    g_list = []

    for arg in sys.argv[1:]:
        g = parse_graph(arg)
        g_list.append( g )

    g1 = g_list[1]
    g2 = g_list[0]
    modp = mod_product( cart_product( g1.nodes, g2.nodes))
    bk = BK()
    x = set()
    r = set()
    p = list(modp.nodes)

    print(p)
    t = bk.bk_pivot( r, p, x)
    print(bk.bk_pivot(r,p,x))
    print(t)
