class Car:
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color
    
    def start_engine(self):
        return f"{self.brand} {self.model} engine started!"

c1=Car("toyota",'innova',"red")
print(c1.start_engine())
