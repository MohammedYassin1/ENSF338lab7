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

    root.balance(root)  
    return

def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None

def get_balances(root):
    if root is None:
        return []
    return [root.balance_factor] + get_balances(root.left) + get_balances(root.right)  # use 'balance_factor' instead of 'balance'



#3.


numbers = list(range(1, 1001))

tasks = []
for z in range(1000):
    random.shuffle(numbers)
    tasks.append(numbers.copy())

#4.
total_balance = []
total_average_time = []
counter = 0
for task in tasks:
    counter += 1
    print(counter)
    root = Node(task[0])
    balance = 0
    for element in task:
        insert(element, root)
    balance_list = get_balances(root)
    balance = max(balance_list)
    total_balance.append(balance)
    total_time = 0
    for e in task:
        time = timeit.timeit(lambda: search(e, root), number=1)
        total_time += time
    average_time = total_time / 1000
    total_average_time.append(average_time)

#5.
    
plt.scatter(total_balance, total_average_time)

plt.xlabel('Balance')
plt.ylabel('Search Time')
plt.title('Balance vs Search Time')

plt.show()



        
    
