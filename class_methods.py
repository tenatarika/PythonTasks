class Foo:
    def method(self):
        return "вызван метод экземпляра", self
    
    
    @classmethod
    def class_method(cls):
        return "вызван метод классa", cls
    
    
    @staticmethod
    def static_method():
        return "вызван статический метод"
    
    
obj = Foo()
# объект
print(obj.method())
print(obj.class_method())
print(obj.static_method())

print(Foo.class_method())
print(Foo.static_method())
# print(Foo.method()) don't work  


class Book():
    def __init__(self, name : str, price : float, author : str) :
        self.name = name
        self.price = price
        self.author = author
        
    def __repr__(self) -> str:
        return "Book {self.name} by {self.author} for {self.price}"
    
    def cost_with_tax(self):
        return self.tax(self.price)
    
    @staticmethod
    def tax(price: int):
        return price*1.13