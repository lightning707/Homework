from pythonds.basic import Queue
from collections import defaultdict


class Vertex:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.adjacents = {}

        self.color = 'white'
        self.prev_vertex = None

    def add_adjacent(self, adj, weight=0):
        self.adjacents[adj] = weight

    def get_adjacents(self):
        return self.adjacents.keys()

    def get_weight(self, adj):
        return self.adjacents.get(adj)

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_prev_vertex(self, prev_vertex):
        self.prev_vertex = prev_vertex

    def __str__(self):
        return f"{self.key}: {[adj.key for adj in self.adjacents]}"

    def __repr__(self):
        return f"{self.key}: {[adj.key for adj in self.adjacents]}"


class Graph:
    def __init__(self):
        self.vertices = {}
        self.graph_size = 0
        self.start_vertex = None

    def add_vertex(self, key, value=None):
        self.vertices[key] = Vertex(key, value)
        self.graph_size += 1
        return self.vertices[key]

    def get_vertex(self, key):
        return self.vertices.get(key)

    def get_vertices(self):
        return [vert for vert in self.vertices.values()]

    def add_edge(self, first_vertex, second_vertex, weight=0) -> None:
        self.vertices[first_vertex].add_adjacent(self.vertices[second_vertex], weight)

    def set_start_vertex(self, key):
        self.start_vertex = key

    def __contains__(self, key):
        return key in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())


def is_similar(word1, word2, difference_max=1):
    difference = 0
    for char_id in range(len(word1)):
        if word1[char_id] != word2[char_id]:
            difference += 1
    return difference <= difference_max


def build_graph(filename: str):
    with open(filename, 'r') as fd:
        word_list = fd.read().split()
    graph = Graph()
    for word in word_list:
        graph.add_vertex(word)

    for ind1, word1 in enumerate(word_list):
        for word2 in word_list[ind1:]:
            if is_similar(word1, word2):
                graph.add_edge(word1, word2)
                graph.add_edge(word2, word1)
    return graph


print(build_graph('vocabulary.txt').get_vertices())
