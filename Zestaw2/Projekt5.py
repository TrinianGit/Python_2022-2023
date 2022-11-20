x = int (input('Podaj liczbe: '))
bits = bin(x)[2:]

max = 0
count = 0

for bit in bits:
    bit = int(bit)
    if (bit == 1):
        if (max < count):
            max = count
        count = 0
    else:
        count += 1

print (bits)
print (max)