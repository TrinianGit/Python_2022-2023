dane = input ('Podaj ciąg znaków: ')

cyfry = 0
litery = 0

wystepowanie = {}

for znak in dane:
    if not (znak.isalpha() or znak.isnumeric()):
        dane.replace(znak, ' ')

for znak in dane:
    if znak != ' ':
        wystepowanie[znak] = wystepowanie.get(znak, 0) + 1
    if (znak.isnumeric()):
        cyfry += 1
    elif (znak.isalpha()):
        litery += 1

dane_split = dane.split()

print (f'slowa: {len(dane_split)}, litery: {litery}, cyfry: {cyfry}')
print (wystepowanie)