"""
module for node insertion sorting
"""
from node import Node

def sorted_insert(head, data):
    """
    fucntion to sort nodes by values when new node is added
    """
    if head is None or data <= head.data:
        new_node = Node(data)
        new_node.next = head
        return new_node
    current_node = Node(data)
    probe = head
    while probe is not None:
        if probe.data <= current_node.data:
            if probe.next is None or current_node.data <= probe.next.data:
                current_node.next = probe.next
                probe.next = current_node
                break
        probe = probe.next
    return head
