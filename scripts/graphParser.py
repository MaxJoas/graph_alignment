#!/bin/python3

import sys
import pprint

def parseGraph(doc):
    checkList = [] #contains #nodes #edges, if they are labelled and if graph is directed
    nodes = {}
    edges = {}

    with open(doc) as d:
    
        indicator = 0 #counts the empty lines to indicate which list/dict is being filled
        for line in d:
            line = line.replace("\n", "")
            splitList = line.split("\t")
            if not line:
                indicator += 1
                continue
           
            elif indicator == 0:
                try:
                    checkList.append(int(splitList[0]))
                except:
                    checkList.append(splitList[-1] == "True")
            
            elif indicator == 1:
                if checkList[2]:    #if nodes are labelled
                    nodes[(splitList[0], splitList[1])] = splitList[2:]
                else:   #if nodes are not labelled
                    nodes[(splitList[0], "")] = splitList[1:]
            
                if not checkList[3] and not checkList[4]:
                    createUndirectedEdges(nodes, edges)
                else:
                    if indicator == 2:
                        if checkList[3]:    #if edges are labelled
                            if checkList[4]:    #if graph is directed and edges labelled
                                edges[(splitList[0], splitList[1])] = splitList[2:]
                            else:   #if graph is not directed but edges labelled
                                edges[(splitList[0], splitList[1])] = ["", splitList[2]]
                        else:
                            if checkList[4]:    #if graph is directed but edges not labelled
                                edges[(splitList[0], splitList[1])] = [splitList[2], ""]
                            else:   #if graph is not directed and edges not labelled
                                edges[(splitList[0], splitList[1])] = ["", ""]
                    else:
                        print("Oh no, something went wrong here! File contains too many empty lines.")
                        return

    pprint.pprint(checkList)
    pprint.pprint(nodes)
    pprint.pprint(edges)
    print("Successfully parsed " + sys.argv[1].split("/")[-1])
    return (checkList, nodes, edges)

def createUndirectedEdges(nodes, edges):
    done = []
    for node in nodes:
        for neighbour in nodes[node]:
            if neighbour not in done:
                edges[(node, neighbour)] = ["", ""]
        done.append(node)

#EXECUTION ROAD#

parseGraph(sys.argv[1])
