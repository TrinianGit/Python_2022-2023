list_base =  [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]

max = 0
x = []

def recurinto (lista, depth):
    global max
    global x
    for item in lista:
        if isinstance(item, list):
            recurinto(item, depth + 1)
    if depth > max:
        x.clear()
        max = depth
        x.append(lista)
    elif (depth == max):
        x.append(lista)

recurinto(list_base, 0)
for item in x:
    item.append(item[-1] + 1)
print(list_base)
