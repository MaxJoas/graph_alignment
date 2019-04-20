#!/bin/python3

import sys
from graphParser import parseGraph 


def bk(p, r, x, graph):
    if not p and not x:
        print(r)
        return r
    else:
        #p is a dictionary of nodes {(id, label):[n1, n2,...]}
        for v in p[:]:
            r_new = r[::]
            r_new.append(v)
            p_new = intersection(p, graph[v]) #(v for v in p if v in graph[v])
            #print(p_new)
            x_new = intersection(x, graph[v])
            #print(x_new)
            bk(p_new, r_new, x_new, graph)
            x.append(v)
            #print(list(set(x) and set(graph[v])))
            p.remove(v)

def intersection(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result


#EXECUTION ROAD#

graph = parseGraph(sys.argv[1])[1]
p = list(graph.keys())
g = []
bk(p, g, g, graph)
