import random
import math

# take 2 numbers

num1 =int(input("Key in a positive number: "))
num2 = int(input("Key in another positive number: "))
operator = input("Key in an operator: ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1/num2

print ("The result is: " ,result)

# generate a random number

random_num = random.randint(1,100)
print("The random number is ", random_num)

num3 = int(input("Enter the number whose square root you want to find "))
if num3 < 0:
    print("Error. Cannot calculate squareroot of a negative number")
else:
    square_root = math.sqrt(num3)

print(f"The square root of {num3} is { square_root} ")

