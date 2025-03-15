import networkx as nx
from networkx.generators.random_graphs import barabasi_albert_graph
from networkx.generators.random_graphs import watts_strogatz_graph
from networkx.generators.random_graphs import erdos_renyi_graph
from scipy.stats import kendalltau
from statistics import mean
from statistics import stdev
from tqdm.std import trange

n,m_list,eval_times = 100,[1,2,3,4],1000
print("Evaluate BA Random Networks :")
for m in m_list :
    print("N = %d, M = %d" % (n,m))
    d = {'n':[], 'm':[], 'm_line_graph':[], 'm_en_graph':[], 'lg_score':[], 'en_score':[]}
    for rep in trange(eval_times) :
        g = barabasi_albert_graph(n, m)
        d['n'].append(len(g.nodes()))
        d['m'].append(len(g.edges()))
        c1 = nx.edge_betweenness_centrality(g)
        A = [c1[x] for x in g.edges()]
        g2 = nx.line_graph(g)
        d['m_line_graph'].append(len(g2.edges()))
        c2 = nx.betweenness_centrality(g2)
        B = [c2[v,u] if c2.get((u,v))==None else c2[u,v] for (u,v) in g.edges]
        corr1,_ = kendalltau(A, B)
        d['lg_score'].append(corr1)
        g3 = nx.Graph()
        for (u,v) in g.edges() :
            g3.add_edge(u,(u,v))
            g3.add_edge(v,(u,v))
        d['m_en_graph'].append(len(g3.edges()))
        c3 = nx.betweenness_centrality(g3)
        C = [c3[x] for x in g.edges()]
        corr2,_ = kendalltau(A, C)
        d['en_score'].append(corr2)
    f = open("../results/result_model.txt", "a")
    f.write('BA(n=%d,m=%d)' % (n,m))
    f.write(' %.2f±%.2f' % (mean(d['n']), stdev(d['n'])))
    f.write(' %.2f±%.2f' % (mean(d['m']), stdev(d['m'])))
    f.write(' %.2f±%.2f' % (mean(d['m_line_graph']), stdev(d['m_line_graph'])))
    print('Average Edges in Line Graph : %.2f±%.2f' % (mean(d['m_line_graph']), stdev(d['m_line_graph'])))
    f.write(' %.2f±%.2f' % (mean(d['m_en_graph']), stdev(d['m_en_graph'])))
    print('Average Edges in NodeEdge Graph : %.2f±%.2f' % (mean(d['m_en_graph']), stdev(d['m_en_graph'])))
    f.write(' %.4f±%.4f' % (mean(d['lg_score']), stdev(d['lg_score'])))
    print('Average Line Graph Score : %.4f±%.4f' % (mean(d['lg_score']), stdev(d['lg_score'])))
    f.write(' %.4f±%.4f\n' % (mean(d['en_score']), stdev(d['en_score'])))
    print('Average EdgeNode Graph Score : %.4f±%.4f\n' % (mean(d['en_score']), stdev(d['en_score'])))
    f.close()

n,k_list,p,eval_times = 100,[2,4,6,8],0.15,1000
print("Evaluate WS Random Networks :")
for k in k_list :
    print("N = %d, K = %d, P = %.2f" % (n,k,p))
    d = {'n':[], 'm':[], 'm_line_graph':[], 'm_en_graph':[], 'lg_score':[], 'en_score':[]}
    for rep in trange(eval_times) :
        g = watts_strogatz_graph(n,k,p)
        d['n'].append(len(g.nodes()))
        d['m'].append(len(g.edges()))
        c1 = nx.edge_betweenness_centrality(g)
        A = [c1[x] for x in g.edges()]
        g2 = nx.line_graph(g)
        d['m_line_graph'].append(len(g2.edges()))
        c2 = nx.betweenness_centrality(g2)
        B = [c2[v,u] if c2.get((u,v))==None else c2[u,v] for (u,v) in g.edges]
        corr1,_ = kendalltau(A, B)
        d['lg_score'].append(corr1)
        g3 = nx.Graph()
        for (u,v) in g.edges() :
            g3.add_edge(u,(u,v))
            g3.add_edge(v,(u,v))
        d['m_en_graph'].append(len(g3.edges()))
        c3 = nx.betweenness_centrality(g3)
        C = [c3[x] for x in g.edges()]
        corr2,_ = kendalltau(A, C)
        d['en_score'].append(corr2)
    f = open("../results/result_model.txt", "a")
    f.write('WS(n=%d,k=%d,p=%.2f)' % (n,k,p))
    f.write(' %.2f±%.2f' % (mean(d['n']), stdev(d['n'])))
    f.write(' %.2f±%.2f' % (mean(d['m']), stdev(d['m'])))
    f.write(' %.2f±%.2f' % (mean(d['m_line_graph']), stdev(d['m_line_graph'])))
    print('Average Edges in Line Graph : %.2f±%.2f' % (mean(d['m_line_graph']), stdev(d['m_line_graph'])))
    f.write(' %.2f±%.2f' % (mean(d['m_en_graph']), stdev(d['m_en_graph'])))
    print('Average Edges in NodeEdge Graph : %.2f±%.2f' % (mean(d['m_en_graph']), stdev(d['m_en_graph'])))
    f.write(' %.4f±%.4f' % (mean(d['lg_score']), stdev(d['lg_score'])))
    print('Average Line Graph Score : %.4f±%.4f' % (mean(d['lg_score']), stdev(d['lg_score'])))
    f.write(' %.4f±%.4f\n' % (mean(d['en_score']), stdev(d['en_score'])))
    print('Average EdgeNode Graph Score : %.4f±%.4f\n' % (mean(d['en_score']), stdev(d['en_score'])))
    f.close()

n,p_list,eval_times = 100,[0.02,0.03,0.04,0.05],1000
print("Evaluate ER Random Networks :")
for p in p_list :
    print("N = %d, P = %.2f" % (n,p))
    d = {'n':[], 'm':[], 'm_line_graph':[], 'm_en_graph':[], 'lg_score':[], 'en_score':[]}
    for rep in trange(eval_times) :
        g = erdos_renyi_graph(n,p)
        d['n'].append(len(g.nodes()))
        d['m'].append(len(g.edges()))
        c1 = nx.edge_betweenness_centrality(g)
        A = [c1[x] for x in g.edges()]
        g2 = nx.line_graph(g)
        d['m_line_graph'].append(len(g2.edges()))
        c2 = nx.betweenness_centrality(g2)
        B = [c2[v,u] if c2.get((u,v))==None else c2[u,v] for (u,v) in g.edges]
        corr1,_ = kendalltau(A, B)
        d['lg_score'].append(corr1)
        g3 = nx.Graph()
        for (u,v) in g.edges() :
            g3.add_edge(u,(u,v))
            g3.add_edge(v,(u,v))
        d['m_en_graph'].append(len(g3.edges()))
        c3 = nx.betweenness_centrality(g3)
        C = [c3[x] for x in g.edges()]
        corr2,_ = kendalltau(A, C)
        d['en_score'].append(corr2)
    f = open("../results/result_model.txt", "a")
    f.write('ER(n=%d,p=%.2f)' % (n,p))
    f.write(' %.2f±%.2f' % (mean(d['n']), stdev(d['n'])))
    f.write(' %.2f±%.2f' % (mean(d['m']), stdev(d['m'])))
    f.write(' %.2f±%.2f' % (mean(d['m_line_graph']), stdev(d['m_line_graph'])))
    print('Average Edges in Line Graph : %.2f±%.2f' % (mean(d['m_line_graph']), stdev(d['m_line_graph'])))
    f.write(' %.2f±%.2f' % (mean(d['m_en_graph']), stdev(d['m_en_graph'])))
    print('Average Edges in NodeEdge Graph : %.2f±%.2f' % (mean(d['m_en_graph']), stdev(d['m_en_graph'])))
    f.write(' %.4f±%.4f' % (mean(d['lg_score']), stdev(d['lg_score'])))
    print('Average Line Graph Score : %.4f±%.4f' % (mean(d['lg_score']), stdev(d['lg_score'])))
    f.write(' %.4f±%.4f\n' % (mean(d['en_score']), stdev(d['en_score'])))
    print('Average EdgeNode Graph Score : %.4f±%.4f\n' % (mean(d['en_score']), stdev(d['en_score'])))
    f.close()