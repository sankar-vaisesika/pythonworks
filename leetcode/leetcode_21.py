class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def mergeTwoLists(self, l1, l2):
        dummy = Node()
        tail = dummy

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy  # skip dummy node and return merged head

# Helper function to create a linked list from Python list
def create_linked_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for value in lst[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Test:
l1 = create_linked_list([1, 2, 3])
l2 = create_linked_list([1, 2, 4])

merged = LinkedList().mergeTwoLists(l1, l2)
print_linked_list(merged)
