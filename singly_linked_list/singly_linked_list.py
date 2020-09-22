class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next

# Head, Tail and None are special nodes in the linked list
# You will always need a head, you should also have a tail


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def output_list(self):
        current_node = self.head
        if current_node is None:
            print("List is empty")
        while current_node is not None:
            print(current_node.get_value())
            current_node = current_node.get_next_node()
        return

    def add_to_head(self, value): # order is important here.  Don't update until last.
        new_node = Node(value)
        if self.head is None:
             #update head and tail attributes
            self.head = new_node # if a linked list has 1 element it's the head and also the tail.
            self.tail = new_node
        else:
            # set next_node of the new Node to the head
            new_node.set_next_node(self.head)
            # update the head attribute
            self.head = new_node # self refers to the head of this linked list

    def add_to_tail(self, value):
        # create a new Node
        new_node = Node(value)
        # 1. LL is empty
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node

        # 2. LL is not empty
        else:
            # update next_node of our tail
            self.tail.set_next_node(new_node)
            # update self.tail
            self.tail = new_node

    def remove_head(self):
        # cases to consider?
        # empty list
        if self.head is None:
            return None
        # else, return VALUE of the old head
        else:
            ret_value = self.head.get_value()
            # list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                # list with 2+ elements
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # empty list?
        if self.head is None:
            return None

        current = self.head

        if self.head is self.tail:
            ret_value = self.head.get_value()
            self.head = None
            self.tail = None
            return ret_value

        # traverse from head to tail(go through the list from start to finish)
        # use a while loop to find the tail
        while current.get_next_node() is not self.tail:
            # set current to the next node in the list
            current = current.get_next_node()

        # How do we get rid of the node? We set the current node pointer to None
        ret_value = self.tail.get_value()
        self.tail = current
        self.tail.set_next_node(None)
        return ret_value

    def contains(self, value):
        # loop through the linked list until we find the value OR the next pointer is None
        current_node = self.head
        while current_node is not None:
            # if we find 'value'
            if current_node.get_value() == value:
                print("The list contains the value")
                return True
            current_node = current_node.get_next_node()
        print("The list does not contain the value")
        return False

    def get_max(self):
        # check for empty list
        if self.head is None:
            return None

        # Returns the max value in the linked list
        # set current_node to the head
        # initialize variable to head value for comparison
        current_node = self.head
        max_value = self.head.get_value()

        # traverse the list while the list is not empty
        # if the current node value is greater than the current max value
        # set the current node value as the new max value
        # go to the next node value and compare to the current max value
        # when all node values have been checked - return the max value
        while current_node is not None:
            if current_node.get_value() > max_value:
                max_value = current_node.get_value()
            current_node = current_node.get_next_node()
        return max_value

# *** Tests for get_max and contains ***
new_list = LinkedList()
new_list.add_to_head(5)
new_list.add_to_head(8)
new_list.add_to_head(50)
new_list.add_to_head(1)
new_list.contains(8)
new_list.contains(10)
print("The max value is: ", new_list.get_max())