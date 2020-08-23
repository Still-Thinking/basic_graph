from .vertex import Vertex
from .edge import Edge

class Graph(dict):
    _vertex_count = 0
    _edge_count = 0
    @property
    def vertex_count(self):
        return self._vertex_count
    @vertex_count.setter
    def vertex_count(self, _):
        pass
    @property
    def edge_count(self):
        return self._edge_count
    @edge_count.setter
    def edge_count(self, _):
        pass

    @classmethod
    def empty(cls):
        return Graph([],[])

    @classmethod
    def unconnected(cls, vertices):
        return Graph(vertices,[])

    def __str__(self):
        v, e = (self.vertex_count, self.edge_count)
        return f"Graph contains {v} vertices and {e} edge"

    def __init__(self, vertices, edges):
        for v in vertices:
            self.add_vertex(v)
        for e in edges:
            self.add_edge(e)

    def add_vertex(self, v):
        assert isinstance(v, Vertex), f"Must be a Vertex, not {type(v)}"
        self[v]={}
        self._vertex_count += 1

    def add_edge(self, e):
        assert isinstance(e, Edge), f"Must be a Edge, not {type(e)}"
        v, w = e
        self[v][w] = e
        self[w][v] = e
        self._edge_count += 1
