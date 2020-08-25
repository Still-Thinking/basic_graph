from basic_graph.graph import *
from basic_graph.vertex import Vertex
from basic_graph.edge import Edge

def test_create_graph():
    t = Graph([],[])
    assert t is not None

def test_add_vertex():
    t = Graph([],[])
    a = Vertex("a")
    t.add_vertex(a)
    assert type(t[a]) == dict
    assert t.vertex_count == 1

def test_add_edge():
    a = Vertex("a")
    b = Vertex("b")
    e = Edge(a,b)
    t = Graph([a,b],[])
    t.add_edge(e)
    assert t[a][b] == e
    assert t[b][a] == e
    assert t.edge_count == 1

def test_str():
    a = Vertex("a")
    b = Vertex("b")
    e = Edge(a,b)
    t = Graph([a,b],[e])
    assert t.__str__() == "Graph contains 2 vertices and 1 edge"

def test_create_empty_graph():
    t = Graph.empty()
    assert isinstance(t,Graph)
    assert t.vertex_count == 0
    assert t.edge_count == 0
    assert len(list(t.keys())) == 0

def test_create_unconnected_graph():
    a = Vertex(1)
    t = Graph.unconnected([a])
    assert isinstance(t,Graph)
    assert t.vertex_count == 1
    assert t.edge_count == 0
    assert len(list(t.keys())) == 1

def test_create_fully_connected_graph():
    vs= [Vertex(x) for x in "abcdef"]
    t = Graph.fully_connected(vs)
    assert t.vertex_count == 6
    assert t.edge_count == 15
