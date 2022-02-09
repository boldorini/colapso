import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import collections

def processNetwork(file, log):
    network = nx.read_edgelist(file)
    networkGroupingNodes = collections.Counter()    
    for node in network.nodes:
        networkGroupingNodes[network.degree(node)] += 1
    if log:
        orderedNodes = sorted(networkGroupingNodes.items(), key=lambda x:x[1], reverse=True)
    else:
        orderedNodes = sorted(networkGroupingNodes.items())
    x,y = zip(*orderedNodes)
    if (log):
         x = np.log(x)
         y = np.log(y)
    title = 'Distribuição de graus - {} vértices e {} arestas'.format(len(network.nodes()), len(network.edges()))
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




# file = 'E:\\mestrado\\redesII\\1to1000\\00_864_19.gml'
# processNetwork(file,log)
# log = True
# file = 'E:\\mestrado\\redesII\\1000to10000\\00_6047_192480.gml'
# processNetwork(file,log)

# log = False
# file = 'E:\\mestrado\\redesII\\1000to10000\\00_6029_181592_removed_metodoII.gml'
# processNetwork(file,log)

# log = True
# file = 'E:\\mestrado\\redes\\100000to1000000\\redesOriginais\\919233_21.gml'
# processNetwork(file,log)

log = True
file = 'G:\\Meu Drive\\Mestrado\\defesa\\método II\\CE-CX.txt'
processNetwork(file,log)

log = False
file = 'G:\\Meu Drive\\Mestrado\\defesa\\método II\\00_2555_303_removed_metodoIII.txt'
processNetwork(file,log)

# log = False
# file = 'E:\\mestrado\\redes\\100000to1000000\\experimentoIII\\919233_21.gml'
# processNetwork(file,log)

# file = 'E:\\mestrado\\redesII\\1to1000\\00_removed_302_506_metodoI.gml'
# processNetwork(file, log)

# log = True
# file = 'E:\\mestrado\\redesII\\1to1000\\00_864_19.gml'
#processNetwork(file, log)

# file = 'E:\\mestrado\\redesII\\1000to10000\\00_5330_83060_removed_metodoIII.gml'
# processNetwork(file,log)

# file = 'E:\\mestrado\\redesII\\10000to100000\\00_10315_14.gml'
# processNetwork(file,log)

# file = 'E:\\mestrado\\redesII\\100000to1000000\\00_559585_2.gml'
# processNetwork(file,log)