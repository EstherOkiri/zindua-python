def greet():
    print("Hello, Python!")

#call the function
greet()

#Class Task 1
def sum(num1, num2):
    result = num1 + num2
    print(result)

sum(670, 670)

#write a function that takes user input and checks whether it is even or odd

def is_even_odd(num):
    if num % 2 ==0:
        print(f"{num} is EVEN")
    else :
        print(f"{num} is ODD")

num = int(input("Enter a number : "))
is_even_odd(num)
    