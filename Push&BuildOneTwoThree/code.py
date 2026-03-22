"""
module for implementation of push and build one two three functions
"""
from node import Node

def push(head, data):
    """
    function to update head
    """
    next_node = head
    head = Node(data)
    head.next = next_node
    return head

def build_one_two_three():
    """
    function to build first three nodes
    """
    probe = None
    for i in range(3,0,-1):
        probe = push(probe, i)
    return probe
