import csv

data = "Toby,HR"
#with open('employees.csv', 'a+') as file:
#    file.write(data) 
with open('employees.csv', 'r') as file:
    print( file.read() ) 