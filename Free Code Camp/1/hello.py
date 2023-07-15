 #adj1 = input("Enter an adjective: ")
#txt = "You are a {}"
#print("You are a " + adj1 + " person")

from re import I


fruits = ["Orange", "Apple", "Durain", "Grape", "Blueberry"]
#print(fruits[1:3])

coordinates = (4, 5)

def say_hi():
    print("Hi")

def cube(num):
    return num** 3

say_hi()
print(cube(3))

is_male = False

if is_male:
    print("You are a male")
else:
    print("You are female")

i = 1
while i <= 10:
    #print(i)
    i += 1
