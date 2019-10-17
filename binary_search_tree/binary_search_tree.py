import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE
        # if element == target
        if self.value == target:
            # return true
            return True
        # LEFT CASE
        # if target < element
        if target < self.value:
            if not self.left:
                return False
            # return left.contains(target)
            return self.left.contains(target)
        # RIGHT CASE
        # else 
        else:
            if not self.right:
                return False
            # return right.contains(target)
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # go to right until there is no more elements
        if self.right:
            return self.right.get_max()
        # return the last element
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        values = []
        append_to_values = lambda value : values.append(value)
        self.for_each(append_to_values)
        values.sort()
        for value in values:
            print(str(value))

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue data structure
        queue = Queue()
        # push the starting node on to the queue
        queue.enqueue(node)
        # loop while the queue has data
        while queue.len() > 0:
            # dequeue the current it em off the queue
            current = queue.dequeue()
            # print the current value
            print(str(current.value))
            # if the current node has a left child
            if current.left:
                # enqueue the left child on to the queue
                queue.enqueue(current.left)
            # if the current node has a right child
            if current.right:
                # enqueue right child on to the queue 
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # use a stack data structure
        stack = Stack()
        # push the starting node on to the stack
        stack.push(node)
        # loop while the stack has data
        while stack.len() > 0:
            # pop the current it em off the stack
            current = stack.pop()
            # print the current value
            print(str(current.value))
            # if the current node has a left child
            if current.left:
                # push the left child on to the stack
                stack.push(current.left)
            # if the current node has a right child
            if current.right:
                # push right child on to the stack          
                stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
