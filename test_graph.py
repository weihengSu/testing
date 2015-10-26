__author__ = 'weiheng su'
import unittest
from graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.g1 = Graph( {'A':['B','D'], 'B': ['A','D','C'], 'C': ['B'], 'D':['A','B'],'E':[]})

    """test-id: G1"""
    def test_get_adjlist_g1(self):
        assert self.g1.get_adjlist('A') == ['B','D'], "Test-id: G1. Node A connects B and D, so it should return ['B','D']"
        assert self.g1.get_adjlist('E') == [], "Test-id: g1. Node E contains nothing, and it should return []"
        assert self.g1.get_adjlist('Z') == None, "Test-id: G1. Node Z is not in the graph, so it should return None"
    """test-id: G2"""
    def test_is_adjacent_g2(self):
        assert self.g1.is_adjacent('B','C')== True,"Test-id: G2. Node B and C are connected, and it should return true"
        assert self.g1.is_adjacent('B','E')== False,"Test-id: G2. Node B and E are not connected, and it should return false"
        assert self.g1.is_adjacent('F','B')== False,"Test-id: G2. F is not in the graph, and it should return true"

    """test-id: G3 """
    def test_num_nodes_g3(self):
        assert self.g1.num_nodes()== 5, "Test-id: G3. Total nodes in the graph are 5, and it should return 5"

    """test-id: G4"""
    def test___contains___g4(self):
        assert self.g1.__contains__('A') == True, "Test-id: G4. It should return true since A is in the graph"
        assert self.g1.__contains__('Z') == False, "Test-id: G4. It should return false since Z is not in the graph"

    """test-id: G5 """
    def test_len_g5(self):
        assert len(self.g1)== 5, "Test-id: G5. The length should be the number of nodes, which is 5"

    """test-id: G6 """
    def test_add_node_g6(self):
        assert self.g1.add_node('F') == True, "Test-id: G6. It should return true because F is not in the graph"
        assert self.g1.add_node('A') == False, "Test-id: G6. It should return false because A is in the graph"

    """test-id: G7"""
    def test_link_nodes_g7(self):
        assert self.g1.link_nodes('A','E') == True, "Test-id: G7. It should return true if A and E are connected"
        assert self.g1.link_nodes('A','B') == False, "Test-id: G7. Since A and B are already connected, it should return false"
        assert self.g1.link_nodes('A','Z') == False, "Test-id: G7. It should return false because Z is not in the graph"
        assert self.g1.link_nodes('A','A') == False, "Test-id: G7. It should return false because two nodes are the same"
        assert self.g1.link_nodes('H','Z') == False, "Test-id: G7. It should return false because nodes are not in the graph"
    """test-id: G8"""
    def test_unlink_nodes_g8(self):
        assert self.g1.unlink_nodes('A','C') == False, "Test-id: G8. It should return false since two nodes are initially not connected"
        assert self.g1.unlink_nodes('A','B') == True, "Test-id: G8. It should return true after two nodes are not unlinked"
        assert self.g1.unlink_nodes('A','F') == False, "Test-id: G8. It should return false since node F is not in the graph"
        assert self.g1.unlink_nodes('Z','F') == False, "Test-id: G8. It should return false since two nodes are not in the graph"

    """ test-id: G9"""
    def test_del_node_g9(self):
        assert self.g1.del_node('C') == True, "Test-id: G9. It should return true if node C is successfully removed"
        assert self.g1.del_node('Z') == False, "Test-id: G9. It should return false since node Z is not in the graph"







