try: 
    answer = 10 / 2
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print("Invalid Error")