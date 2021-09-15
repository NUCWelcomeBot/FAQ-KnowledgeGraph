from typing import List

from Models import TypeEnum


class Edge:
    def __init__(self):
        self.nodeA: Node = None
        self.nodeB: Node = None
        self.relation: str = ''
        pass

    def set_node_a(self, node):
        self.nodeA = node

    def set_node_b(self, node):
        self.nodeB = node


EdgeVector = List[Edge]


class Node(object):
    def __init__(self, answer: str, type: str):
        self.edges: EdgeVector = []
        self.type = type
        self.answer = answer
        pass

    def add_edge(self, edge: Edge):
        self.edges.append(edge)
