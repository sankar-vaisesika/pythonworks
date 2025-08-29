class Node:                                                         

    def __init__(self,data=None,next=None):         #a node has a data and next(pointer)
    
        self.data=data
    
        self.next=next                              #Points to the next node

class LinkedList:                                   #this class manages list

    def __init__(self):                            

        self.head=None                              #start with an empty list also head is starting of the list 

    def append(self,data):

        new_node=Node(data)                         #assinging initial node with data

        if self.head is None:                       #if the list is empty:

            self.head=new_node                      #then newly assigned node is starting node and head is pointed to this node

            return
        
        last=self.head                              # then asigned head to last variable

        while last.next:                            #if there is next then iterate to next

            last=last.next      

        last.next=new_node                          #last node kazhinju ayirikkum adutha node assign cheyukka

    def display(self):

        current=self.head                           #display cheyan head node il ninnu thudaghum

        while current:                              #node indenghil loopinakathulath work cheyum allel none print avum
            
            print(current.data,end=" ->")

            current=current.next

        print("None")


l1=LinkedList()

l1.append(40)
l1.append(20)

l1.display()

#or


# class Node:

#     def __init__(self,data=None,next=None):
        
#         self.data=data

#         self.next=next

# n1=Node(20)
# n2=Node(10)
# n3=Node(50)

# n1.next=n2
# n2.next=n3

# current=n1

# while current:

#     print(current.data,end="->")

#     if current.next is None:

#         print("None")

#         break

#     current=current.next
