
dlugosc = int(input ('Podaj dlugosc miarki: '))
miarka = '|'
for i in range (dlugosc):
    miarka += '....|'
miarka += '\n'

for i in range (dlugosc):
    miarka += str(i)
    for j in range (5 - len(str (i+1))):
        miarka += ' '

miarka += str(dlugosc)
print(miarka)