def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))

input =  input('Enter a limit for fibonacci: ')

try:
    fibonacii_List = []
    limit = int(input)
    if(limit <= 0):
        print("Please enter a positive integer")
    else: 
        print('Fibonacci Sequce : ', end = '')
        for i in range (limit):
            fibonacii_List.append(recur_fibo(i))
        print(fibonacii_List)
except Exception as error:
    print(error)  
        

    