# Exercise 4

class Node:
    def __init__(self, data, parent=None, left=None, right=None, balance_factor=0):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance_factor = balance_factor

    def height(self, node):
        if node is None:
            return -1
        return max(self.height(node.left), self.height(node.right)) + 1

    def balance(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        node.balance_factor = left_height - right_height

        # Recursively update balance for left and right subtrees
        self.balance(node.left)
        self.balance(node.right)

    def get_pivot(self, node):
        if node is None:
            return None

        if abs(node.balance_factor) > 1:
            return node

        return self.get_pivot(node.parent)

    def _right_rotate(self, node):
        """
        Perform a right rotation on the given node.
        """
        if node is None or node.left is None:
            return

        pivot = node.left
        node.left = pivot.right
        if pivot.right is not None:
            pivot.right.parent = node

        pivot.parent = node.parent
        if node.parent is None:
            self = pivot
        elif node == node.parent.right:
            node.parent.right = pivot
        else:
            node.parent.left = pivot

        pivot.right = node
        node.parent = pivot

        # Update balance factors
        self.balance(node)
        self.balance(pivot)

        return pivot

    def _left_rotate(self, node):
        """
        Perform a left rotation on the given node.
        """
        if node is None or node.right is None:
            return

        pivot = node.right
        node.right = pivot.left
        if pivot.left is not None:
            pivot.left.parent = node

        pivot.parent = node.parent
        if node.parent is None:
            self = pivot
        elif node == node.parent.left:
            node.parent.left = pivot
        else:
            node.parent.right = pivot

        pivot.left = node
        node.parent = pivot

        # Update balance factors
        self.balance(node)
        self.balance(pivot)

        return pivot

    def _lr_rotate(self, node):
        """
        Perform an LR rotation on the given node.
        """
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def _rl_rotate(self, node):
        """
        Perform an RL rotation on the given node.
        """
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)


def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    newnode = Node(data, parent)
    if root is None:
        root = newnode
    elif data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    old_balance = root.balance_factor
    root.balance(root)
    pivot = root.get_pivot(newnode)

    if pivot is None:
        print("Case #1: Pivot not detected")
    else:
        if newnode.data < pivot.data:
            if pivot.balance_factor > 0:
                if newnode.data > pivot.left.data:
                    print("Case #3b: adding a node to an outside subtree")
                    pivot = root._lr_rotate(pivot)
                else:
                    print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                if newnode.data < pivot.left.data:
                    print("Case #3a: adding a node to an outside subtree")
                    pivot = root._right_rotate(pivot)
                else:
                    print("Case #2: A pivot exists, and a node was added to the shorter subtree")
        else:
            if pivot.balance_factor > 0:
                if newnode.data < pivot.right.data:
                    print("Case #3a: adding a node to an outside subtree")
                    pivot = root._left_rotate(pivot)
                else:
                    print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                if newnode.data > pivot.right.data:
                    print("Case #3b: adding a node to an outside subtree")
                    pivot = root._rl_rotate(pivot)
                else:
                    print("Case #2: A pivot exists, and a node was added to the shorter subtree")

    return root


# Test cases
# Test case 1: Adding a node results in case 1
root = Node(10)
insert(5, root)

# Test case 2: Adding a node results in case 2 
root = Node(10)
insert(15, root)
insert(20, root)
insert(25, root)
insert(5, root)

# Test case 3: Adding a node results in case 3
root = Node(10)
insert(5, root)
insert(4, root)

# Test case 4: Adding a node results in case 3a
root = Node(10)
insert(5, root)
insert(3, root)
insert(4, root)

# Test case 5: Adding a node results in case 3b
root = Node(10)
insert(5, root)
insert(15, root)
insert(7, root)

# Additional test cases for case 3b
# Test case 6: Adding a node results in case 3b
root = Node(10)
insert(5, root)
insert(15, root)
insert(12, root)
