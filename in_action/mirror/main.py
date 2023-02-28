import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import utils

Row, Col = 5, 5
Color_Num = 5
Colors = list(range(1, Color_Num + 1))

X, Y = 3, 2


class Cluster:
    def __init__(self, color) -> None:
        self.color = color
        self.nodes = []
        self.gccs = []
        self.matchs = []

    def add_node(self, node):
        self.nodes.append(node)
        self.refresh()

    def remove_node(self, node):
        self.nodes.remove(node)
        self.refresh()

    def refresh(self):
        self.gen_gcc()
        self.gen_match()

    def gen_gcc(self):
        self.gccs = []
        for node in self.nodes:
            linked = False
            for gcc in self.gccs:
                if any(self.is_neighbor(n, node) for n in gcc):
                    gcc.append(node)
                    linked = True

            if not linked:
                self.gccs.append([node,])

    def is_neighbor(self, node1, node2):
        return all(abs(node1[i] - node2[i]) <= 1 for i in range(2))

    def middle_node(self, node1, node2):
        if any((node1[i] + node2[i]) % 2 for i in range(2)):
            return (-1, -1)

        return tuple(int((node1[i] + node2[i]) / 2) for i in range(2))

    def gen_match(self):
        self.matchs = []
        for gcc in self.gccs:
            size = len(gcc)
            if size < 3:
                continue

            match = set()
            for i in range(size):
                for j in range(i + 1, size):
                    middle_node = self.middle_node(gcc[i], gcc[j])
                    if middle_node in gcc and self.is_neighbor(gcc[i], middle_node):
                        match.add(gcc[i])
                        match.add(gcc[j])
                        match.add(middle_node)
            if match:
                self.matchs.append(list(match))

    def has_match(self):
        return bool(self.matchs)

    def max_match_size(self):
        if self.matchs:
            return max(len(match) for match in self.matchs)

        return 0

    def max_gcc_size(self):
        return max(len(gcc) for gcc in self.gccs)

    def size(self):
        return len(self.nodes)


def plot():
    net = np.zeros((Row, Col), dtype=np.int8)

    # net = np.array(
    #     [[3, 2, 4, 3, 3],
    #      [5, 3, 2, 1, 2],
    #      [1, 2, 2, 4, 4],
    #      [5, 5, 4, 2, 4],
    #      [1, 4, 4, 5, 5]]
    # )

    clusters = {c: Cluster(c) for c in Colors}

    for i in range(net.shape[0]):
        for j in range(net.shape[1]):
            c = random.choice(Colors)
            net[i, j] = c
            # c = net[i, j]
            clusters[c].add_node((i, j))

    print(net)

    for c, cluster in clusters.items():
        # print(cluster.nodes)
        # print(cluster.gccs)

        if cluster.matchs:
            print(cluster.matchs)

    cluster_list = list(clusters.values())
    cluster_list.sort(key=lambda x: 10 * x.max_match_size() + x.max_gcc_size(), reverse=True)

    match_size_list = []
    for cluster in cluster_list:
        for match in cluster.matchs:
            match_size_list.append(len(match))

    if max(match_size_list) == X and match_size_list.count(X) == Y:
        pass
    else:
        pass

    plt.imshow(net)
    plt.show()


def main():
    plot()
    print("hello, world")


if __name__ == "__main__":
    main()
