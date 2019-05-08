#https://www.researchgate.net/publication/200034365_An_Improved_Algorithm_for_Matching_Large_Graphs
#graph matching algorithm efficiently solve the graph isomorphism and graph-subgraph isomorphism problems on Attributed Relational Graphs. This version is particularly suited to work with very large graphs.
#(i, j) is to be considered different from (j, i). The extension of the algorithm to undirected graphs is however trivial.

from parser import parse_graph
from graph import Graph
import sys
import pprint
import random

#INPUT: an intermediate state s; the initial state s 0 has M(s 0 )=∅
#OUTPUT: the mappings between the two graphs



def F(intermediate_state, n, m): #boolean fkt. Machbarkeitsfunktion F will also prune some states that, albeit corresponding to an isomorphism between G 1 (s) and G 2 (s), would not lead to a complete matching solution.







def matchs(intermediate_state, G1, G2):
	while (procedure == True):		
		if (intermediate_state covers all nodes G2.node):
				return matchs(intermediate_state) #?
			else
			#Compute the set P(s) of the pairs candidate for inclusion in matchs(intermediate_state)
				for n in G1.node: #FOREACH (n, m)∈ P(s)???
					for m in G2.node:
						if (F(intermediate_state, n, m) == True ):
							#Compute the state s ́ obtained by adding (n, m) to M(s)
							matchs(intermediate_state) #?
						#end if ?
				#end for each?
			#restore data structure?
		#end if?
	# end procedure == False ???
			



intermediate_state=0 #the_initial_state
G1=
G2=
matchs(intermediate_state, G1, G2)
