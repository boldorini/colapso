import networkx as nx

from google.colab import drive

import os

import time

def readNetwork(path,file):
    
    G = nx.read_gml(p)
    
    for node in G.nodes():
      if G.degree(node) > biggestDegree:
        biggestDegree = G.degree(node)
    
    degreeToRemove = biggestDegree * 0.005
            #medidaPareto
                    
    for node in G.nodes():
      if G.degree(node) >= degreeToRemove:
          GRemoved.remove_node(node)        
        
    nx.write_gml(GRemoved,'/content/drive/MyDrive/Mestrado/Redes/100000to1000000/experimentoIII/{0}'.format(file))
    stopNetwork = time.perf_counter()
    tmstTermino = '{0}'.format(time.strftime("%d/%m/%Y, %H:%M:%S"))
    totalTime = stopNetwork - startNetwork
    print('{0} & {1} & {2} & {3} & {4} & {5} & {6} & {7} & {8} & {9}\\\\ \\hline'.format(idx,file,tmstInicio,tmstTermino,totalTime,degreeToRemove, len(G.nodes()),len(GRemoved.nodes()),len(nx.edges(G)),len(nx.edges(GRemoved))))