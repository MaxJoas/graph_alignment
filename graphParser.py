#!/bin/python3

module parseGraph
import sys
import pprint

def parseGraph(doc):
    checkList = [] #contains #nodes #edges and if graph is directed
    nodes = {}
    edges = {}

    with open(doc) as d:

        indicator = 0 #counts the empty lines to indicate which info is being processed
        for line in d:
            line = line.replace("\n", "")
            splitList = line.split(" ")
            if not line:
                indicator += 1
                continue
            elif indicator == 0:
                try:
                    checkList.append(int(splitList[0]))
                except:
                    checkList.append(splitList[0] == "True")
            elif indicator == 1:
                nodes[splitList[0]] = splitList[1:]
            elif indicator == 2:
                edges[(splitList[0], splitList[1])] = splitList[2:]
            else:
                print("Beep")
                continue

    pprint.pprint(checkList)
    pprint.pprint(nodes)
    pprint.pprint(edges)
    return (checkList, nodes, edges)

parseGraph(sys.argv[1])
