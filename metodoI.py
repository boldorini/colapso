import os
import networkx as nx
import matplotlib.pyplot as plt
import collections
import copy

def readNetwork(network):
  G = nx.read_gml(network)
  c = collections.Counter()
  for node in G.nodes:
    c[G.degree(node)] += 1
  GRemoved = nx.read_gml(network)
  networkDensity = nx.density(G)
  nodesOfG = len(nx.nodes(G))
  possibleLinks = (nodesOfG * (nodesOfG - 1)) / 2
  qtdeNodesRemoved = 0;
  for n in G.nodes():
    GDensity = copy.deepcopy(G)
    GDensity.remove_node(str(n))
    density = len(nx.edges(GDensity))/possibleLinks
    densityWithout = density/networkDensity
    if (1 - round(densityWithout,4)) >= 0.014:
        qtdeNodesRemoved += 1
        GRemoved.remove_node(str(n))        
    cRemoved = collections.Counter()
    if len(GRemoved.nodes()) > 0:
        for nodeRemoved in GRemoved.nodes():
            cRemoved[GRemoved.degree(nodeRemoved)] += 1
    listsRemoved = sorted(cRemoved.items())
    xRemoved, yRemoved = zip(*listsRemoved)
    return xRemoved, yRemoved
  else:
      return 0,0

#files = os.listdir('/media/juca/Dados/mestrado/redes/1to1000/')
#sortedFiles = sorted(files)

files = os.listdir('/home/juca/Documentos/10000to100000/') 
qtdRemovedNetworks = 0
qtdNetworks = 0
i = 0
fig = plt.figure(figsize=(20,50))
subs = []
subs.append(fig.add_subplot(511))

for f in files:
    if f.endswith('.gml'):
        qtdNetworks += 1
        fileAux = '/home/juca/Documentos/10000to100000/{0}'.format(f)
        xRemovedAux,yRemovedAux = readNetwork(fileAux)
        if xRemovedAux == 0:
            qtdRemovedNetworks += 1    
        else:
            subs[i].plot(xRemovedAux,yRemovedAux,label=qtdNetworks)    
            subs[i].legend(loc='best')
        if qtdNetworks % 5 == 0:
            i += 1
            if i+1 <= 5:
                subs.append(fig.add_subplot(int('51{0}'.format(str(i+1)))))
            break
            
fig.savefig('/home/juca/Documentos/10000to100000/networks10000to100000.png'.format(str(qtdNetworks)))
print(qtdRemovedNetworks)
plt.show()