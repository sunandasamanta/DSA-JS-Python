# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)

# # creating an object of the class
# p1 = Person("John", 25)
# p1.display()


class MyPC:
    def __init__(self, brand, model, processor, memory, display):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.memory = memory
        self.display = display

    def values(self):
        return (self.brand, self.model, self.processor, self.memory, self.display)


PC1 = MyPC('Apple', 'MacBook Pro', 'M2 Pro', '16GB', 'OLED QHD+')

PC1.values()