x = int(input ('Podaj szerokosc siatki: '))
y = int(input ('Podaj wysokosc siatki: '))

siatka = '\n'
for i in range (y):
    for j in range (x):
        siatka += '+---'
    siatka += '+\n'
    for j in range (x):
        siatka += '|   '
    siatka += '|\n'
for i in range (x):
    siatka += '+---'
siatka += '+\n'
print (siatka)