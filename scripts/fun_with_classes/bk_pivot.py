
from graph import Graph
import sys
import pprint
import random

''' implementing broknkerbosch algorithmn where r is the list of possible nodes
in a clique, p is the list of canditates and x is the garbage collection'''

def bk_pivot ( r, p, x ):

    # when p and x are empty return r as max clique and end 
    if not any ( [p, x] ):
        pprint.pprint(r)
        return r

    pivot = random.choice( p  + r ) # chosing pivot randomly from union of p, r
    #pprint.pprint( pivot )

    # loop through canditates p without neighbours of pivot element
    for v in p[:] :

        if  v in pivot.neighbours:
            pass

        r_ = r + [v] # concatenate r and v

        # intersection of x respectively p and neighbours of v
        x_ = [ v for v in v.neighbours if v in x ]
        p_ = [ v for v in v.neighbours if v in p ]

        bk_pivot ( r_, p_, x_ ) # recursive call of broknkerbosch

        p.remove(v) # taking current node out of canditates
        x.append(v) # adding current node to garbage collection

def bk ( r, p, x ):

    # when p and x are empty return r as max clique
    if not any ( [ p, x ] ):
        pprint.pprint(r)
        return r

    for v in p[:] :

        r_ = r + [v] # concatenate r and v

        # intersection of x respectively p and neighbours of v
        x_ = [ v for v in v.neighbours if v in x ]
        p_ = [ v for v in v.neighbours if v in p ]

        bk ( r_, p_, x_ ) # recursive call of broknkerbosch

        p.remove(v) # taking current node out of canditates
        x.append(v) # adding current node to garbage collection


# EXECUTION (PIVOT VERSION) ----------------------------------------------------

if __name__ == '__main__':

    try:

        graph = Graph(sys.argv[1])
        r = x = []
        p = graph.nodes

        bk_pivot ( r, p, x )

    except:
        print( ' please provide a graph file as argument \n example: python3 bk_pivot.py graph.graph' )
