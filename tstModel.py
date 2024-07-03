import networkx as nx

from model.model import Model
myModel=Model()
myModel.buildGraph(5)
myModel.printGraphDeteils()
v0=myModel.getAllNodes()[0]
connessa=list(nx.node_connected_component(myModel._grafo, v0))
v1=connessa[10]
pathDi=myModel.trovaCamminoDijkstra(v0,v1)
pathB=myModel.trovaCamminoBFS(v0,v1)
pathD=myModel.trovaCamminoDFS(v0,v1)
print(pathDi,sep="\n")
print(pathB,sep="\n")
print(pathD,sep="\n")