# Ex. 6
a = int(input('Enter ur current result: '))
b = int(input('What result do you dream of: '))
day = 1
while a < b:
    a = a + a * 0.1
    day = day + 1

print('You will reach the desired result in: ', day, 'days')
