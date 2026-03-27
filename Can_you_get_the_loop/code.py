"""
module to calculate loop size
"""
def loop_size(node):
    """
    function to calculate loop size
    """
    length = 1
    slow = node
    fast = node.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    fast = fast.next
    while fast != slow:
        fast = fast.next
        length += 1
    return length
