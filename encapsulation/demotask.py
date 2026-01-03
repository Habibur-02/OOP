class Animal:
    def speak(self):
        pass  

class Dog(Animal):
    def speak(self): 
        return "Bark"

class Cat(Animal):
    def speak(self):  # Override
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  
# Output: Bark, Meow
