

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

    def __str__( self ):

        return "({} to {}) '{}'".format( self.node1, self.node2, self.label )

    def __repr__(self):
        return self.__str__()
