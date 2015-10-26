__author__ = 'ws2ta'

from graph import Graph
import sys

def is_complete(object):
    if isinstance(object, Graph):
        if object.num_nodes()==1 or object.num_nodes()==0:
            return True
        else:
            a = 0
            b = 0
            for i in object:
                for x in list(object.get_adjlist(i)):
                    if object.__contains__(x)==False:
                        return False
                a += len(object.get_adjlist(i))
            a /= len(object)
            b %= len(object)
            c = a + 1
            if c == len(object) and b==0:
                return True
            else:
                return False
    else:
        raise TypeError('This is a Graph object')
def sortItem(item):
    return item[1]

def notes_by_degree(object):
    if isinstance(object,Graph):
        result = []
        for i in object:
            x = (i, len(list(object.get_adjlist(i))))
            result.append(x)
        return sorted(result, key=sortItem, reverse=True)
    else:
        raise TypeError('This is not a Graph object')

