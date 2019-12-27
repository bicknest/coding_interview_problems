from best_line import best_line

def test_simple_graph():
    graph = [(0, 0), (1, 1), (2, 2), (1, 2), (2, 4)]
    assert best_line(graph) == (1, 0)
