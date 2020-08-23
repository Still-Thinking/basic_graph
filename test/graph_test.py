from basic_graph.graph import *

def test_create_graph():
    t = Graph([],[])
    assert t is not None

def test_add_vertex():
    t = Graph([],[])
    t.add_vertex(1)
    assert type(t[1]) == dict
    assert t.vertex_count == 1

def test_add_edge():
    t = Graph([1,2],[])
    t.add_edge((1,2))
    assert t[1][2] == (1,2)
    assert t[2][1] == (1,2)
    assert t.edge_count == 1

def test_str():
    t = Graph([1,2],[(1,2)])
    assert t.__str__() == "Graph contains 2 vertices and 1 edge"

