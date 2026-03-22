"""
module to get n-th node
"""

def get_nth(node, index):
    """
    gets n-th node
    """
    head = node
    probe = head
    count = 0
    while probe:
        if count == index:
            return probe
        count += 1
        probe = probe.next
    raise IndexError
