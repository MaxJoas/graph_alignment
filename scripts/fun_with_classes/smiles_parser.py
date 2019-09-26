from parser import parse_graph
import sys
from pysmiles import read_smiles
import networkx as nx


smiles = 'C1CC[13CH2]CC1C1CCCCC1'
mol = read_smiles(smiles)


print(mol.nodes(data='element'))
# [(0, 'C'),
#  (1, 'C'),
#  (2, 'C'),
#  (3, 'C'),

print(mol.nodes(data='hcount'))
# [(0, 2),
#  (1, 2),
#  (2, 2),
#  (3, 2),


mol_with_H = read_smiles(smiles, explicit_hydrogen=True)
print(mol_with_H.nodes(data='element'))
# [(0, 'C'),
#  (1, 'C'),
#  (2, 'C'),
#  (3, 'C'),


def g_writer(mol):

    z = "y" #input("do you want to save the plot? (y=yes):\n")

    if z=="y":
        f = open('Graphwirter.graph', 'w')
        f.write("AUTHOR: Clemens M., Max. J, Michel K., NetworkX\n")
        f.write("#nodes;" + str(len(mol.nodes)))
        f.write("\n#edges;"+ str(len(mol.edges)))
        f.write("\nNodes labelled;"+ str(mol.nodes_are_labelled))
        f.write("\nEdges labelled;"+ str(mol.edges_are_labelled))
        f.write("\nDirected graph;"+ str(mol.is_directed))
        f.write("\n\n")
        if mol.nodes_are_labelled == "False":
            for i in (mol.nodes):
                split_list = i.split(" ")
                f.write(split_list[1])
                f.write(";\n")
            f.write("\n")
        else:
            for i in (mol.nodes):
                _list=(str(i))
                _list = _list.replace("'", "")
                split_list = _list.split(" ")
                f.write(split_list[2])
                f.write(";")
                f.write(split_list[3])
                f.write("\n")
            f.write("\n")

        if not mol.is_directed:
            for edge1 in mol.edges:
                reverse=False
                for edge2 in mol.edges:
                    if edge1.is_reverse_of(edge2):
                        reverse=True
                if reverse==False:
                    print(edge1)
                    _list=(str(edge1))
                    _list = _list.replace("'", "")
                    _list = _list.replace("(", "")
                    _list = _list.replace(")", "")
                    _list = _list.replace(" ", "")
                    _list = _list.replace("to", ";")
                    split_list = _list.split(" ")
                    f.write(_list)
        else:
            for edge1 in mol.edges:
                _list=(str(edge1))
                _list = _list.replace("'", "")
                _list = _list.replace("(", "")
                _list = _list.replace(")", "")
                _list = _list.replace(" ", "")
                _list = _list.replace("to", ";")
                split_list = _list.split(" ")
                f.write(_list)
    f.close()
    print("\nthe graph is saved as Graphwirter.graph")

        #print("split_list:" + str(split_list))


# EXECUTION  -------------------------------------------------------------------

if __name__ == '__main__':
    try:
        mol = parse_graph( sys.argv[1] )
        g_writer(mol)
    except Exception as e:
        print(e)
        print("please provide the graph you want to test the graphwriter with \n example: python3 graph_writer.py /home/clm/graph_alignment/graphs/graph1.graph")
#python3 graph_writer.py /home/clm/graph_alignment/graphs/graph1.graph