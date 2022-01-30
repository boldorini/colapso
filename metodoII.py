import networkx as nx

from google.colab import drive

import os

import time

drive.mount('/content/drive')

startGlobal = time.perf_counter()

files = os.listdir('/content/drive/MyDrive/Mestrado/Redes/100000to1000000/redesOriginais')

filesSorted = sorted(files)

idx = 0

for file in filesSorted:
    if file.endswith('gml'):
        idx += 1
        tmstInicio = '{0}'.format(time.strftime("%d/%m/%Y, %H:%M:%S"))
        fileAux = '/content/drive/MyDrive/Mestrado/Redes/100000to1000000/redesOriginais/{0}'.format(file)
        startNetwork = time.perf_counter()
        G           = nx.read_gml(fileAux)
        GRemoved    = nx.read_gml(fileAux)        
        
        biggestDegree = 0
        for node in G.nodes():
          if G.degree(node) > biggestDegree:
            biggestDegree = G.degree(node)
        
        degreeToRemove = biggestDegree * 0.3 #medidaPareto
                
        for node in G.nodes():
          if G.degree(node) >= degreeToRemove:
              GRemoved.remove_node(node)        
        
        nx.write_gml(GRemoved,'/content/drive/MyDrive/Mestrado/Redes/100000to1000000/experimentoIII/{0}'.format(file))
        stopNetwork = time.perf_counter()
        tmstTermino = '{0}'.format(time.strftime("%d/%m/%Y, %H:%M:%S"))
        totalTime = stopNetwork - startNetwork
        print('{0} & {1} & {2} & {3} & {4} & {5} & {6} & {7} & {8} & {9}\\\\ \\hline'.format(idx,file,tmstInicio,tmstTermino,totalTime,degreeToRemove, len(G.nodes()),len(GRemoved.nodes()),len(nx.edges(G)),len(nx.edges(GRemoved))))