

#The vertex set of the modular product of G and H is the cartesian product V(G) ×  V(H). Any two vertices (u, v) and (u' , v' ) are adjacent in the modular product of G and H if and only if either

#    u is adjacent with u' and v is adjacent with v' , or
#    u is not adjacent with u' and v is not adjacent with v' .

#G1edges[0][0] #erstes Tupel mit erste Element   -> 1
#G1edges[0][1] #erstes Tupel mit zweiten Element -> 2

#if node in node.neighbours

#    def __init__ ( self, id, label ):

#        self.id = id
#        self.label = label
#        self.neighbours = []

#    def add_neighbour(self, node):
#        self.neighbours.append(node)

from graph import Graph
import sys
import 

def m_Product(g,h):
	mP = []
	#def __init__ ( mP, id, label ):
	#mP.id = []
	#mP.label = []
	#mP.neighbours = []

	for vertex_g in g:
		for vertex_h in h:
			if (g.nodes in h.neighbours and  h.nodes in h.neighbours) or (not g.nodes in h.neighbours and  not g.nodes in h.neighbours) :
				mP.id.apppend ( vertex_g + vertex_h )

	return (mP)

if __name__ == '__main__':
	try: 
		g=Graph(sys.argv[1])
		h=Graph(sys.argv[2])
		m_Product(g.nodes, h.nodes)
	except:
		print( ' please provide a graph file as argument \n example: python3 mProduct.py graph1.graph, graph2.graph' )
