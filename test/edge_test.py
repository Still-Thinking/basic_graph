from basic_graph.edge import *

def test_can_create_edge():
    t = Edge(1,2)
    assert isinstance(t,Edge)

