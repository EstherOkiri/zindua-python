#Task
#Write a python program that stores firve numbers in a list and check for even numbers in the list

num_List = [5,10,17,25,3,40,28]
even_numbers = []
odd_numbers = []

for num in num_List:
    if num % 2 == 0 :
        even_numbers.append(num)
    else :
        odd_numbers.append(num)

print(num_List)
print(even_numbers)
print(odd_numbers)


#Dictionaries
person = {
    "name": "John Doe",
    "age": 23,
    "height": 1.67,
    "occupation": "Software Developer"
    "hobbies": ["Football", "Care Racing", "Horse Riding"],
    "books":{
        "fiction": "Book A",
        "crime": "Book B",
    }
}

print(person)
#accessing elements in a dictionary
print(person["name"])
