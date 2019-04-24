#!/bin/python3

from graph import Graph
from node import Node
import sys
import pprint

#sys.setrecursionlimit(99999999)


def bk( p, r, x ):
    if not x and not p:
        pprint.pprint(r)
        return r
    else:
        print(1)
        for v in p[:]:
            r_new = r[::]
            r_new.append(v)
            p_new = intersection(p, v.neighbours)
            print("p_new " + str(p_new))
            x_new = intersection(x, v.neighbours)
            print("x_new " + str(x_new))
            bk( p_new, r_new, x_new )
            p.remove(v)
            x.append(v)

def intersection(list1, list2):
    result = []
    for element in list1:
        #print("element " + str(element))
        if element in list2:
            result.append(element)
    #print("result " + str(result))
    return result


#EXECUTION ROAD#

graph = Graph(sys.argv[1])
p = graph.nodes
g = []

bk(p, g, g)
