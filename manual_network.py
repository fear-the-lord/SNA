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
    # Number of nodes
    n = 6
    
    # G.add_nodes_from([i for i in range(1, n+1)])
    # mapping = {1:'Alexandra',2:'Anterim', 3:'Bercy',4:'Bearland',5:'Eplex', 6:'Ron'}

    # Hard Coding positions for better presentation
    G.add_node(1,pos=(2,3))
    G.add_node(2,pos=(1,2))
    G.add_node(3,pos=(2,1))
    G.add_node(4,pos=(4,3))
    G.add_node(5,pos=(5,2))
    G.add_node(6,pos=(4,1))
  
    mapping = {}
    for i in range(1,n+1):
        mapping[i] = "Node" + str(i)
    G = nx.relabel_nodes(G, mapping)
    
    # Hard coding the signs
    G.add_edge( 'Node1', 'Node2', sign ='+')
    G.add_edge( 'Node1', 'Node3', sign ='+')
    G.add_edge( 'Node1', 'Node4', sign ='-')
    G.add_edge( 'Node1', 'Node5', sign ='-')
    G.add_edge( 'Node1', 'Node6', sign ='-')
    G.add_edge( 'Node2', 'Node3', sign ='+')
    G.add_edge( 'Node2', 'Node4', sign ='-')
    G.add_edge( 'Node2', 'Node5', sign ='-')
    G.add_edge( 'Node2', 'Node6', sign ='-')
    G.add_edge( 'Node3', 'Node4', sign ='-')
    G.add_edge( 'Node3', 'Node5', sign ='-')
    G.add_edge( 'Node3', 'Node6', sign ='-')
    G.add_edge( 'Node4', 'Node5', sign ='+')
    G.add_edge( 'Node4', 'Node6', sign ='+')
    G.add_edge( 'Node5', 'Node6', sign ='+')
    
    # # Random signs
    # G = nx.relabel_nodes(G, mapping)
    # signs = ['+', '-']
    # for i in G.nodes():
    #     for j in G.nodes():
    #         if i != j:
    #             G.add_edge(i, j, sign = random.choice(signs))

    edges = G.edges()
    nodes = G.nodes()

    tris_list = [list(x) for x in itertools.combinations(nodes, 3)]
    stable, unstable = checkStability(tris_list, G)

    edge_labels = nx.get_edge_attributes(G, 'sign')
    # pos = nx.circular_layout(G)
    pos = nx.spring_layout(G)

    # Getting positions from the nodes
    pos=nx.get_node_attributes(G,'pos')

    nx.draw(G, pos, node_size = 2000, with_labels = True, font_size = 10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 15)

    Friends = [k for k, v in edge_labels.items() if v == '+']
    Enemies = [k for k, v in edge_labels.items() if v == '-']
    nx.draw_networkx_edges(G, pos, edgelist = Friends, edge_color="g")
    nx.draw_networkx_edges(G, pos, edgelist = Enemies, edge_color="r")
    
    # plt.savefig("network.png", format="PNG")
    plt.show()
    
    # # Uncomment this to see individual triangle states
    # plt.pause(10)

    # for i in range(len(stable)):
    #     temp = [tuple(x) for x in itertools.combinations(stable[i], 2)]
    #     plt.cla()
    #     nx.draw(G, pos, node_size = 2000, with_labels = True, font_size = 10)
    #     nx.draw_networkx_edges(G, pos, edgelist = temp, edge_color="g", width = 6 )
    #     # plt.savefig("stable{}.png".format(i), format="PNG")
    #     plt.pause(2)
    
    # plt.show()
    # for i in range(len(unstable)):
    #     temp = [tuple(x) for x in itertools.combinations(unstable[i], 2)]
    #     plt.cla()
    #     nx.draw(G, pos, node_size = 2000, with_labels = True, font_size = 10)
    #     nx.draw_networkx_edges(G, pos, edgelist = temp, edge_color="r", width = 6)
    #     plt.pause(2)
    
