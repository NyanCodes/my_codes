import random

# Choose Sr lote mal and Netflix kyi mal
# if random number is odd, sr lote mal
# else netflix kyi mal

def checkNumber(num):
    if(num % 2 == 0):
        print("Neflix kyi mal")
    else:
        num += 1
        checkNumber(num)

print(random.random())

