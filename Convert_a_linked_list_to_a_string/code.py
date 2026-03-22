"""
module to convert linked list to a string
"""
def stringify(node):
    """
    converts linked list to a string
    """
    result = ''
    head = node
    probe = head
    while probe is not None:
        result += f'{probe.data} -> '
        probe = probe.next
    result += 'None'
    return result
