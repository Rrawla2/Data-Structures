import sys
sys.path.append('../queue2')
sys.path.append('../stack')
from queue2 import Queue
from stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            return None
        # RECURSIVE
        if value < self.value:  # if value is less than self.value
            if self.left is None:  # if left child is None
                self.left = BSTNode(value)  # insert here - create new BSTnode
            else:
                self.left.insert(value)  # recursive call

        elif value >= self.value:  # - duplicate values go right
            if self.right is None:  # if right child is None
                self.right = BSTNode(value)  # insert here
            else:
                self.right.insert(value)  # recursive call
    # ************************************************************
        # ITERATIVE
        # while not at bottom level of tree

        # is it less than or equal to the root - duplicate values go right
            # if left child is None
                # add here
                # exit loop
        # is it greater than or equal to the root - duplicate values go right
            # if right child is None
                # add node here
                # exit loop

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value is None:
            return None
        if self.value == target:  # check if self.value is target
            return True  # if yes, return True
        # if no,
        elif target < self.value:  # go left
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target >= self.value:  # go right
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return None
        # Go right until you can't go right anymore - you get back the biggest value
        # while loop - while self.value is not next right node
        while not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # RECURSIVE
        # check one side and then check the other
        fn(self.value)  # call function fn on each node
        if self.right:  # go right
            self.right.for_each(fn)  # call function when it's the right side
        if self.left:  # go left
            self.left.for_each(fn)  # call function when it's the left side

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        my_queue = Queue()  # Create a new Queue
        my_queue.enqueue(self)  # add passed node to the new Queue

        while len(my_queue) > 0:  # check if the queue is not empty
            current_node = my_queue.dequeue()  # set node_value to next item in the list
            print(current_node.value)  # print the node_value

            if current_node.left:
                my_queue.enqueue(current_node.left)
            if current_node.right:
                my_queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        my_stack = Stack()  # create a stack to keep track of nodes we are processing
        my_stack.push(self)  # push `self` into the stack
        # while something still in the stack(not done processing all nodes)
        while len(my_stack) > 0:
            # push when we START, pop when a node is DONE
            current_node = my_stack.pop()
            print(current_node.value)  # call `print()`

            if current_node.left:
                my_stack.push(current_node.left)
            if current_node.right:
                my_stack.push(current_node.right)
            # use existing `for_each()` as a reference for the traversal logic

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
print("in order")
bst.in_order_print()
# print("post order")
# bst.post_order_dft()
