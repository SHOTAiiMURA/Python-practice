# 10. What is a loop, and how do you write a for loop in Python? 11. How do you handle exceptions in Python?
# 12. What is the difference between == and is in Python?
a = [1,2,3,4,5]
b=a
print(a==b)
print(a is b)

#its not same object to the memory
a = [1,2,3,4,5]
b = [1,2,3,4,5]
print(a is b)

# 13. How do you create a class in Python?
#base class: initialize the class.
class Animal:
    def __init__ (self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass msut implement this methods")
class Human:
    def __init__ (self,name):
        self.name = name
    def greeting(self):
        raise NotImplementedError("Subclass must implement this methods")
#subclass
#Derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

dog = Dog("Buddy")
cat = Cat("Tama")

class Japanese(Human):
    def greeting(self):
        return f"{self.name} says Mochimaker"
class India(Human):
    def greeting(self):
        return f"{self.name} says Villager"

japanese = Japanese("Naruto")
india = India("Chikin curry")

if __name__ == "__main__":
    print(dog.speak())
    print(cat.speak())
    print(japanese.greeting())
    print(india.greeting())
# 14. What is a module in Python?
import math
print(math.sqrt(16))
# 15. How do you import a module in Python?
# 16. What is the purpose of the if __name__ == "__main__": statement? 17. How do you open a file in Python for reading?
# 18. What is a list comprehension in Python?
# 19. How do you install a package using pip?
# 20. What is the use of the lambda function in Python?