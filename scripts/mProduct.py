G= [A1,]

H= [(1, 2), (2, 3), (1, 4), (4, 2)]

#The vertex set of the modular product of G and H is the cartesian product V(G) ×  V(H). Any two vertices (u, v) and (u' , v' ) are adjacent in the modular product of G and H if and only if either

#    u is adjacent with u' and v is adjacent with v' , or
#    u is not adjacent with u' and v is not adjacent with v' .

#G1edges[0][0] #erstes Tupel mit erste Element   -> 1
#G1edges[0][1] #erstes Tupel mit zweiten Element -> 2

#if node in node.neighbours

def mProduct(G,H):
	mP = []
	for i in G:
		for j in H:
			if (G[i] in H[j].neighbours and  G[i] in H[j].neighbours) or (not G[i] in H[j].neighbours and  not G[i] in H[j].neighbours) :
				mP.apppend(G[i], H[j])
	return (mP)
