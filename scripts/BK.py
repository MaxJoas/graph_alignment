#init
#R=0 # zum clique zwischenspeichern/bauen KANTENMENGE={{1,2},{1,5}...}}
#x=0 # Knoten der R nicht erweitert
#P=knotenmenge von G #V={1,2,3,4,...}


def BK(R,P,x):
	if not any ((P, x)):				#P=0 x=0 #len(p) == 0
		print R		
		return R				#R ist clique
	else:
		for v in P[:]:				#P[:] this will cause it to iterate over a copy of p instead. Iterate a Changing Dict
			Rr=Rr[::]			#sliced das Rr
			Rr.append(v)			#Rr=R or v    #or und and geht hier nicht
			Pp=[v for v in p if v in N(v)]	#P and Neigbor(v) #intersection #NEBEN ZAHL WURDE IDENTIFIER GEMACHT SO DAS WIR KEINE NAIGBORFKT BRAUCHEN
			Xx=[v for v in x if v in N(v)]	#x and Neigbor(v) #alle 
			BR(Rr,Pp,Xx)
			P.pop(v)			#P=P \ {v}
			x.append(v)			#x=x or {v}
			

	 
def N(v):						#???????
	c = 0
	l = []
	for i in graph[v]:
		if i is 1 :
		l.append(c)
		c+=1   
	return l 

#nods=Knoten
#node ID und Label
