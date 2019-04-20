

class Edge(object):
    """simple Edge class that stores id, label and direction of an edge"""

    def __init__(self, node1, node2, direction, label):

        self.node1 = node1
        self.node1 = node2
        self.direction = direction
        self.label = label
