
from graph imodular_productort
from nodes import Node
import sys


def cart_product(G,H):
	modular_product = []
	for vertex_g in G:
		for vertex_h in H:
			modular_product.append( (vertex_g , vertex_h ) )


	print(modular_product)
	return (modular_product)



def neighbours_in_mp ( vertex_g, vertex_h ):

		if:
			 vertex_g in vertex_h.neighbours and  vertex_g in vertex_h.neighbours
			 return True
		elif:
			not vertex_g in vertex_h.neighbours and  not vertex_g in vertex_h.neighbours
			return True





g = ['a', 'b']
h = ['d', 'c']

cart_product( g, h )
