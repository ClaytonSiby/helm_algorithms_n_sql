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

3. <h4>SQL CHALLENGE 1</h4>

<h6>
  A table containing the students enrolled in a yearly course has incorrect data in records with ids between 20 and 100 (inclusive).
</h6>

```
  TABLE enrollments
  id INTEGER NOT NULL PRIMARY KEY
  year INTEGER NOT NULL
  studentId INTEGER NOT NULL
```

<ins>Write a query that updates the field (year) of every faulty record of 2015</ins>

4. <h4>SQL CHALLENT 2</h4>

<h6>
  App usage data are kept in the following table:
</h6>

```
  TABLE sessions
  id INTEGER PRIMARY KEY,
  userId INTEGER NOT NULL,
  duration DECIMAL NOT NULL
```

<ins>Write a query that selects userId and average session duration for each user who has more than one session.</ins>


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
- the sql stuff is in the `/sql` directory

- **NB** make sure your virtual environment is well set and is activated, please refer to the setup instrucitons above

- **IMPORTANT** please read through the SQL setup instructions included in the shared documents. Thank you!
