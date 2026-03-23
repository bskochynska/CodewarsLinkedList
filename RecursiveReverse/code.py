"""
module to reverse linked list using recursion
"""

def reverse(head):
    """
    function to reverse linked list using recursion
    """
    def _reverse_helper(current, prev):
        if current is None:
            return prev
        temp = current.next
        current.next = prev
        return _reverse_helper(temp, current)
    return _reverse_helper(head, None)
