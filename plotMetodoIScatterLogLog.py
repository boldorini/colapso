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
   x= np.log(x)
   y = np.log(y)   
   return x, y

#######################################################
def getGraphParams(metodo, conjunto):
    redes = ''
    
    if conjunto == 'A':       
        redes = '100to1000'
        qtdeRedesAnalisadas = 5
    elif conjunto == 'B':
        redes = '1000to10000'
        qtdeRedesAnalisadas = 5
    elif conjunto == 'C':
        redes = '10000to100000'
        qtdeRedesAnalisadas = 5
    elif conjunto == 'D':
        redes = '100000to1000000'
        if metodo == 'I':
            qtdeRedesAnalisadas = 1
        else:
            qtdeRedesAnalisadas = 3
    
    if (metodo == 'originais'):
        titleGrafico = 'Distribuição de graus - Redes Originais - Conjunto {}'.format(conjunto)
        pathGrafos = 'D:\\mestrado\\redes\\{}\\redesOriginais'.format(redes)
        pathFiguras = 'D:\\mestrado\\python\\correcao\\plotRedes\\originais\\{}\\'.format(redes)        
    else:    
        titleGrafico = 'Distribuição de graus - Método {} - Conjunto {}'.format(metodo, conjunto)
        pathGrafos = 'D:\\mestrado\\redes\\{}\\metodo{}'.format(redes,metodo)
        pathFiguras = 'D:\\mestrado\\python\\correcao\\plotRedes\\metodo{}\\{}\\'.format(metodo,redes)
        
    return titleGrafico, pathGrafos, pathFiguras, qtdeRedesAnalisadas
#######################################################

def plotGraphs(titleGrafico, pathGrafos, pathFiguras, qtdeRedesAnalisadas):
    files = os.listdir(pathGrafos) 
    qtdNetworks = 0
    markersArray = ['o','+','s','*','^']
    for f in files:    
        if f.endswith('.gml'):
            fileAux = '{0}\\{1}'.format(pathGrafos,f)        
            qtdNetworks += 1
            xRemovedAux,yRemovedAux = readNetwork(fileAux)
            plt.scatter(xRemovedAux,yRemovedAux,label=qtdNetworks,marker=markersArray[qtdNetworks % 3 - 1])    
            plt.legend(loc='best')
            plt.xlabel("Grau dos vértices (log)")
            plt.ylabel("Quantidade de vértices (log)")
            if qtdNetworks % qtdeRedesAnalisadas == 0:
                if metodo == 'I' and conjunto == 'D':
                    title = '{} - Rede 1'.format(titleGrafico)        
                else:                        
                    title = '{} - Redes {} a {}'.format(titleGrafico, qtdNetworks - (qtdeRedesAnalisadas - 1), qtdNetworks)        
                plt.title(title)            
                plt.savefig('{}\\{:02d}to{:02d}.png'.format(pathFiguras, qtdNetworks - (qtdeRedesAnalisadas - 1), qtdNetworks))
                plt.show()
    plt.show()
    

#metodos = ['I','II','III']
#metodos = ['II','III']
conjuntos = ['D']
metodos = ['originais']
#conjuntos = ['A','B','C','D']

for metodo in metodos:
    for conjunto in conjuntos:
      #print(getGraphParams(metodo, conjunto))
      titleGrafico, pathGrafos, pathFiguras, qtdeRedesAnalisadas = getGraphParams(metodo, conjunto)
      plotGraphs(titleGrafico, pathGrafos, pathFiguras, qtdeRedesAnalisadas)