

class Node():
    """ node class for storing label and id of node amd neighbours """

    def __init__ ( self, id, label="" ):

        self.id = id
        self.label = label
        self.neighbours = set()

    def add_neighbour(self, node):
        self.neighbours.add(node)

    def __str__( self ):
        neighbours_string = " "
        for neighbour in self.neighbours:
            neighbours_string += neighbour.id
            neighbours_string += " "
        return "\n Node " + self.id + " '" + self.label + "' {" + str(neighbours_string) + "}"

    def __repr__(self):
        return self.__str__()
