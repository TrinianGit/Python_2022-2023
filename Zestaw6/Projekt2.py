toSort = input()
def sorting_func(char):
    if (char.isalpha()):
        
        if (char.islower()):
            return ord(char)
        else:
            return ord(char) + 1000
    else:
        if (int(char) % 2 == 1):
            return ord(char) + 2000
        else:
            return ord(char) + 3000
            
toSort = ''.join(sorted(toSort, key = sorting_func))
print(toSort)