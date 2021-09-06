from typing import List

from Models import TypeEnum
from Models.Edge import Edge

EdgeVector = List[Edge]


class Node(object):
    def __init__(self):
        self.edges: EdgeVector = []
        self.type = None
        self.answer = None
        pass
