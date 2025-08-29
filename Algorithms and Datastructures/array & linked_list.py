# Using Python list as Array
arr = [10, 20, 30, 40]

# Insert at head (index 0) → O(n)
arr.insert(0, 5)  
print("Insert at head:", arr)  # [5, 10, 20, 30, 40]

# Insert at tail → O(1) amortized
arr.append(50)  
print("Insert at tail:", arr)  # [5, 10, 20, 30, 40, 50]

# Delete at head (index 0) → O(n)
arr.pop(0)  
print("Delete at head:", arr)  # [10, 20, 30, 40, 50]

# Delete at tail → O(1)
arr.pop()  
print("Delete at tail:", arr)  # [10, 20, 30, 40]

###Linked List###############
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Keep tail pointer for O(1) tail insert

    # Insert at head -> O(1)
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    # Insert at tail -> O(1) using tail pointer
    def insert_tail(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:  # if list empty
            self.head = self.tail = new_node

    # Delete at head -> O(1)
    def delete_head(self):
        if self.head:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    # Delete at tail -> O(n) in singly linked list
    def delete_tail(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        self.tail = current

    # Print linked list
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)


# Usage
ll = LinkedList()
ll.insert_head(10)
ll.insert_head(5)
ll.insert_tail(20)
ll.display()  # [5, 10, 20]

ll.delete_head()
ll.display()  # [10, 20]

ll.delete_tail()
ll.display()  # [10]


