#from parser import parse_graph
import sys
from pysmiles import read_smiles
import networkx as nx
#import numpy as np

smiles = "c1cccc(OC(=O)C)c1C(=O)O"
mol = read_smiles(smiles, explicit_hydrogen=False, zero_order_bonds=True, reinterpret_aromatic=True)
#mol2 = read_smiles(smiles, explicit_hydrogen=True, zero_order_bonds=True, reinterpret_aromatic=True)

# explicit_hydrogen determines whether hydrogen atoms should be represented as explicit nodes in the created molecule, or implicit in the 'hcount' attribute.
#  zero_order_bonds determines whether zero-order bonds (.) in the SMILES string should result in edges in the produced molecule.
#    reinterpret_aromatic determines whether aromaticity should be reinterpreted, and determined from the constructed molecule, or whether the aromaticity specifications from the SMILES string (lower case elements) should be taken as leading. If True, will also set bond orders to 1 for bonds that are not part of an aromatic ring and have a bond order of 1.5. If False, will create a molecule using only the information in the SMILES string.

#print(mol.nodes(data='element'))
#print(mol.nodes(data='aromatic'))
#print(mol.nodes(data='order'))


#print(is_directedmol.edges)
# print(nx.adjacency_matrix(mol2, weight='order').todense())
# mol[4]
# mol2[20]
# len(mol2)
# [[0.  1.5 0.  0.  0.  0.  0.  0.  0.  1.5 0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0. ]
#  [1.5 0.  1.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0. ]
#  [0.  1.5 0.  1.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0. ]
#  [0.  0.  1.5 0.  1.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0. ]
#  [0.  0.  0.  1.5 0.  1.  0.  0.  0.  1.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  1.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  0.  1.  0.  2.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  0.  0.  2.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  1.  1.  0. ]
#  [1.5 0.  0.  0.  1.5 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  2.  1.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  2.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1. ]
#  [1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
#  [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  0. ]]
#0;C
#C 1=sp3 1.5=c 2=sp2.
#Essentially, the hybridisation of the carbon atom is based on the number of
#bonds to other carbons or identical atoms. sp3 = single bond. sp2 = double
#bond. sp = triple bond.

# Csp3: C mit nur Einfachbindungen
# Csp2: C mit einer Doppelbindung (und zwei Einfachbindungen)
# Csp: C mit einer Dreifachbindung (und einer Einfachbindung) oder zwei Doppelbindungen
# c: aromatisches C
# Osp3: O mit zwei Einfachbindungen
# Osp2: O mit einer Doppelbindung


def s_writer(mol):

    z = "y" #input("do you want to save the plot? (y=yes):\n")

    if z == "y":
        f = open('smile.graph', 'w')
        f.write("AUTHOR: Clemens M., Max. J, Michel K., NetworkX, pysmiles, ")
        f.write(str(smiles))
        f.write("\n#nodes;" + str(len(mol.nodes)))
        f.write("\n#edges;" + str(len(mol.edges)))
        f.write("\nNodes labelled;" + str("True"))
        f.write("\nEdges labelled;" + str("False"))
        f.write("\nDirected graph;" + str("False"))
        f.write("\n\n")
        c = 0
        for i in (mol.nodes(data='element')):
            _list = (str(i))
            _list = _list.replace("'", "")
            _list = _list.replace("(", "")
            _list = _list.replace(")", "")
            _list = _list.replace(",", ";")
            _list = _list.replace(" ", "")
            if mol.nodes(data='aromatic')[c]:
                _list = _list.replace("C", "c")
            f.write(_list)
            _list = str(nx.adjacency_matrix(mol, weight='order').todense()[c])
            _list = _list.replace("[", "")
            _list = _list.replace(" ", "")
            _list = _list.replace("]", "")
            _list = list(_list.split("."))
            sp2 = False
            sp3 = False
            for j in _list:
                if j == "2":
                    sp2 = True
                # else:
                #     if j == "50" and lh != "1":
                #         sp3 = True
                # Csp3: C mit nur Einfachbindungen
                # Csp2: C mit einer Doppelbindung (und zwei Einfachbindungen)
                # Csp: C mit einer Dreifachbindung (und einer Einfachbindung) oder zwei Doppelbindungen
                # c: aromatisches C
                # Osp3: O mit zwei Einfachbindungen
                # Osp2: O mit einer Doppelbindung
            if sp2:
                f.write("sp2")
            # if sp3:
            #     f.write("sp3")
            f.write("\n")
            c = c + 1
        f.write("\n")
        
        for i in (mol.edges):
            _list = (str(i))
            _list = _list.replace("'", "")
            _list = _list.replace("(", "")
            _list = _list.replace(")", "")
            _list = _list.replace(",", ";")
            _list = _list.replace(" ", "")
            f.write(_list)
            #f.write(";")
            #f.write(split_list[3])
            f.write("\n")
            #print(_list)
        f.write("\n")
    f.close()




# EXECUTION  -------------------------------------------------------------------

if __name__ == '__main__':
    s_writer(mol)
