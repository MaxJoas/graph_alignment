from parser import parse_graph
import sys
import edge
import node

class Graph():

    """ idea: get nodes from a parser and get edges from nodes """

    def __init__( self,  doc ):

<<<<<<< HEAD
        parsed = parse_graph(sys.argv[1])

        raw_bools = parsed[0]
        raw_nodes = parsed[1]
        raw_edges = parsed[2]

=======
        parsed = parse_graph(doc)

        raw_bools = parsed[0]
        raw_nodes = parsed[1]
        raw_edges = parsed[2]
        
>>>>>>> 2e29255f17aa3706769ba96d53b4497b8dc31536
        self.nodes_are_labelled = raw_bools[2]
        self.edges_are_labelled = raw_bools[3]
        self.is_directed = raw_bools[4]

        self.nodes = self.get_nodes(parsed[1])
        #self.edges = get_edges(parsed[2])


<<<<<<< HEAD
    def get_nodes( self, raw_nodes_list ):

        nodes = []

        for raw_node in raw_nodes_list:
            nodes.append(node.Node( raw_node[0], raw_node[1] )) #0 is the id, 1 is the label


        self.deduce_neighbours( raw_nodes_list, nodes )

        return nodes

    ''' doesn't work yet '''
    def deduce_neighbours( self, raw_nodes_data, nodes_list_without_neighbours ):

=======
    def get_nodes( self, raw_nodes_dict ):
        
        nodes = []
        
        for key in raw_nodes_dict.keys():
            cur_node = Node( raw_node[0], raw_node[1] )) #0 is the id, 1 is the label
            nodes.append(cur_node)

        self.add_neighbours( raw_nodes_dict, nodes )
        
        return nodes

    ''' doesn't work yet '''
    def add_neighbours( self, raw_nodes_data, nodes_list_without_neighbours ):
                
        tupelHelperList = nodes_list_without_neighbours
        tupelHelperDict = {}

        for node in raw_nodes_data:
            for neighbour in raw_nodes_data[node]:
                





        
>>>>>>> 2e29255f17aa3706769ba96d53b4497b8dc31536
        for node in nodes_list_without_neighbours:
            neighbours = []
            print(raw_nodes_data)

            # how do I make real nodes out of the raw nodes?

            raw_neighbours = raw_nodes_data[raw_nodes_data.index(node.id)][2:]

            for raw_neighbour in raw_neighbours:
                neighbours.append( nodes_list_without_neighbours[nodes_list_without_neighbours.index(raw_neighbour)] )



    def get_edges ( self ):

        edges = []

        for node in nodes:
            for neighbour in neighbours:
                cur_edge = Edge( node, neighbour, "direction", "label" )
                reverse_edge = Edge( neighbour, node, "direction", "label" )

                if not reverse_edge in edges: # prevents duplicates
                    edges.append(cur_edge)


#EXECUTION ROAD#

G = Graph(sys.argv[1])
print(G)
