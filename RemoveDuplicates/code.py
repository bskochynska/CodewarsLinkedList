"""
module to implement function that removes duplicates
"""
def remove_duplicates(head):
    """
    function that removes duplicates
    """
    probe = head
    values = set()
    prev = None
    while probe is not None:
        if probe.data in values:
            prev.next = probe.next
        else:
            values.add(probe.data)
            prev = probe
        probe = probe.next
    return head
