import random
import timeit
import matplotlib.pyplot as plt

#1.
class Node:
    def __init__(self, data, parent=None, left=None, right=None, balance_factor = 0):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance_factor = balance_factor  
    
    #2.
           
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
                print("Case #3: Not supported")
            else:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")

        else:
            if pivot.balance_factor > 0:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("Case #3: Not supported")
    return



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




