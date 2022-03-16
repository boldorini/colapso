import networkx as nx

def readNetwork(path,file):    
    network = path + file
    G           = nx.read_gml(network)
    GRemoved    = nx.read_gml(network)        
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
    nx.write_gml(GRemoved,'{}00_{}_{}_removed_metodoIII.gml'.format(path,len(GRemoved.nodes()),len(GRemoved.edges())))    
    

# path = 'E:\\mestrado\\redesII\\1to1000\\'
# file = '00_864_19.gml' 
# readNetwork(path,file)

# path = 'E:\\mestrado\\redesII\\1000to10000\\'
# file = '00_6047_192480.gml'
# readNetwork(path,file)

path = 'G:\\Meu Drive\\Mestrado\\defesa\\método II\\''
file = 'CE-CX.txt'
readNetwork(path,file)

# path = 'E:\\mestrado\\redesII\\10000to100000\\' 
# file = '00_10315_14.gml'
# readNetwork(path,file)

# path = 'E:\\mestrado\\redesII\\100000to1000000\\' 
# file = '00_559585_2.gml' 
# readNetwork(file)