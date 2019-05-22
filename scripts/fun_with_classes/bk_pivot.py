from parser import parse_graph
from graph import Graph
import sys
import pprint
import random
from node import Node

''' implementing broknkerbosch algorithmn where r is the list of possible nodes
in a clique, p is the list of canditates and x is the garbage collection'''

def find_max_pivot(p, x):

    helper = dict()
    p_union_x = p + list(x)
    helper = [0,0]

    for v in p_union_x[:]:

        cur_len_intersection = len([n for n in v.neighbours if n in p])
        helper[v] = cur_len_intersection

    key_max = max(helper.keys(), key=(lambda k: helper[k]))
    return  key_max

def test(p,x):
    p_union_x = p + list(x)
    helper = 0
    piv = Node('0', '')
    for v in p_union_x:
        cur_len_intersection = len([n for n in v.neighbours if n in p])
        if cur_len_intersection > helper:
            piv = v
            helper = cur_len_intersection

    return piv


def bk_pivot ( r, p, x ):

    # when p and x are empty return r as max clique and end
    if not any ( [p, x] ):

        print('clique: ', r)
        return r

    pivot = test( p, x )

    # chosing pivot randomly from union of p, x:
    #pivot = random.choice( p + list(x) )

    # loop through canditates p without neighbours of pivot element
    for v in p[:] :

        if  v in pivot.neighbours: # bk with pivot only takes
            continue

        r_ = r | {v} # concatenate r and v

        # intersection of x respectively p and neighbours of v
        x_ = x & v.neighbours
        p_ = [n for n in v.neighbours if n in p ]

        bk_pivot ( r_, p_, x_ ) # recursive call of broknkerbosch

        p.remove(v) # taking current node out of canditates
        x.add(v) # adding current node to garbage collection

def bk ( r, p, x ):

    # when p and x are empty return r as max clique
    if not any ( [ p, x ] ):
        print('clique')
        pprint.pprint(r)
        return r

    for v in p[:] :

        r_ = r | {v} # concatenate r and v

        # intersection of x respectively p and neighbours of v
        x_ = x & v.neighbours
        p_ = [n for n in v.neighbours if n in p]

        bk ( r_, p_, x_ ) # recursive call of broknkerbosch

        p.remove(v) # taking current node out of canditates
        x.add(v) # adding current node to garbage collection


# EXECUTION (PIVOT VERSION) ----------------------------------------------------

if __name__ == '__main__':

    try:

        graph = parse_graph(sys.argv[1])
        r = set()
        x = set()
        p = list(graph.nodes)

        bk_pivot ( r, p, x )

    except Exception as e:
        print(e)
        print( ' please provide a graph file as argument \n example: python3 bk_pivot.py graph.graph' )
