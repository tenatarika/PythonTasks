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
print(Foo.method())
