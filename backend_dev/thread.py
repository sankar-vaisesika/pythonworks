# class called bank account .two thread acting on same bank account trying to update the bank balance. Try that thread should not block each other


class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
        A.show(self)

class C(A):
    def show(self):
        print("C")
        A.show(self)

class D(B,C):
    def show(self):
        print("D")
        super().show()

print(D.__mro__)
obj=D()
obj.show()



