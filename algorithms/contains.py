def contains(node, value):
    """
    :return : (bool) True if the node contains the value, False otherwise
    """
    if node is None:
        return False
    if node.value == value:
      return True
    if value < node.value:
        return contains(node.left, value)
    return contains(node.right, value)
