# Write a Program in Python to Find the Smallest and the Largest List Elements on Inputs Provided by the User

fruits = list()
num = int(input('How many fruits do you want to include in the list? '))

for x in range(num):
    fruit = input("Enter Fruit name : ")
    fruits.append(fruit)

print(fruits)

# Write a Python Program to Split a List in Half and Store the Elements in Two Different Lists
#using slicing method
complete = [1,2,3,4,5,6,7,8,9,10]
first_half = complete[:5]
second_half = complete[5:]

print(first_half)
print(second_half)

#Write a Python Program to Remove Multiple Empty Strings From a List of Strings

