# Dictionary: Key-Value Paris, Unorderd, Mutable

myDict = {
    "Name": "May", 
    "Age": 29,
    "City": "New York"
}

myDict2 = {
    "Name" : "Mary",
    'Age' : 19,
    'Email' : 'mary193@gmail.com'
}

myDict.update(myDict2)
print(myDict)

myDict3 = dict(name = "Nyan", city = "Rangoon")
 
print(myDict)

myDict['Age'] = 18
print(myDict["Age"]) # 18

value = myDict['Name'] 
print(value)

try:
    print(myDict["Last Name"])
except:
    print("Error")

for key in myDict.keys():
    print(key)

for values in myDict.values():
    print(values)

for key, value in myDict.items():
    print(key, value)
