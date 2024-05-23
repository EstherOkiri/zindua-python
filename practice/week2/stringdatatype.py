str1 = 'Hello '
str2 = 'there'

bob = str1 + str2
print(bob)
fruit = 'banana'
letter = fruit[1]
print(letter)
print(len(fruit))

#loop through strings
index = 0

while index< len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#loop using a for loop
for letter in fruit:
    print(letter)

#looping and Counting
word = 'banana'
count = 0
for letter in word :
    if letter == 'a':
        count = count + 1
print(count)

#String Methods
print('Slicing')
s = 'Monty Python'
print(s[0:4])
print(s[6:7])

# Search a string
if 'n' in fruit :
    print(True)

a = 'Hello'
b = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)
#String Comparison
if word == 'banana':
    print('All right, bananas')
if word < 'banana' :
    print('Your word ' + word + ',comes before banana')
elif word > 'banana' :
    print('Your word ' + word + ',comes after banana')
else :
    print('All right, bananas')

#String Library
greet = 'Hello Esther'
zap = greet.lower()
print(zap)

#Search and Replace
nstr = greet.replace('Esther', 'Jane')
print(nstr)

#Stripping Whitespace
greet1 = '  Hello Esther'
greet1.strip() #strips space at the beginning and end of a string
print(greet1)





