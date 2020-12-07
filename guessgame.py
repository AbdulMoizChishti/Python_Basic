import random
num=0
print("Welcome to Guessing game")

rv = random.randint(1, 21)

for i in range(1,6):
    num= int(input("Select number"))
    if num<rv:
        print("number is less than rv")
    elif num>rv:
         print("number is greater than rv")
    else:
        print("your ans is correct")
        break
    