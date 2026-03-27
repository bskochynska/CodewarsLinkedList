"""
module for altering split
"""
class Node(object):
    """
    class to initialize Node
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """
    class to store result
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    method for alternating split
    """
    if head is None or head.next is None:
        raise ValueError
    first = head
    second = head.next
    current_first = first
    current_second = second
    while current_second is not None and current_second.next is not None:
        current_first.next = current_second.next
        current_first = current_first.next
        current_second.next = current_first.next
        current_second = current_second.next
    current_first.next = None
    return Context(first, second)
