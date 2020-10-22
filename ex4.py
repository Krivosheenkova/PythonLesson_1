# Ex. 4
pos_int = int((input('Enter positive integer: ')))
the_biggest = pos_int % 10
pos_int = pos_int // 10

while pos_int > 0:
    if pos_int % 10 > the_biggest:
        the_biggest = pos_int % 10
    pos_int = pos_int // 10

print(the_biggest)
