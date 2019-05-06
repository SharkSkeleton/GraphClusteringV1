# Variant with random nums on edges
#
# import networkx as nx
# import matplotlib.pyplot as plt
#
# def draw_graph(graph, labels=None, graph_layout='shell',
#                node_size=1600, node_color='blue', node_alpha=0.3,
#                node_text_size=12,
#                edge_color='blue', edge_alpha=0.3, edge_tickness=1,
#                edge_text_pos=0.3,
#                text_font='sans-serif'):
#
#     # create networkx graph
#     G=nx.Graph()
#
#     # add edges
#     for edge in graph:
#         G.add_edge(edge[0], edge[1])
#
#     # these are different layouts for the network you may try
#     # shell seems to work best
#     if graph_layout == 'spring':
#         graph_pos=nx.spring_layout(G)
#     elif graph_layout == 'spectral':
#         graph_pos=nx.spectral_layout(G)
#     elif graph_layout == 'random':
#         graph_pos=nx.random_layout(G)
#     else:
#         graph_pos=nx.shell_layout(G)
#
#     # draw graph
#     nx.draw_networkx_nodes(G,graph_pos,node_size=node_size,
#                            alpha=node_alpha, node_color=node_color)
#     nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
#                            alpha=edge_alpha,edge_color=edge_color)
#     nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
#                             font_family=text_font)
#
#     if labels is None:
#         labels = range(len(graph))
#
#     edge_labels = dict(zip(graph, labels))
#     nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels,
#                                  label_pos=edge_text_pos)
#
#     # show graph
#     plt.show()
#
# graph = [(0, 1), (1, 9), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9),
#          (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
#
# # you may name your edge labels
# labels = map(chr, range(65, 65+len(graph)))
# #draw_graph(graph, labels)
#
# # if edge labels is not specified, numeric labels (0, 1, 2...) will be used
# draw_graph(graph)

# Variant of empty random graph
import networkx as nx
import matplotlib.pyplot as plt
import random as r

def draw_graph(graph):

    # extract nodes from graph
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    # create networkx graph
    G=nx.Graph()

    # add nodes
    for node in nodes:
        G.add_node(node)

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # draw graph
    pos = nx.shell_layout(G)
    nx.draw(G, pos)

    # show graph
    plt.show()

def Union(lst1, lst2):
    final_list = lst1 + lst2
    return final_list


def Difference(first, second):
    second = set(second)
    return [item for item in first if item not in second]

def main():
    # draw example
    a = r.randint(1,6)

    graph = [(1, 2),(2, 3),(3, 4), (4, 5),(5, 6), (6, 1)]
    matrix = nx.Graph(graph)

    print(nx.adjacency_matrix(matrix))
    # print(matrix.has_edge(1,6))

    unionCounter = 0
    differenceCounter = 0
    deltaCounter = 0

    for i in range(7):
        for j in range(7):
            if(matrix.has_edge(i,j)):
                print("Существующие ребра: ",matrix.has_edge(i,j), i, j)
                unionCounter += 1

    print("\nКол-во всех ребер: ",unionCounter)

    # print(list(matrix.neighbors(6)))

    print("\nПример на вершинах 1,3")

    if(matrix.neighbors(1) == matrix.neighbors(3)):
        print("Расстояние Чеконовского-Дайса: ",0)
    else:
        listUnion = Union(list(matrix.neighbors(1)), list(matrix.neighbors(3)))
        listUnion = list(dict.fromkeys(listUnion))

        listDifference = Union(Difference(list(matrix.neighbors(1)), list(matrix.neighbors(3))), Difference(list(matrix.neighbors(3)), list(matrix.neighbors(1))))

        a = listUnion.__len__()
        b = listDifference.__len__()
        c = a - b

        print("\nВсе вершины до которых данные могут имеют путь: ",listUnion, a)
        print("Общие вершины для данных вершин: ",listDifference, b)

        print("Расстояние Чеконовского-Дайса: ",(c)/(a+b))

    for i in range(1,7):
        for j in range(1,7):
            if(matrix.neighbors(i)==matrix.neighbors(j)):
                print("Расстояние Чеконовского-Дайса: ", 0, i, j)
            else:
                print("\nПример на вершинах: ", i, j)
                listUnion = Union(list(matrix.neighbors(i)), list(matrix.neighbors(j)))
                listUnion = list(dict.fromkeys(listUnion))

                listDifference = Union(Difference(list(matrix.neighbors(i)), list(matrix.neighbors(j))),
                                       Difference(list(matrix.neighbors(j)), list(matrix.neighbors(i))))

                a = listUnion.__len__()
                b = listDifference.__len__()
                c = a - b

                print("\nВсе вершины до которых данные могут имеют путь: ", listUnion, a)
                print("Общие вершины для данных вершин: ", listDifference, b)

                print("Расстояние Чеконовского-Дайса: ", (c) / (a + b))
    # some = [nx.adjacency_matrix(g)]
    # print(some)

    draw_graph(graph)

if __name__ == "__main__":
    main()