import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

def get_signs_of_tris(tris_list, G):
    # tris_list = [[1,2,3],[4,5,6]]
    # all_signs = [['+','-','+'],[]]
    all_signs = []
    for i in range (len(tris_list)):
        temp = []
        temp.append(G[tris_list[i][0]][tris_list[i][1]]['sign'])
        temp.append(G[tris_list[i][1]][tris_list[i][2]]['sign'])
        temp.append(G[tris_list[i][0]][tris_list[i][2]]['sign'])
        all_signs.append(temp)
    return all_signs

def count_unstable(all_signs):
    stable = 0
    unstable = 0
    for i in range(len(all_signs)):
        if all_signs[i].count('+') == 3 or all_signs[i].count('+') == 1:
            stable += 1
        elif all_signs[i].count('+') == 0 or all_signs[i].count('+') == 2:
            unstable += 1

    balance_score = stable / (stable + unstable)
    if balance_score >=  0.5: 
    	print('The network is STABLE')
    else:
    	print('The network is UNSTABLE')
    print('Total number of triangles: ', stable + unstable)
    print('Number of stable triangles: ', stable)
    print('Number of unstable triangles: ', unstable)



G = nx.Graph()
n = 7
G.add_nodes_from([i for i in range(1, n+1)])
mapping = {1:'Alexandra',2:'Anterim', 3:'Bercy',4:'Bearland',5:'Eplex', 6:'Ron', 7:'Harry'}
G = nx.relabel_nodes(G, mapping)

signs = ['+', '-']
for i in G.nodes():
    for j in G.nodes():
        if i != j:
            G.add_edge(i, j, sign = random.choice(signs))

edge_labels = nx.get_edge_attributes(G, 'sign')
pos = nx.circular_layout(G)
nx.draw(G, pos, node_size = 2000, with_labels = True, font_size = 10)
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 20)

plt.show()

nodes = G.nodes()
tris_list = [list(x) for x in itertools.combinations(nodes, 3)]

all_signs = get_signs_of_tris(tris_list, G)

unstable = count_unstable(all_signs)