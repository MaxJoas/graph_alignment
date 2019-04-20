

class Node ():
    """ node class for storing label and id of node amd neighbours """

    def __init__ ( self, id, label, neighbours ):

        self.id = id
        self.label = label
        self.neighbours = neighbours
