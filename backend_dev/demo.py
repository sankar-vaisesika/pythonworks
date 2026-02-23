class grandparent():
    def __init__(self):
        
        super().__init__()
        print("hai")

class parent(grandparent):
    def __init__(self):

        super().__init__()
        print("hello")
    
class child(parent):
    def __init__(self):
 
        super().__init__()
        print("bye")

p1=child()


class A():
    def __init__(self):
        super().__init__()
        return "hai"

class B(A):
    def __init__(self):
        super().__init__()
        return "hello"
    
class C(B):
    def __init__(self):
        super().__init__()
        return "Bye"
    
p1=C()
print(p1)


#MRO -Method Resolution Order
#multiple inheritance(diamond problem)
#interface- 3types
#abstraction
#polymorphism - 