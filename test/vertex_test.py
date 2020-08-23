from basic_graph.vertex import *

def test_can_create_vertex():
    t = Vertex('')
    assert isinstance(t,Vertex)

def test_can_represent_vertex():
    t = Vertex("Test")
    assert t.__str__() == "Vertex: (Test)"
