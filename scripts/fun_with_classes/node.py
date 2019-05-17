

class Node():
    """ node class for storing label and id of node amd neighbours """

    def __init__ ( self, id, label="" ):

        self.id = id
        self.label = label
        self.neighbours = set()



    def add_neighbour(self, node):

        self.neighbours.add(node)




    def __eq__( self, other ):
        return self.id == other.id and self.label == other.label and self.neighbours == other.neighbours



    def __hash__( self ):
        return hash((self.id, self.label))


    def __str__( self ):

        neighbours_string = " "
        
        for neighbour in self.neighbours:
            neighbours_string += neighbour.id
            neighbours_string += " "
        return "\n Node " + self.id + " '" + self.label + "' {" + str(neighbours_string) + "}"



    def __repr__(self):
        return self.__str__()
