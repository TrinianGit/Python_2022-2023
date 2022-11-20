import json

def sort_tuple(l_tup):
    l_tup.sort(key = lambda x: x[1])
    l_tup.reverse()
    return l_tup

with open('./tramwaje.json', 'r', encoding = 'utf-8') as read_file:
    data = json.load(read_file)

result = {}
przystanki = set()
linia_przystanki = []

for l in data['linia']:
    trasa = []
    liczba = 0
    if 'przystanek' in l:
        for t in l['przystanek']:
            liczba += 1
            trasa.append(t['name'][:-3])
            przystanki.add(t['name'][:-3])
    linia_przystanki.append(((int(l['name'])), liczba))
    result[int(l['name'])] = tuple(trasa)

linia_przystanki = sort_tuple(linia_przystanki)

with open ('tramwaje_out.json', 'w', encoding = 'utf-8') as file:
    json.dump(result, file, ensure_ascii = False)

print (linia_przystanki)
print (przystanki)
