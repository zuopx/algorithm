import random

Row, Col = 5, 5
Color_Num = 5

X, Y = 4, 1


class Mirror:
    def __init__(self, row, col, color_num):
        self.row = row
        self.col = col
        self.color_num = color_num
        self.nodes = [[Node((r, c), random.choice(range(color_num))) for c in range(col)]
                      for r in range(row)]  # type: list[list[Node]]

        self.gen_neibor()

    def gen_neibor(self):
        pass

    def __str__(self) -> str:
        s = ""

        for r in range(self.row):
            s += 4 * self.col * " " + "\n"
            for c in range(self.col):
                s += f"  {self.nodes[r][c].color} "
            s += " \n"
        s += 4 * self.col * " "

        return s


class Cluster:
    def __init__(self, color):
        self.color = color
        self.nodes = []  # type: list[Node]
        self.gccs = []  # type: list[GCC]

    @property
    def size(self):
        return len(self.nodes)


class GCC:
    def __init__(self, cluster, node):
        self.nodes = [node,]  # type: list[Node]
        self.cluster = cluster  # type: Cluster
        self.match = None  # type: Match

    @property
    def color(self):
        return self.cluster.color

    @property
    def size(self):
        return len(self.nodes)

    @property
    def match_size(self):
        return self.match.size if self.match else 0


class Match:
    def __init__(self, gcc, nodes):
        self.nodes = nodes  # type: list[Node]
        self.gcc = gcc  # type: GCC

    @property
    def color(self):
        return self.gcc.color

    @property
    def size(self):
        return len(self.nodes)

    @property
    def gcc_size(self):
        return self.gcc.size


class Node:
    def __init__(self, pos: tuple, color):
        self.pos = pos
        self.color = color
        self.gcc = None  # type: GCC
        self.match = None  # type: Match
        self.neibors = []