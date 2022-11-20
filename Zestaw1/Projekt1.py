

x = int(input('Podaj postawe trojkata: '))
y = 0
while (y < x):
    if y == 0:
        for i in range (x):
            print('*', end='')
        print('')
        y += 2
    else:
        for i in range (int(y/2)):
            print(' ', end='')
        print('*', end='')
        for i in range (x-2-y):
            print(' ', end='')
        if (x % 2 == 0 or (x-2-y) > 0): 
            print('*', end='')
        for i in range (int(y/2)):
            print(' ', end='')
        print ('')
        y += 2
