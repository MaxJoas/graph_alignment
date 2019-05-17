

class Edge(object):
    """simple Edge class that stores id, label and direction of an edge"""

    def __init__( self, node1, node2, label="" ):

        self.node1 = node1
        self.node2 = node2
        self.label = label




    #checks if edge is reverse (as in a,b to b,a) to another edge 
    def is_reverse_of( self, e2 ):
        if self.node1 == e2.node2 and self.node2 == e2.node1:
            return True
        else:
            return False



    def __eq__( self, other ):
        return self.node1 == other.node1 and self.node2 == other.node2 and self.label == other.label
    
    
    
    def __hash__( self ):
        return hash((self.node1, self.node2, self.label))



    def __str__( self ):

        return "\n ({} to {}) '{}'".format( self.node1.id, self.node2.id, self.label )

    
    
    
    def __repr__(self):
        return self.__str__()
