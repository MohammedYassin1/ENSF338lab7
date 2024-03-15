import random
import timeit
import matplotlib.pyplot as plt

#1.
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right  

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data, parent=self)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data, parent=self)
            else:
                self.right.insert(data)

    def search(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(data)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(data)

#2.

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def measure_balance(root, balance_list):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    balance = abs(left_height - right_height)
    balance_list.append(balance)
    # Measure balance for left and right subtrees
    measure_balance(root.left, balance_list)
    measure_balance(root.right, balance_list)

    return balance_list
    

#3.

numbers = list(range(1, 1001))

tasks = []
for _ in range(1000):
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
        root.insert(element)
    balance_list = []
    balance_list = measure_balance(root, balance_list)
    balance = max(balance_list)
    total_balance.append(balance)
    total_time = 0
    for elemetn in task:
        time = timeit.timeit(lambda: root.search(element), number=1)
        total_time += time
    average_time = total_time / 1000
    total_average_time.append(average_time)

#5.
    
plt.scatter(total_balance, total_average_time)

plt.xlabel('Balance')
plt.ylabel('Search Time')
plt.title('Balance vs Search Time')

plt.show()


        
    
