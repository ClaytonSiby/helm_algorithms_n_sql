
import collections
Node = collections.namedtuple('Node', ['value', 'left', 'right'])

def contains(node, value):
    if node is None:
        return False
    if node.value == value:
      return True
    if value < node.value:
        return contains(node.left, value)
    return contains(node.right, value)
