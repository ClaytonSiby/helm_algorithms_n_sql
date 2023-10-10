# Python and SQL
Algorithms and data structures for Helm, also include some SQL scripts.

**Problem Statements (Implement the following)**

1. <h4>Python Challenge 1: (Repeating Playlist)</h4>

<h6>
  A playlist is considered a repeating playlist if any of the songs contain a reference to (i.e points to) a previous song in the playlist. Otherwise, the playlist will end with the last song which points to None.
</h6>

- Implement a function `is_repeating_playlist` that, efficiently with respect to time used, returns true if a playlist is repeating or false if it is not.

**Example: (the following code prints "True" as both songs point to each other):**

```
first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)

print(first.is_repeating_playlist()) # True
print(second.is_repeating_playlist()) # True
```

2. <h4>Python Challenge 1: (Repeating Playlist)</h4>

<h6>
  A Binary search tree (BST) is a binary tree where the value of each node is larger or equal to the values in all the node in that node's left subtree and is smaller than the values in all the nodes in that node's right subtree.
</h6>

- Write a function `def contains(node, value)` that, efficiently with respect to time used, checks if a give binary search tree with root `node` contains the given value.

**Example:**

```
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3)) # true
print(contains(n2, 5)) # false
```

**Requirements**
- Python
- Pytest
- Pip
- Git

**Setup Instructions**

<h6>From your terminal run: </h6>

- `git clone https://github.com/ClaytonSiby/helm_algorithms_n_sql.git` <br />
- `cd helm_algorithms_n_sql` <br />
- `python3 -m venv .venv` <br />
- `source .venv/bin/activate` <br />
- `pip install -r requirements.txt` <br />
- `pytest` <br />

**Project Structure**

- all the algorithms are in `/algorithms` directory
- all the tests are defined in `/tests`

- **NB** make sure your virtual environment is well set and is activated, please refer to the setup instrucitons above
