import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import collections

def readNetwork(file):
   network = nx.read_gml(file)
   networkGroupingNodes = collections.Counter()    
   for node in network.nodes:
       networkGroupingNodes[network.degree(node)] += 1
   orderedNodes = sorted(networkGroupingNodes.items(), key=lambda x:x[1], reverse=True)
   x,y = zip(*orderedNodes)
   
   x = np.log(x)
   y = np.log(y)   
   return x, y

files = os.listdir('/home/juca/Documentos/10000to100000/') 
qtdRemovedNetworks = 0
qtdNetworks = 0
i = 0
subs = []
for f in files:
    if f.endswith('.gml'):
        qtdNetworks += 1
        fileAux = '/home/juca/Documentos/10000to100000/{0}'.format(f)
        xRemovedAux,yRemovedAux = readNetwork(fileAux)
        if xRemovedAux == 0:
            qtdRemovedNetworks += 1    
        else:
            subs[i].scatter(xRemovedAux,yRemovedAux,label=qtdNetworks)    
            subs[i].legend(loc='best')
        if qtdNetworks % 5 == 0:
            i += 1
            if i+1 <= 5:
                subs.append(fig.add_subplot(int('51{0}'.format(str(i+1)))))
            break
     fig.savefig('C:\\Users\\boldo\\OneDrive\\Documentos\\Dissertação\\imagens\\100to1000plots\{}.png'.format(str(qtdNetworks)))