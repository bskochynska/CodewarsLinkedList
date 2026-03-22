"""
module to move nodes
"""
class Context(object):
    """
    class to store source and dest
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    changes dest's head to source's head and removes source's head
    """
    if source is None:
        raise ValueError
    new_head = source
    source = source.next
    new_head.next = dest
    return Context(source, new_head)
