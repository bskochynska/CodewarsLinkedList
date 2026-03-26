"""
module to swap pairs of nodes
"""

def swap_pairs(head):
    """
    function to swap pairs
    """
    probe = head
    prev = None
    while probe is not None and probe.next is not None:
        next_probe = probe.next
        next_pair = next_probe.next
        probe.next = next_pair
        next_probe.next = probe
        if prev is None:
            head = next_probe
        else:
            prev.next = next_probe
        prev = probe
