import os
import networkx as nx
import copy

def readNetwork(path,file):
    
    network = path + file
    G = nx.read_gml(network)
    GRemoved = copy.deepcopy(G)
    biggestDegree = 0
    for node in G.nodes():
      if G.degree(node) > biggestDegree:
        biggestDegree = G.degree(node)
    
    degreeToRemove = biggestDegree - (biggestDegree * 0.3)
            #medidaPareto
                    
    for node in G.nodes():
      if G.degree(node) >= degreeToRemove:
          GRemoved.remove_node(node)
    nx.write_gml(GRemoved,'{}00_{}_{}_removed_metodoII.gml'.format(path,len(GRemoved.nodes()),len(GRemoved.edges())))    
    

# path = 'E:\\mestrado\\redesII\\1to1000\\'
# file = '00_864_19.gml' 
# readNetwork(path,file)

path = 'E:\\mestrado\\redesII\\1000to10000\\'
file = '00_6047_192480.gml'
readNetwork(path,file)

# path = 'E:\\mestrado\\redesII\\10000to100000\\' 
# file = '00_10315_14.gml'
# readNetwork(path,file)

# path = 'E:\\mestrado\\redesII\\100000to1000000\\' 
# file = '00_559585_2.gml' 
# readNetwork(path, file)