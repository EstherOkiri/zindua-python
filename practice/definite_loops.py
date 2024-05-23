for i in[5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year: ', friend)
print('Done!')


print('Before')
for thing in[9, 41, 12, 3, 74, 15] :
    print(thing)
print('After')

#finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

#counting in aloop
print('COUNTING IN A LOOP')
zork = 0
print('Before ', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)

print('SUMMING IN A LOOP')
zork1 = 0
print('Before ', zork1)
for thing in [9, 41, 12, 3, 74, 15] :
    zork1  = zork1 + thing
    print(zork1, thing)
print('After', zork1)
