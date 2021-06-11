# Import all the necessary dependencies
import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

def checkStability(tris_list, G):
    stable = []
    unstable = []
    for i in range(len(tris_list)):
        temp = []
        temp.append(G[tris_list[i][0]][tris_list[i][1]]['sign'])
        temp.append(G[tris_list[i][1]][tris_list[i][2]]['sign'])
        temp.append(G[tris_list[i][0]][tris_list[i][2]]['sign'])
        if(temp.count('+') % 2 == 0):
            unstable.append(tris_list[i])
        else:
            stable.append(tris_list[i])
    
    stableNum = len(stable)
    unstableNum = len(unstable)

    balance_score = stableNum / (stableNum + unstableNum)
    if balance_score == 1.0:
        print('The network is STRUCTURALLY BALANCED') 
    elif balance_score >=  0.9:
        print('The network is APPROXIMATELY STRUCTURALLY BALANCED')
    else:
        print('The network is Not STRUCTURALLY BALANCED')

    print("Stable triangles: ", stableNum)
    print("Unstable triangles: ", unstableNum)
    print("Number of Triangles: ", stableNum + unstableNum)
    return stable, unstable

if __name__ == "__main__":
    G = nx.Graph()

    n = 7
    G.add_nodes_from([i for i in range(1, n+1)])
  
    mapping = {}
    for i in range(1,n+1):
        mapping[i] = "Node" + str(i)
    G = nx.relabel_nodes(G, mapping)

    signs = ['+', '-']
    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                G.add_edge(i, j, sign = random.choice(signs))

    edges = G.edges()
    nodes = G.nodes()

    tris_list = [list(x) for x in itertools.combinations(nodes, 3)]
    stable, unstable = checkStability(tris_list, G)

    edge_labels = nx.get_edge_attributes(G, 'sign')
    pos = nx.circular_layout(G)

    nx.draw(G, pos, node_size = 2000, with_labels = True, font_size = 10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 15)

    Friends = [k for k, v in edge_labels.items() if v == '+']
    Enemies = [k for k, v in edge_labels.items() if v == '-']
    nx.draw_networkx_edges(G, pos, edgelist = Friends, edge_color="g")
    nx.draw_networkx_edges(G, pos, edgelist = Enemies, edge_color="r")
  
    plt.pause(10)

    for i in range(len(stable)):
        temp = [tuple(x) for x in itertools.combinations(stable[i], 2)]
        plt.cla()
        nx.draw(G, pos, node_size = 2000, with_labels = True, font_size = 10)
        nx.draw_networkx_edges(G, pos, edgelist = temp, edge_color="g", width = 6 )
        plt.pause(2)

    for i in range(len(unstable)):
        temp = [tuple(x) for x in itertools.combinations(unstable[i], 2)]
        plt.cla()
        nx.draw(G, pos, node_size = 2000, with_labels = True, font_size = 10)
        nx.draw_networkx_edges(G, pos, edgelist = temp, edge_color="r", width = 6)
        plt.pause(2)