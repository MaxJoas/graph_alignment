
class Edge():
    '''Edge object with a label (str)  and a node1 (Node) connecting to node2 (Node) '''

    def __init__(
                    self,
                    node1,
                    node2,
                    label=None
                ):

        self.node1 = node1
        self.node2 = node2
        self.label = label if label else ""


    def is_reverse_of( self, e2 ):
        '''checks if edge is the reverse (as in a,b to b,a) of another edge'''
        if self.node1 == e2.node2 and self.node2 == e2.node1:
            return True
        else:
            return False


    '''allow comparing edges to each other (==, !=)'''
    def __eq__( self, other ):
        if not isinstance(other, Edge):
            return NotImplemented
        else:
            return all( (self.node1 == other.node1, self.node2 == other.node2, self.label == other.label) )


    def __ne__( self, other ):
        if not isinstance(other, Edge):
            return NotImplemented
        else:
            return any( (self.node1 != other.node1, self.node2 != other.node2, self.label != other.label) )


    def __hash__( self ):
        return hash((self.node1, self.node2, self.label))



    '''define the way an edge is printed'''
    def __str__( self ):
        if self.node1.mult_id == "":
            node1_id = self.node1.id
        else:
            node1_id = self.node1.mult_id
        if self.node2.mult_id == "":
            node2_id = self.node2.id
        else:
            node2_id = self.node2.mult_id
        return " ( {},   {} )   '{}'".format( node1_id, node2_id, self.label )


    def __repr__(self):
        return self.__str__()
