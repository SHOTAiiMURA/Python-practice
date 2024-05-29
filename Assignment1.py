# 1. What is Python?
# python is interpreter language. this is used for web developing, statics, machine learninng.
# 2. How do you print "Hello, World!" in Python?
print("Hello World")
# 3. How do you create a variable in Python? Provide an example.
a = 5
b = 'Mochimaker'
print(a, b)
# 4. What is the difference between a list and a tuple in Python?
#tuple is immutable object while list is mutable.
# 5. How do you write a comment in Python?
#
# 6. How do you get the length of a list in Python?
example_list = [1,2,3,4,5,6,7]
print(len(example_list))
# 7. How do you convert a string to an integer in Python?
# use int()
string_user_age = input("what is your age?: ")
int_user_age = int(string_user_age)
# 8. What is a function in Python, and how do you define one?
# the block code that can only run inside block.
#def assignment():
# 9. How do you check if a key exists in a dictionary?
my_dict={"task1":"learning python", "task2":"java"}
print(my_dict["task1"])
# 10. What is a loop, and how do you write a for loop in Python?
#loop is that repeats multiple times as long as condition is met
for i in range(10):
    if i % 2 == 0:
        print(i)
# 11. How do you handle exceptions in Python?
try:
    result = 10 / 0
except ZeroDivisionError:
    print("This is invalid number")
# 12. What is the difference between == and is in Python?
# equality operator
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True
#identity operator
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)  # Output: False
print(a is c)  # Output: True

# 13. How do you create a class in Python?
class myClass:
    x = 6

p1 = myClass()
print(p1.x)
# 14. What is a module in Python?
# a module to be the same as a code library.
# 15. How do you import a module in Python?

# 16. What is the purpose of the if __name__ == "__main__": statement?
# 3 pourpose of using the if__name__ == "__main__"
# to test
# to execute command line tool
# To allow the script to be both executable and importable without running the executable code on import.
# 17. How do you open a file in Python for reading?
# file_path = "example.txt"
#
# with open(file_path, "r") as file_object:
#     #read entire contents of file
#     entire_content = file_object.read()
#     print(entire_content)
# 18. What is a list comprehension in Python?
#条件に基づいて要素をフィルタリング、新しいリストを生成する。
# [expression for item in iterable if condtion]
# expression: 新しいリスト内の各要素が何になるかを定義する式。
# item: 反復可能オブジェクト内の各要素を表す変数。
# iterable: 反復処理する項目のコレクション (リスト、タプル、範囲など)。
# condition: (オプション) 式をアイテムに適用するかどうかを決定するフィルタリング条件。
squares = [i**2 for i in range(11)]
print(squares)
#if there are conditions
evens = [x for x in range(11) if x % 2 ==0]
print(evens)
# 19. How do you install a package using pip?
# 20. What is the use of the lambda function in Python?