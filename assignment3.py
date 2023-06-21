# MCIS5313_029211S: Data Structures and Algorithms, Assignment#3: Linked List

# A linked list is an object that creates, references and manipulates node objects. In
# this assignment, you are asked to write a Python program to create a linked list
# and do a set of operations as follows:

# 1. Create an empty linked list
# 2. Create and insert a new node at the front of the linked list
# 3. Insert a new node at the back of the linked list
# 4. Insert a new node at a specified position in the linked list
# 5. Get a copy of the data in the node at the front of the linked list
# 6. Get a copy of the data in the node at a specified position in the linked list
# 7. Remove the node at the front of the linked list
# 8. Remove the node at the back of the linked list
# 9. Remove the node at a specified position in the linked list
# 10.Traverse the list to display all the data in the nodes of the linked list
# 11.Check whether the linked list is empty
# 12.Check whether the linked list is full
# 13.Find a node of the linked list that contains a specified data item

# These operations can be implemented as methods in a class you can name:
# LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
      
    # check whether linked list is empty
    def is_empty(self):
        return self.head is None

    # create and insert a new node at the front of the linked list
    def create_and_insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # insert a new node at the back of the linked list
    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # insert a new node at a specified position in the linked list
    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Invalid position")
        if position == 0:
            self.create_and_insert_front(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Invalid position")
                current = current.next
            if current is None:
                raise IndexError("Invalid position")
            new_node.next = current.next
            current.next = new_node

     # get a copy of the data in the node at the front of the linked list
    def get_front_data(self):
        if self.head is None:
            raise IndexError("Linked list is empty")
        return self.head.data

    # get a copy of the data in the node at a specified position in the linked list 
    def get_data_at_position(self, position):
        if self.head is None:
            raise IndexError("Linked list is empty")
        current = self.head
        for _ in range(position):
            if current is None:
                raise IndexError("Invalid position")
            current = current.next
        if current is None:
            raise IndexError("Invalid position")
        return current.data

    # remove the node at the front of the linked list
    def remove_front(self):
        if self.head is None:
            raise IndexError("Linked list is empty")
        self.head = self.head.next

    # remove the node at the back of the linked list
    def remove_back(self):
        if self.head is None:
            raise IndexError("Linked list is empty")
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None

    # remove the node at a specified position in the linked list
    def remove_at_position(self, position):
        if self.head is None:
            raise IndexError("Linked list is empty")
        if position == 0:
            self.remove_front()
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError("Invalid position")
                current = current.next
            if current.next is None:
                raise IndexError("Invalid position")
            current.next = current.next.next

    # traverse the list to display all the data in the nodes of the linked list
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    # find a node of the linked list that contains a specified data item
    def find_node_with_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False


# Example usage of the LinkedList class

# Create an empty linked list
my_list = LinkedList()

# Insert nodes
my_list.create_and_insert_front(3)
my_list.insert_back(5)
my_list.insert_at_position(7, 1)

# Get data from nodes
print(my_list.get_front_data())  # Output: 3
print(my_list.get_data_at_position(1))  # Output: 7

# Remove nodes
my_list.remove_front()