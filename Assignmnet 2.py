# 1. What is a variable in Python?
#assin a value to a name using the assignment operator '='
# 2. How do you create a variable with the value 10 in Python?
num = 10
# 3. What are the basic data types in Python?
# integer variable
age = 9000
 #float
height = 9.65
#String variable
name = "Johnson"
#Boolean variable
is_primeminister = False
#List variable
race_colors = ["white","black","yellow","brown","green"]
#dictionary variable
person_prof = {"name":"Johnson","age":9000,"is_primeminister":False}
# 4. How do you take input from the user in Python?
user_intput = input("What is the current prime minister in japan?: ")
print(user_intput)
# 5. What is a list in Python?
#リストとはデータを格納するために使用されるデータ型。「」を使用してリストを作成できる。turpleとの違いは可変オブジェクトであること。タプルで作成された内容は変更できない。
# 6. How do you create a list with the values 1, 2, and 3?
num_list = [1,2,3]
# 7. How do you access the first element of a list?
print(num_list[0])
# 8. What is a dictionary in Python?
#dictionaryは、順序付けられ、変更可能であるが、重複はできないコレクションである。
# 9. How do you create a dictionary with the key-value pairs "name": "Alice" and "age": 25?
my_dict = {"name": "Alice","age": 25}
# 10. What is a function in Python?
#funcitonとはブロック内のコードを実行できる。これは再利用することが可能であり、コードを整理し、読みやすくする特徴がある。
# 11. How do you define a function that takes two arguments and returns their sum?
def sum(a,b):
    return a + b
result = sum(6,6)
print(result)

# 12. What is a loop in Python?
# a loop is that repeat multiple times as long as conditions are match.
# 13. How do you write a for loop that prints the numbers from 1 to 5?
for i in range(1,6):
    print(i)
# 14. What is an if statement in Python?
#コード内で実行をするためにIfという条件を用いて使用される。
# 15. How do you write an if statement that prints "Hello" if a variable x is equal to 10?
def exe_hello(num):
    if num == 10:
        print("Hello")

result = exe_hello(10)
# 16. What is the difference between a list and a tuple in Python?
#リストとはデータを格納するために使用されるデータ型。「」を使用してリストを作成できる。turpleとの違いは可変オブジェクトであること。タプルで作成された内容は変更できない。
# 17. How do you handle exceptions in Python?
# 18. How do you read a file in Python?
# 19. What is a module in Python?
# 20. How do you import a module in Python?