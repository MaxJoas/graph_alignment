#!/bin/python3

from graph import Graph
import sys
import pprint


def bk( p, r, x ):
    if not x and not p:
        pprint.pprint(r)
        return r
    else:
        for v in p[:]:
            r_new = r[::]
            r_new.append(v)
            p_new = intersection(p, v.neighbours)
            x_new = intersection(x, v.neighbours)
            bk( p_new, r_new, x_new )
            p.remove(v)
            x.append(v)

def intersection(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result

if __name__ == "__main__":
    graph = Graph(sys.argv[1])
    p = graph.nodes
    r = []
    x = []
    bk(p, r, x)
