import collections
from algorithms.contains import contains

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def test_contains():
    n1 = Node(value=1, left=None, right=None)
    n3 = Node(value=3, left=None, right=None)
    n2 = Node(value=2, left=n1, right=n3)

    assert contains(n2, 1) is True
    assert contains(n2, 2) is True
    assert contains(n2, 3) is True
    assert contains(n2, 4) is False

    n4 = Node(value=4, left=None, right=None)
    assert contains(n4, 1) is False
