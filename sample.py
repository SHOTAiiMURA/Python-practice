#1:
# the output is Hello world.
#2
list = [1,2,3,4,5]
#3
list.append(7)
#4.you can find out how many elements in the list.
print(len(list))
#5.
dict = {"child":10, "teenager":14,"adult":20}
#6
print(dict["child"])
#7
x = 5
y = 10
print(x + y)

#8
def return_squre(num):
    return num ** 2

try:
    result = 10 / 0
except ZeroDivisionError:
    print("this is invalid numnber")