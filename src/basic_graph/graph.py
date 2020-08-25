from .vertex import Vertex
from .edge import Edge

class Graph(dict):
    _vertex_count = 0
    _edge_count = 0
    _vertices = set()
    _edges = set()
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

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, _):
        pass

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, _):
        pass

    @classmethod
    def empty(cls):
        return Graph([],[])

    @classmethod
    def unconnected(cls, vertices):
        return Graph(vertices,[])

    @classmethod
    def fully_connected(cls, vertices):
        t = Graph(vertices, [])
        for v in vertices:
            for w in filter(lambda x: x != v, vertices):
                e = Edge(v,w)
                try:
                    t[v][w]
                except KeyError:
                    t.add_edge(e)
        return t

    @classmethod
    def regular_connected(cls, vertices, degree):
        assert degree < len(vertices)
        assert not ((degree % 2 ==1) and (len(vertices)%2==1))

        t = Graph(vertices, [])
        if degree % 2 == 0:
            for x in _make_rings(vertices, int(degree/2)):
                t.add_edge(x)
        else:
            half_len = int(len(vertices)/2)
            for x in _make_rings(vertices, int((degree-1)/2)):
                t.add_edge(x)
            for ix, v in enumerate(vertices[0:half_len]):
                t.add_edge(Edge(v, vertices[ix+half_len]))
        return t

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
        if v not in self.vertices:
            self[v]={}
            self._vertices.add(v)
            self._vertex_count += 1

    def remove_vertex(self, v):
        assert isinstance(v, Vertex), f"Must be a Vertex, not {type(v)}"
        assert v in self._vertices, f"{v} not in Graph"
        for w in self[v].keys():
            self.remove_edge(self[v][w])
        del self[v]
        self._vertices.remove(v)
        self._vertex_count -= 1

    def add_edge(self, e):
        assert isinstance(e, Edge), f"Must be a Edge, not {type(e)}"
        if e not in self._edges:
            v, w = e
            self[v][w] = e
            self[w][v] = e
            self._edges.add(e)
            self._edge_count += 1

    def remove_edge(self, e):
        assert isinstance(e, Edge), f"Must be a Vertex, not {type(e)}"
        assert e in self._edges, f"{e} not in Graph"
        v, w  = e
        del self[v][w]
        del self[w][v]
        self._edges.remove(e)
        self._edge_count -= 1

def _make_rings(vs, num_rings):
    edges = []
    for ix, v in enumerate(vs):
        for j in (x for x in range(-num_rings, num_rings+1) if x != 0):
            edges.append(Edge(v, vs[(ix+j)%len(vs)]))
    return edges

