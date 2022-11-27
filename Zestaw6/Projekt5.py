strings = input().split()
k, m = int(strings[0]), int(strings[1])

maximal = 0
lists = []

def recur(l, l_num, sm):
    global maximal, k, m, lists
    for i in l:
        sm_loc = sm + i ** 2
        if (l_num < k - 1):
            recur(lists[l_num + 1], l_num + 1, sm_loc)
        else:
            if ((sm_loc % m) > maximal):
                maximal = (sm_loc % m)
        

for _ in range(k):
    numbers = input().split()
    l = []
    for i in numbers[1:]:
        l.append(int(i))
    lists.append(l)
recur(lists[0], 0, 0)
print(maximal)