import os
import networkx as nx
#import matplotlib.pyplot as plt
import collections
import copy

def readNetwork(network):
    removedFile = 'E:\\mestrado\\python\\colapso\\networks\\removed\\removed' 
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
      nx.write_gml(GRemoved,'{0}_{1}.gml'.format(removedFile,n))    

file = 'E:\\mestrado\\python\\colapso\\networks\\metodoIOriginal.gml' 
readNetwork(file)
files = os.listdir('E:\\mestrado\\python\\colapso\\networks\\removed\\removed\\')
for f in files:
    if f.endswith('.gml'):
        G = nx.read_gml(f)
        subs[i].plot(xRemovedAux,yRemovedAux,label=qtdNetworks)    
        subs[i].legend(loc='best')            
        fig.savefig('/home/juca/Documentos/10000to100000/networks10000to100000.png'.format(str(qtdNetworks)))

