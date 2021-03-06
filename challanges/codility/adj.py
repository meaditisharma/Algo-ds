from collections import defaultdict

class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def __str__(self):
        return '{} neighbors: {}'.format(
            self.key,
            [x.key for x in self.neighbors]
        )

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]


class Graph(object):
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        self.verticies[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.verticies[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.verticies

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.verticies:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.verticies:
            self.add_vertex(Vertex(to_key))
        self.verticies[from_key].add_neighbor(self.verticies[to_key], weight)

    def get_vertices(self):
        return self.verticies.keys()

    def __iter__(self):
        return iter(self.verticies.values())

g = Graph()
for i in range(10):
    g.add_vertex(Vertex(i))
g.verticies

T = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
for i in range(len(T)):
    g.add_edge(T[i], i)

for v in g:
    for w in v.get_connections():
        print('{} -> {}'.format(v.key, w.key))

