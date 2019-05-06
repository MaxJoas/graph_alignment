
from graph import Graph
from node import Node
import sys
import pprint


''' building cartesian product of two graphs '''

def cart_product(G,H):

	# init empty dictionary to store nodes and later neighbours (in mod_product)
	cart_product = dict()
	for vertex_g in G:
		for vertex_h in H:
			cart_product[(vertex_g , vertex_h )] = []

	return cart_product


''' this function checks if the two given new nodes ( of the cartesian product)
of two graphs are neighbours according to the rules of the modular product which'''

def neighbours_in_mp ( tup1, tup2 ):


	if  tup2[0] in tup1[0].neighbours and  tup2[1] in tup1[1].neighbours:
		return True

	elif not ( tup2[0] in tup1[0].neighbours or  tup2[1] in tup1[1].neighbours ):
		return True

	return False


''' this function build the modular product out of the cartesian product therfore
we take each node ( here still a tupel of the two old nodes) and compare it which
each node (tupel) except itself and check then neighobouring rules. In case we
found a neughbour we add it to the list of values in the dict to the according
node'''

def mod_product( cartp ):

	for tup in cartp.keys():
		for tup2 in cartp.keys():

			# prevents that the node gets comparedwith itself
			if not  (tup[0].id == tup2[0].id or tup[1].id == tup2[1].id):
				if neighbours_in_mp(tup, tup2):

					cartp[tup].append(tup2)
	pprint.pprint(cartp)
	return cartp

# EXECUTION  ----------------------------------------------------

if __name__ == '__main__':

	try:
		g = Graph( sys.argv[1] )
		h = Graph( sys.argv[2] )
		modp = mod_product( cart_product( g.nodes, h.nodes ) )

	except :
		print( "please provide the two graphs you want to build the modular product with \n example: python3 modular_product.py graph1.graph garph2.graph" )
