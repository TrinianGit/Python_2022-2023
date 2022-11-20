x = int(input('Wpisz x: ')) + 1
y = int(input('Wpisz y: ')) + 1
z = int(input('Wpisz z: ')) + 1
n = int(input('Wpisz n: '))

wynik = [ [i, j, k] for i in range (x) for j in range (y) for k in range (z) if i+j+k != n]

print (wynik)