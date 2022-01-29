import networkx as nx
import os
import time

startGlobal = time.perf_counter()
files = os.listdir('E:\\mestrado\\defesa')
filesSorted = sorted(files)
idx = 0
for file in filesSorted:
    if file.endswith('gml'):
        idx += 1
        tmstInicio = '{0}'.format(time.strftime("%d/%m/%Y, %H:%M:%S"))
        fileAux = 'E:\\mestrado\\defesa\\{0}'.format(file)
        startNetwork = time.perf_counter()
        G           = nx.read_gml(fileAux)
        GRemoved    = nx.read_gml(fileAux)        
        lowestDegree = 10000000000000
        for node in G.nodes():
          if G.degree(node) < lowestDegree:
            lowestDegree = G.degree(node)
        
        if lowestDegree <= 100:
            degreeToRemove = lowestDegree * 3
        elif lowestDegree <= 1000:
            degreeToRemove = lowestDegree * 2
        else:
            degreeToRemove = lowestDegree * 1.5
                
        for node in G.nodes():
          if G.degree(node) >= degreeToRemove:
              GRemoved.remove_node(node)        
        
        nx.write_gml(GRemoved,'E:\\mestrado\\defesa\\removed_{0}'.format(file))
        stopNetwork = time.perf_counter()
        tmstTermino = '{0}'.format(time.strftime("%d/%m/%Y, %H:%M:%S"))
        totalTime = stopNetwork - startNetwork
        print('{0} & {1} & {2} & {3} & {4} & {5} & {6} & {7} & {8} & {9}\\\\ \\hline'.format(idx,file,tmstInicio,tmstTermino,totalTime,degreeToRemove, len(G.nodes()),len(GRemoved.nodes()),len(nx.edges(G)),len(nx.edges(GRemoved))))
        

stopGlobal = time.perf_counter()
totalGlobalTime = stopGlobal - startGlobal
print(totalGlobalTime)