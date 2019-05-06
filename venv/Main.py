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