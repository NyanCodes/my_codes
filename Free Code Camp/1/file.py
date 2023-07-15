import csv

employee_file = open("employees.csv", "a+")

employee_file.write("\nKelly,Customer Service")

for employee in employee_file.readlines()[1:]:
   print(employee)

employee_file.close()