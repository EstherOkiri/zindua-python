friends = ['Joseph','Mary','Esther' ]

print(friends[1])

#mutable-you can change things unlike strings

lotto = [2,14,26,41,63]
print(lotto)
lotto[2] = 28
print(lotto)

#How long is a list? How many elements are in a specific list

print(f"List length : {len(lotto)}")

#range function

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year: ', friend)

#concatenating lists using +
a = [1,2,3,4]
b = [5,6,7,8]
c = a + b
print(c)

#list Slicing
d=c[1:3] #excludes index 0 and 3 items
print(d)

e=c[:3]#includes items from index 0 to 3 excluding item on index 3
print(e)

f = c[3:]#includes items from index 3 to the last index
print(f)

#building a list from scratch
stuff = list()
stuff.append('book')
stuff.append('chair')
stuff.append('table')

print(stuff)

#is something in a list
'bool' in stuff

#lists in order- sort
friends.sort()
stuff.sort()
print(friends)
print(stuff)
#strings and lists

abc = 'With three words'
stuff1 = abc.split()
print(stuff1[2])

line = 'firsr:second:third'
thing = line.split(':')
print(thing)

