###python -m pip install -U pip
#sudo apt install python3-pip
#pip3 install networkx
#sudo apt-get install python3-matplotlib
#python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
#sudo apt-get install python3.6-tk

#sudo apt-get install python3-scipy

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

'''first number is the number of nodes; second is the edge probability, ergo a float between 0 and 1'''
n = input("number of nodes? (integer):\n")
p = input("the edge probability? (a float between 0 and 1):\n")
d = input("directed? (True or False):\n").upper == "TRUE" #turns cas insensitive string-input to true bool

G = nx.fast_gnp_random_graph(int(n), float(p), seed=None, directed=d) 

'''
this changes the layout of the node display. Planar layout doesn't work with every graph. KK layout is pretty nice
(better than spring_layout) most of the time.
'''
if int(n) < 20:
    pos = nx.planar_layout(G) #no edge intersections
else:
    pos = nx.kamada_kawai_layout(G) #nice layout

nx.draw(G, pos, with_labels = 1) 

'''
The functions below return some properties about the graph
More functions like this can be found here:
https://networkx.github.io/documentation/networkx-1.10/reference/functions.html
'''
#print("Directed? " + str(nx.is_directed(G)))
#print("Number of nodes: " + str(nx.number_of_nodes(G)))
#print("Nodes: " + str(nx.nodes(G)))
#print("Edges: " + str(nx.edges(G)))
#print("Edgetype:" + str(type(G.edges)))

x = input("do you want to see the plot? (y=yes):\n")
if (x=="y"):
    fig_copy = plt.gcf()
    plt.show() #.show clears the image
    plt.draw()

z = input("do you want to save the plot? (y=yes):\n")

if z=="y":
    fig_copy.savefig("RandomGraph.png")
    print("\nthe random generated graph is saved as RandomGraph.png")

    f = open('RandomGraph.graph', 'w')
    f.write("AUTHOR: Clemens M., Max. J, Michel K., NetworkX\n")
    f.write("#nodes;" + str(nx.number_of_nodes(G)))
    f.write("\n#edges;"+ str(nx.number_of_edges(G)))
    f.write("\nNodes labelled;"+ "False")
    f.write("\nEdges labelled;"+ "False")
    f.write("\nDirected graph;"+ str(nx.is_directed(G)))
    f.write("\n\n")
    for i in (nx.nodes(G)):
        f.write(str(i))
        f.write(";\n")
    f.write("\n")

    _list= (str(G.edges)).replace("[", "")
    _list = _list.replace("]", "")
    _list = _list.replace("(", "")
    _list = _list.replace(")", "")
    _list = _list.replace(" ", "")
    split_list = _list.split(",")

    #print("split_list:" + str(split_list))
    a=0
    for i in (split_list):
        f.write(i)
        if (a % 2 == 0):
            f.write(";")
        else :
            f.write("\n")
        a=a+1
    f.close()

    print("\nthe random generated graph is saved as RandomGraph.graph")
