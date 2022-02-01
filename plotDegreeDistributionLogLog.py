import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import collections

def processNetwork(file, log):
    network = nx.read_gml(file)
    networkGroupingNodes = collections.Counter()    
    for node in network.nodes:
        networkGroupingNodes[network.degree(node)] += 1
    orderedNodes = sorted(networkGroupingNodes.items(), key=lambda x:x[1], reverse=True)
    x,y = zip(*orderedNodes)
    if (log):
         x = np.log(x)
         y = np.log(y)
    title = 'Grafo {} vértices e {} arestas'.format(len(network.nodes()), len(network.edges()))
    plt.title(title)
    xlabel = "Grau dos vértices"
    ylabel = "Quantidade de vértices"
    if (log):
        xlabel += " - log(k)"
        ylabel += " - log(v)"
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if (log):
        plt.scatter(x, y)
    else:
        plt.plot(x,y)
    plt.show()


log = False

file = 'E:\\mestrado\\redesII\\1to1000\\00_864_19.gml'
processNetwork(file,log)

file = 'E:\\mestrado\\redesII\\1000to10000\\00_6047_32.gml'
processNetwork(file,log)

file = 'E:\\mestrado\\redesII\\10000to100000\\00_10315_14.gml'
processNetwork(file,log)

file = 'E:\\mestrado\\redesII\\100000to1000000\\00_559585_2.gml'
processNetwork(file,log)