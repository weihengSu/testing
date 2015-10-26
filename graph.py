__author__ = 'weiheng su'
import sys

class Graph(object):
    def __init__(self, dict= {}):
        self.data = dict
    def get_adjlist(self, node):
        if node in self.data.keys():
            nodes = self.data[node]
            return nodes
        else:
            return None
    def is_adjacent(self, node1, node2):
        if node1 in self.data.keys():

            if node2 in list(self.data[node1]):
                return True
            else:
                return False
        else:
            return False
    def num_nodes(self):
        return len(list(self.data.keys()))
    def __str__(self):
        result = "{"
        for k,v in sorted(self.data.items()):
            a = "'"+str(k)+"': "+str(v)+ " "
            result += a
        result +="}"
        return result
    def __iter__(self):
        for i in self.data:
            yield i
    def __contains__(self, node):
        if node in self.data.keys():
            return True
        else:
            return False
    def __len__(self):
        return self.num_nodes()
    def add_node(self, node):
        if node not in self.data:
            self.data[node] = []
            return True
        else:
            return False
    def link_nodes(self, node1, node2):
        if node1 in self.data.keys() and node2 in self.data.keys():
            if node1!= node2:
                if self.is_adjacent(node1,node2) == False:
                    self.data[node1].append(node2)
                    self.data[node2].append(node1)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def unlink_nodes(self, node1, node2):
        if node1 in self.data.keys() and node2 in self.data.keys():
            if self.is_adjacent(node1, node2) == True:
                del self.data[node1][self.data[node1].index(node2)]
                del self.data[node2][self.data[node2].index(node1)]
                return True
            else:
                return False
        else:
            return False
    def del_node(self, node):
        if node in self.data.keys():
            del self.data[node]
            for i in self.data.keys():
                if node in self.data[i]:
                    del self.data[i][self.data[i].index(node)]

            return True
        else:
            return False






