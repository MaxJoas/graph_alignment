
from graph import Graph
from node import Node
import sys
import pprint

def cart_product(G,H):
	cart_product = dict()
	for vertex_g in G:
		for vertex_h in H:
			cart_product[(vertex_g , vertex_h )] = []



	return (cart_product)



def neighbours_in_mp ( tup1, tup2 ):


	if  tup2[0] in tup1[0].neighbours and  tup2[1] in tup1[1].neighbours:
		return True
	elif not (tup2[0] in tup1[0].neighbours or  tup2[1] in tup1[1].neighbours):
		return True
	return False



def mod_product( cartp ):
	for tup in cartp.keys():
		for tup2 in cartp.keys():
			if not  (tup[0].id == tup2[0].id or tup[1].id == tup2[1].id):
				if neighbours_in_mp(tup, tup2):

					cartp[tup].append(tup2)
	pprint.pprint(cartp)
	return cartp

# EXECUTION (PIVOT VERSION) ----------------------------------------------------

if __name__ == '__main__':

	g = Graph(sys.argv[1])
	h = Graph(sys.argv[2])

	cartp = cart_product( g.nodes, h.nodes )
	modp = mod_product( cartp )
