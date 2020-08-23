class Edge(tuple):
    def __new__(cls, a, b):
        return tuple.__new__(cls, (a,b))

    def __repr__(self):
        return f"Edge({repr(self[0])}, {repr(self[1])})"
