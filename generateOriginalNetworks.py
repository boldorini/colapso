import networkx as nx
import random

def createNetworks(qtd, minV, maxV, minE, maxE, path):    
    for i in range(qtd):
        while True:
            v = random.randint(minV,maxV)
            e = random.randint(minE,maxE)
            if (v > e):
                break
        G = nx.barabasi_albert_graph(v, e)
        nx.write_gml(G,"{}{:02d}_{}_{}.gml".format(path,i,v,e))

#Creation of small networks (1-1000 nodes / 1 to 50 links (all random))        
createNetworks(1, 1, 1000, 1, 50, "e:\\mestrado\\redesII\\1to1000\\")

#Creation of medium networks (1000-10000 nodes / 1 to 50 links (all random))    
createNetworks(1, 1000, 10000, 1, 50, "e:\\mestrado\\redesII\\1000to10000\\")

#Creation of big networks (10000-100000 nodes / 1 to 50 links (all random))
createNetworks(1, 10000, 100000, 1, 50, "e:\\mestrado\\redesII\\10000to100000\\")
    
#Creation of giant networks (100000-1000000 nodes / 1 to 30 links (all random))    
createNetworks(1, 100000, 1000000, 1, 30, "e:\\mestrado\\redesII\\100000to1000000\\")