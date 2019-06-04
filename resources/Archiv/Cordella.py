#https://www.researchgate.net/publication/200034365_An_Improved_Algorithm_for_Matching_Large_Graphs
#graph matching algorithm efficiently solve the graph isomorphism and graph-subgraph isomorphism problems on Attributed Relational Graphs. This version is particularly suited to work with very large graphs.
#(i, j) is to be considered different from (j, i). The extension of the algorithm to undirected graphs is however trivial.

from parser import parse_graph
from graph import Graph
import sys
import pprint
import random

#INPUT: an intermediate state intermediate_state; the initial state intermediate_state 0 has M(intermediate_state 0 )=∅
#OUTPUT: the mappings between the two graphs
def P(G1, G2, intermediate_state?): 
#Compute the set P(intermediate_state) of the pairs candidate for inclusion in matchs(intermediate_state)


def F(intermediate_state, n, m, G1=n?, G2=m?): #Durchführbarkeit testen? True/False
#boolean fkt. Machbarkeitsfunktion F will also prune some states that, 
#albeit corresponding to an isomorphism between G 1 (intermediate_state) and G 2 (intermediate_state), would not lead to a complete matching solution.
#wenngleich
  if (corresponding to an isomorphism between G 1 (intermediate_state) and G 2 (intermediate_state) == True):
    return (True)



def matchs(intermediate_state, G1, G2):#M maps each branch of G 1 onto a branch of G 2 and umgekehrt
	while (procedure == True):		
		if (intermediate_state covers all nodes G2.node):
				return matchs(intermediate_state) #intermediate_state covers all nodes G2.node ??MATCH??
		else:
			#P(G1, G2, intermediate_state?) #Compute the set P(intermediate_state) of the pairs candidate for inclusion in matchs(intermediate_state)
				for n in G1.node: #FOREACH (n, m)∈ P (G1, G2, intermediate_state?): 
					for m in G2.node:
						if (F(intermediate_state, n, m) == True ):
							#Compute the state intermediate_state ́ obtained by adding (n, m) to M(intermediate_state)
							matchs(intermediate_state) #?
		end if (end for each? == True?)
      restore data structure?
		end if (end procedure == False)
			



intermediate_state=0 #the_initial_state
G1=			#G 1 = (N 1 , B 1 ) and G 2 = (N 2 , B 2 )
G2=
matchs(intermediate_state, G1, G2)
