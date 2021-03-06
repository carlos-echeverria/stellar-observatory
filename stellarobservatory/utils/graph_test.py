"""Test graph utilities"""
from .graph import get_transpose_graph, get_indegrees, get_induced_subgraph

GRAPH = {
        1: {2, 3},
        2: {3},
        3: {2}
    }

def test_get_transpose_graph():
    """Test get_transpose_graph() with a graph"""
    transpose = get_transpose_graph(GRAPH)
    assert transpose == {
        1: set(),
        2: {1, 3},
        3: {1, 2}
    }

def test_get_indegrees():
    """Test get_indegrees() with a graph"""
    assert get_indegrees(GRAPH) == {1: 0, 2: 2, 3: 2}

def test_get_induced_subgraph():
    """Test get_induced_subgraph() with a graph"""
    assert get_induced_subgraph(GRAPH, {1, 2, 3}) == GRAPH
    assert get_induced_subgraph(GRAPH, {1}) == {1: set()}
    assert get_induced_subgraph(GRAPH, {1, 2}) == {1: {2}, 2: set()}
    assert get_induced_subgraph(GRAPH, {2, 3}) == {2: {3}, 3: {2}}
    assert get_induced_subgraph(GRAPH, set()) == dict()
