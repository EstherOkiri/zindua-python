n = 5
while n > 0:
    print(n)
    n = n-1
print('Blastoff!')
print(n)

#infinite loop no iteration variable
#n = 5
#while n > 0:
  #  print('Lather')
 #   print ('Rinse')
#print ('Dry off!')



n = 0
while n > 0:
    print('Lather')
    print ('Rinse')
print('Dry off!')

#breaking out of an infinite loop
#break

while True :
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

#continue

while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')