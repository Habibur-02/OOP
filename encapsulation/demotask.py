class Animal:
    def speak(self):
        pass  # Generic method

class Dog(Animal):
    def speak(self):  # Override
        return "Bark"

class Cat(Animal):
    def speak(self):  # Override
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Each object behaves differently
# Output: Bark, Meow