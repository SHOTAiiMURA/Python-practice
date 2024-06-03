# What is Python and why is it popular?
    #python is oop programming language. python can be used in web develop, machine learning, data analyze. python is interpretetor language.
# How do you declare a variable in Python?
integer = 1
float = 3.5
string = "apple"

# What are the basic data types in Python?

# How do you create a list in Python? Provide an example.
my_list = [1,2,3,4,5,6,6,7,7,8,99]
print(my_list[0])
# What is a tuple and how is it different from a list?
    #turple cannot be changed whereas list is changeable.
    #tuple can be duplicated whereas list cannot be duplicated.
my_tuple = ("apple","cherry","orange")

# How do you create a dictionary in Python? Provide an example.
my_dict = {"name":"john ","age":"25","race":"asia"}
# What is a set in Python and how does it differ from a list?
    #sets are not changeable, duplicated, ordered.
sets_example = {"apple","banana",True,1,2}
for x in sets_example:
    print(x)
# How do you write a for loop in Python? Provide an example.
for i in range(1,6):
    print(i)
for integer in range(2,31,3):
    print(integer)
# How do you write a while loop in Python? Provide an example.
# What is the difference between break and continue in a loop?
    #break can stop the loop before it looped through all the items
fruits = ["apple","banana","cherry"]
for i in fruits:
    print(i)
    if i == "banana":
        break
for ii in fruits:
    if ii == "banana":
        continue
    print(ii)
    #we can stop the current iteration of the loop, and continue with the next.
# How do you define a function in Python? Provide an example.
def function():
    print("Hello mother fucker")

###Calling function
def function():
    print("Hello mother fucker")
function()
### argument
def my_func(name):
    print(name + " san")
my_func("Keita")
# What is the difference between *args and **kwargs in function definitions?

# What are list comprehensions and how do you use them? Provide an example.
    #[expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
print(squares)
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

def square(x):
    return x*x
numbers = [1,2,3,4,5,6]
squares = [square(x) for x in numbers]
print(squares)
# How do you handle exceptions in Python? Provide an example.

# What is the purpose of the if __name__ == "__main__": statement?
    #if __name__ == "__main__":
# How do you read from and write to a file in Python? Provide examples.
    ##open file
#file = open("testfile.txt")
#file = open("testfile.txt","rt")

# What are classes and objects in Python? Provide an example of a simple class.
    ### class and objects
class Personinfo:
    def __init__(self,name,age,fname,lname):
        self.name = name
        self.age = age
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
p1 = Personinfo("Bille",45,"shota","iimura")
print(p1.name)
print(p1.age)

# What is inheritance in Python and how do you use it? Provide an example.
class Student(Personinfo):
    pass
x = Student("asakura",45,"Shota","Iimura")
x.printname()

# What are decorators in Python and how do you use them? Provide an example.
# How do you use the lambda function in Python? Provide an example.
    #lambda argumnents:expression
x = lambda a: a + 10
print(x(5))

y = lambda a,b: a*b
print(y(5,6))

# What is the difference between == and is in Python?

# How do you convert a string to an integer in Python?
user_input = input("Enter a number: ")
try:
    num = int(user_input)
    print(f"The integer value is: {num}")
except ValueError:
    print("Invalid input! Please enter a valid integer")

