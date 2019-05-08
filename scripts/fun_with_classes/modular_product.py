
from graph import Graph
from node import Node
import sys
import pprint
from parser import parse_graph
from bk_pivot import bk
from view_graph import create_graph


''' building cartesian product of two graphs '''

def cart_product(G,H):

	# init empty set to store nodes
	cart_product = []
	for vertex_g in G:
		for vertex_h in H:
			cart_product.append( (vertex_g , vertex_h ) )

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
we take each node (here a Tuple of two nodes) and make a node object of the tupel
and find neighbours of new nodes accoring to rules of modular prodcut'''

def mod_product( cartp ):

	modular_set = set() # empty set for storing Node objects of modular product
	for tup in cartp :

		#consolidation fo nodes to one new node object
		cur_node = Node( tup[0].id + tup[1].id, tup[0].label + tup[1].label )

		for t in cartp :

			# prevents that the node gets compared with itself
			if not  (tup[0].id == t[0].id or tup[1].id == t[1].id):
				if neighbours_in_mp(tup, t):
					cur_node.add_neighbour(Node( t[0].id + t[1].id, t[0].label + t[1].label))

		# add complete node object at the end of first for loop
		modular_set.add(cur_node)

	# OUTPUT
	modular_product_as_graph = Graph(modular_set)

	modular_product_as_graph.create_undirected_edges()
	#print(modular_product_as_graph.nodes)

	return modular_product_as_graph

# EXECUTION  -------------------------------------------------------------------

if __name__ == '__main__':

	try:
		g = parse_graph( sys.argv[1] )
		h = parse_graph( sys.argv[2] )
		modp = mod_product( cart_product( g.nodes, h.nodes ) )
		#print(modp)
		x = []
		r = []
		p = list(modp.nodes)
		print(p[3])



		bk( r, p, x)
		#create_graph(modp.nodes ,modp.edges)

	except Exception as e:
		print(e)
		print( "please provide the two graphs you want to build the modular product with \n example: python3 modular_product.py graph1.graph garph2.graph" )
