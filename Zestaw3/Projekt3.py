def odwracanie (L, left, right):
    i = left
    j = right
    while (j > i):
        save = L[i]
        L[i] = L[j]
        L[j] = save
        i += 1
        j -= 1

def odwracanie_recur (L, left, right):
    if left > right:
        return
    else:
        save = L[left]
        L[left] = L[right]
        L[right] = save
        odwracanie_recur(L, left + 1, right - 1)


List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
List2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

odwracanie(List1, 3, 8)
odwracanie_recur(List2, 2, 9)

print (List1)
print (List2)