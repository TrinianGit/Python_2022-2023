from numpy import intersect1d


x = input ('Podaj elementy pierwszego zbioru: ')
y = input ('Podaj elementy drugiego zbioru: ')

def intoset (data):
    toReturn = set()
    data = data.split()
    for i in range (len(data)):
        toReturn.add(data[i])
    return toReturn

set1 = intoset (x)
set2 = intoset (y)

print (set1.intersection(set2))
print (set1.union(set2))