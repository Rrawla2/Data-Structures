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
        # RECURSIVE
        if value < self.value:  # if value is less than self.value
            if self.left is None:  # if left child is None
                self.left.insert(BSTNode(value))  # insert here - create new_BSTnode
            else:
                self.left.insert(value)  # recursive call

        if value >= self.value:  # - duplicate values go right
            if self.right is None: # if right child is None
                self.right.insert(BSTNode(value))  # insert here
            else:
                self.right.insert(value)  # self.right.insert(value) # recursive call
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
        # check if self.value is target
            # if yes, return True
            # if no,
                # go left?
                # go right?
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until you can't go right anymore - you get back the biggest value
        # while loop - while current_value is > next value
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # RECURSIVE
        # check one side and then check the other
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

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
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
