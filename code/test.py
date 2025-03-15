import networkx as nx
from networkx.readwrite.edgelist import read_edgelist
from scipy.stats import kendalltau
import sys

gname = sys.argv[1]
g = read_edgelist("../data/"+gname+".txt", nodetype=int)
print("%s %d %d" % (gname, len(g.nodes()), len(g.edges())))
c1 = nx.edge_betweenness_centrality(g)
A = [c1[x] for x in g.edges()]
g2 = nx.line_graph(g)
c2 = nx.betweenness_centrality(g2)
B = [c2[v,u] if c2.get((u,v))==None else c2[u,v] for (u,v) in g.edges]
corr1,_ = kendalltau(A, B)
print("Line Graph : %d %d" % (len(g2.nodes()), len(g2.edges())))
print("Line Graph Score : %.4f" % corr1)
n = len(g.nodes())
g3 = nx.Graph()
for (u,v) in g.edges() :
    g3.add_edge(u,(u,v))
    g3.add_edge(v,(u,v))
c3 = nx.betweenness_centrality(g3)
C = [c3[x] for x in g.edges()]
corr2,_ = kendalltau(A, C)
print("EdgeNode Graph : %d %d" % (len(g3.nodes()), len(g3.edges())))
print("EdgeNode Graph Score : %.4f" % corr2)
