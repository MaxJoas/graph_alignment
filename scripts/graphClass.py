class Graph ():

    # simple Graph class that has nodes and edges

    def __init__(graph_file): # the class get a list of .graph files as input

    ''' idea: give the Graph class a file and let the class parse it
        the function parse_graph returns nodes, edges and a checkList
        use the nodes and edges to assigne values to the variables of the Graph
        class '''

        self.graph_file = graph_file
        self.parsed_file = parse_graph(graph_file)
        self.nodes = self.parsed_file[1]
        self.edges = self.parsed_file[2]
