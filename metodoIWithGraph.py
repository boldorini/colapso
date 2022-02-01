import os
import networkx as nx
#import matplotlib.pyplot as plt
import collections
import copy

def readNetwork(network):
    path = 'E:\\mestrado\\redesII\\1to1000\\metodoIRemoved\\' 
    G = nx.read_gml(network)
    c = collections.Counter()
    for node in G.nodes:
      c[G.degree(node)] += 1
    GRemoved = nx.read_gml(network)
    networkDensity = nx.density(G)
    nodesOfG = len(nx.nodes(G))
    possibleLinks = (nodesOfG * (nodesOfG - 1)) / 2    
    for n in G.nodes():
      GDensity = copy.deepcopy(G)
      GDensity.remove_node(str(n))
      density = len(nx.edges(GDensity))/possibleLinks
      densityWithout = density/networkDensity
      if (1 - round(densityWithout,4)) >= 0.014:    
          GRemoved.remove_node(str(n))
      nx.write_gml(GRemoved,'{}vertice_{}_removido_{}_{}.gml'.format(path,n,len(GRemoved.nodes()),len(GRemoved.edges())))    

file = 'E:\\mestrado\\redesII\\1to1000\\00_864_19.gml' 
readNetwork(file)

