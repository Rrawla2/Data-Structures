"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self.prev = prev_node
        self.value = value
        self.next = next_node

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:  # self is the current head here
            # next_node = self.next - set next_node to the node after the head
            # next_node.prev = self.prev - set next_node to prev of the head which should be None
            # self.prev is None - previous node of the Head
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new_node
        new_node = ListNode(value)
        # adding to an empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # adding to a non-empty list
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # since we added something - update the length by +1
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        head_value = self.head.value
        self.delete(self.head)
        return head_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create a new_node
        new_node = ListNode(value)
        # adding to an empty list
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        # adding to a non-empty list
        else:
            new_node.prev = self.head
            self.tail.next = new_node
            self.tail = new_node
        # since we added something - update the length by -1
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        old_value = node.value
        # 1. delete
        self.delete(node)
        # 2. add_to_head
        self.add_to_head(old_value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        old_value = node.value  # save the current value to return
        # 1. delete the node
        self.delete(node)
        # 2. use add_to_tail
        self.add_to_tail(old_value)  # return the value

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # We don't need to return any value = list is empty
        if self.head is None:
            return None
        # update the head and the tail = has only 1 element
        if self.head is self.tail and node is self.head:
            self.head = None
            self.tail = None
        # the node is the HEAD = update the head pointer
        elif node is self.head:  # list has 2 or more nodes
            self.head = node.next  # Don't forget to update the HEAD pointer
            node.delete()  # see delete function in the ListNode class as this updates the new pointers
        # the node is the TAIL = update the tail pointer
        elif node is self.tail:
            self.tail = node.prev  # Don't forget to update the TAIL pointer
            node.delete()  # see delete function in the ListNode class as this updates the new pointers
        # the node is any node in the list
        else:
            node.delete()  # see delete function in the ListNode class as this updates the new pointers
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current_node = self.head
        max_value = self.head.value

        # check for empty list
        if current_node is None:
            return None
        # traverse the list while the list is not empty
        # if the current node value is greater than the current max value
        # set the current node value as the new max value
        # go to the next node value and compare to the current max value
        # when all node values have been checked - return the max value
        while current_node is not None:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
