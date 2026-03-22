"""
module to parse a linked list from a string
"""
from node import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    """
    parses a linked list from a string
    """
    values = list_repr.split(" -> ")[:-1]
    probe = None
    for i in reversed(values):
        probe = Node(int(i), probe)
    return probe
