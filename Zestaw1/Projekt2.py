import sys

argv = sys.argv[1:]

def rozklad (liczba):
    rozk = ''
    i = 2
    while (liczba > 1):
        powt = 0
        while (liczba % i == 0):
            powt += 1
            liczba /= i
        if (powt == 1):
            rozk = rozk + '*' + str(i)
        elif (powt > 1):
            rozk = rozk + '*' + str(i) + '^' + str(powt)
        i += 1
    return rozk[1:]

for i in range (0, len(argv)):
    print (f'{int(argv[i])} = {rozklad(int(argv[i]))}')