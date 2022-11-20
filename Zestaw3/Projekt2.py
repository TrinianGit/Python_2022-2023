import re

roman = {1 : 'I', 4 : 'IV', 5 : 'V', 9 : 'IX', 10 : 'X', 40 : 'XL', 50 : 'L', 90 : 'XC', 100 : 'C', 400 : 'CD', 500 : 'D', 900 : 'CM', 1000 : 'M'}
number = {v : k for k, v in roman.items()}
roman_poss = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

def IntToRoman(int_num):
    global roman_poss
    global roman
    rom = ''
    for i in roman_poss:
        while (int_num >= i):
            rom += roman[i]
            int_num -= i
    return rom

def RomanToInt(rom_num):
    global number
    rom_num += rom_num[-1]
    num = 0
    prev = None
    for i in rom_num:
        if prev == None:
            prev = i
        elif (number[prev] < number[i]):
            num -= number[prev]
        else:
            num += number[prev]
        prev = i
    return num

num = input('Podaj liczbe w systemie rzymskim lub dziesiętnym: ')

if num.isnumeric():
    if (int(num) >= 0 and int(num) < 4000):
        print(IntToRoman(int(num)))
        exit(0)
    else:
        print('Podana liczba nie należy do zakresu 0-3999')
        exit(-1)
elif num.isalpha():
    if (re.search("M{0,3}(CM|CD|D){0,1}C{0,3}(XC|XL|L){0,1}X{0,3}(IX|IV|V){0,1}I{0,3}", num) != None):
        if (num == re.search("M{0,3}(CM|CD|D){0,1}C{0,3}(XC|XL|L){0,1}X{0,3}(IX|IV|V){0,1}I{0,3}", num).group(0)):
            print(RomanToInt(num))
            exit(0)
print('Podana wartość nie jest liczbą rzymską ani arabską')