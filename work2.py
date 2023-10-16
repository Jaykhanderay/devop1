from abc import ABC,abstractmethod
class product(ABC):
    def __init__(self,price):
        self.price=price
    def get_price(self):
        print(f"Price is {self.price}")
        
    @abstractmethod
    def display_details(self):
     pass
class Electronic(product):
    def __init__(self,product,price,brand,warranty):
        super().__init__(product,price)
        self.product=product
        self.brand=brand
        self.warranty=warranty
    
    def displaydetails(self):
        print(f"Product:{self.product}")
        print(f"Product:{self.price}")
        print(f"Product:{self.brand}")
        print(f"Product:{self.warranty}")

class Clothing(product):
    def __init__(self,price,brand,shirt,):
        super().__init__(price,brand,shirt)
        self.brand=brand
        self.shirt=shirt
    def displaydetails(self):
        print(f"Product:{self.brand}")
        print(f"Product:{self.shirt}")
        print(f"Product:{self.price}")        
class Books(product):
         def __init__(self,price,name,author,genre):
            super().__init__(self,price)
            self.author=author
            self.name=name
            self.genre=genre
            self.price=price
         def displaydetails(self):
          print(f"Product:{self.name}")
          print(f"Product:{self.price}")
          print(f"Product:{self.author}")
          print(f"Product:{self.genre}")
    
product=Electronic("lenvo",50000,"sony","3years")
print(product.display_details())
 




   
        
        
    