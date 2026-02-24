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





#MRO -Method Resolution Order
#multiple inheritance(diamond problem)
#interface- 3types
#abstraction
#polymorphism - 