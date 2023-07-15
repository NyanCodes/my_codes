#Lists: ordered, mutable, allows duplicate elements

myList = ['banana', 'cherry', 'apple']

if 'banana' in myList:
    print("True")
else: 
    print("False")

#copying list
list_cpy = myList.copy() 

a = [1, 2, 3, 4, 5, 6, 7]
b = [ i * i for i in a]

print(a)
print(b)