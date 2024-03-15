#1.
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right  

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        while current:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data, parent=current)
                    self.update_balances(current.left)
                    self.check_pivot(current.left)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data, parent=current)
                    self.update_balances(current.right)
                    self.check_pivot(current.right)
                    return
                current = current.right

    def check_pivot(self, node):
        if node.parent is None:
            print("Case #1: Pivot not detected")
            return

        if self.get_height(node.left) - self.get_height(node.right) > 1:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")

    def update_balances(self, node):
        while node:
            node.balance = self.get_height(node.left) - self.get_height(node.right)
            node = node.parent

    def get_height(self, node):
        if node is None:
            return -1
        return max(self.get_height(node.left), self.get_height(node.right)) + 1
