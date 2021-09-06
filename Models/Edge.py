from Models.Node import Node


class Edge:
    def __init__(self):
        self.nodeA: Node = Node()
        self.nodeB: Node = Node()
        self.relation: str = ''
        pass
