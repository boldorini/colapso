import networkx as nx
import copy

def readNetwork(path,file):    
    network = path + file
    G = nx.read_gml(network)
    GRemoved = nx.read_gml(network)
    networkDensity = nx.density(G)
    nodesOfG = len(nx.nodes(G))
    possibleLinks = (nodesOfG * (nodesOfG - 1)) / 2     
    for n in G.nodes():
      GDensity = copy.deepcopy(G)
      GDensity.remove_node(str(n))
      density = len(nx.edges(GDensity))/possibleLinks
      iota = density/networkDensity
      #print('{}/{} = {} | iota = {}/{} = 1 - {} = {}'.format(len(nx.edges(GDensity)), possibleLinks, density, networkDensity, density, iota, 1 - iota))
      if (1 - round(iota,4)) >= 0.0014:
          GRemoved.remove_node(str(n))
    nx.write_gml(GRemoved,'{}00_removed_método_I_{}_{}.gml'.format(path,len(GRemoved.nodes()),len(GRemoved.edges())))    
    

path = 'E:\\mestrado\\redesII\\1to1000\\'
file = '00_864_19.gml' 
readNetwork(path,file)


# path = 'E:\\mestrado\\redesII\\1000to10000\\'
# file = '00_6047_32.gml'
# readNetwork(path,file)

# path = 'E:\\mestrado\\redesII\\10000to100000\\' 
# file = '00_10315_14.gml'
# readNetwork(path,file)

# path = 'E:\\mestrado\\redesII\\100000to1000000\\' 
# file = '00_559585_2.gml' 
# readNetwork(file)

