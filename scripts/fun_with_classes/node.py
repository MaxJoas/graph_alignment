
""" Node object with an id (str), a label (str) and neighbours (set) """
class Node():


    def __init__ ( self, id, label="" ):

        self.id = id
        self.label = label
        self.in_neighbours = set()
        self.out_neighbours = set()
        self.neighbours = set()



    '''add a neighbour to the neighbours set of the node'''
    def add_neighbour(self, node):
        self.neighbours.add(node)

    '''remove a neighbour from the neighbours set of the node'''
    def remove_neighbour(self, node):
        self.neighbours.remove(node)

    '''allow comparing nodes to each other ( all operations )'''
    def __eq__( self, other ):
        if not isinstance(other, Node):
            return NotImplemented
        else:
            return all( (self.id == other.id, self.label == other.label, self.neighbours == other.neighbours) )


    def __ne__( self, other ):
        if not isinstance(other, Node):
            return NotImplemented
        else:
            return any( (self.id != other.id, self.label != other.label, self.neighbours != other.neighbours) )


    def __lt__( self, other ):
        if not isinstance(other, Node):
            return NotImplemented
        else:
            return self.id < other.id


    def __le__( self, other ):
        if not isinstance(other, Node):
            return NotImplemented
        else:
            return self.id <= other.id


    def __gt__( self, other ):
        if not isinstance(other, Node):
            return NotImplemented
        else:
            return self.id > other.id


    def __ge__( self, other ):
        if not isinstance(other, Node):
            return NotImplemented
        else:
            return self.id >= other.id


    def __hash__( self ):
        return hash((self.id, self.label))



    '''define the way, a node is printed'''
    def __str__( self ):

        neighbours_string = " "

        for neighbour in self.neighbours:
            neighbours_string += neighbour.id
            neighbours_string += ", "
        return  self.id + "\t'" + self.label + "'\t(" + str(neighbours_string) + ")"


    def __repr__(self):
        return self.__str__()
