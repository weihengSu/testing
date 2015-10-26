__author__ = 'ws2ta'

import unittest
from graph import Graph
from graph_functions import *

class TestGraphFunction(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph({'A':['B','C'], 'B': ['A','C'],'C':['A','B']})
        self.g2 = Graph({'A':['B','C'], 'B': ['A','C'],'C':['A','B'], 'E':[]})
        self.g3 = []
        self.g4 = Graph({'A':['B','C','E'], 'B': ['A','C'],'C':['A','B'], 'E':['A']})
        self.g5 = Graph({'A':[]})
        self.g6 = Graph({})

    """test is_complete()"""
    def test_is_complete(self):
        assert is_complete(self.g1) == True, "g1 is a complete function so it should return true"
        assert is_complete(self.g2) == False, "g2 is not complete function since it has a node that is connected. It should return false"
        self.assertRaises(TypeError, self.g3), "g3 is not a graph function, so it should raise TypeError"
        assert is_complete(self.g4) == False, "g4 is not complete because not every node is connected to other nodes. It should return false"
        assert is_complete(self.g5) == True, "g5 contains only one node, so it should return true"
        assert is_complete(self.g6) == True, "g6 does not contain any node, so it should return true"

    """ test notes_by_degree()"""
    def test_notes_by_degree(self):
        assert sorted(notes_by_degree(self.g1)) == [('A', 2),('B', 2),('C', 2)], "notes_by_degree(g1) should return all nodes with a degree of 2 "
        assert sorted(notes_by_degree(self.g2)) == [('A', 2),('B',2),('C',2),('E',0)],"notes_by_degree(g2) should return nodes A, B, and C with a degree of 2 and node E with a degree of 0 "
        self.assertRaises(TypeError, self.g3), "This is not a graph function, so it raises TypeError"
        assert sorted(notes_by_degree(self.g4)) == [('A',3),('B', 2),('C', 2),('E', 1)], "It should return node A with a degree of 3, nodes B and C with a degree of 2, and E with a degree 1 "
        assert notes_by_degree(self.g5) == [('A', 0)], "The graph only contains one node, and it should return a node with a degree of 0"
        assert notes_by_degree(self.g6) == [], "The graph is empty, so it should return nothing"
