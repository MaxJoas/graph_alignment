

class Edge(object):
    """simple Edge class that stores id, label and direction of an edge"""

    def __init__(self, node1, node2, direction="O", label=""):

        self.node1 = node1
        self.node2 = node2
        self.direction = direction
        self.label = label


    def __str__(self):

        return "({}, {}) '{}' direction: {}".format( self.node1, self.node2,
                self.label, self.direction )

    def __repr__(self):
        return self.__str__()
