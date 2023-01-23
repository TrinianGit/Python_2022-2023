import time
from mtablica import MonitorowanaTablica
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import copy

N = 50  # liczba elementów, można zmieniać
FPS = 60  # klatki na sekundę do parametru interval 

tablica = MonitorowanaTablica(0, 1000, N, "R") # zbadaj też opcje: "S", "A", "T"

###############################################
################# Tim Sort ##################

def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

def merge(tab, start, mid, end):
    tmp = [None] * (end - start + 1)
    start1 = start
    end1 = mid
    start2 = mid + 1
    end2 = end
    i = 0
    while start1 <= end1 and start2 <= end2:
        if tab[start1] <= tab[start2]:
            tmp[i] = tab[start1]
            start1 += 1
        else:
            tmp[i] = tab[start2]
            start2 += 1
        i += 1
    while start1 <= end1:
        tmp[i] = tab[start1]
        start1 += 1
        i += 1
    while start2 <= end2:
        tmp[i] = tab[start2]
        start2 += 1
        i += 1

    for i in range(end - start + 1):
        tab[start + i] = tmp[i]

def timsort(array):
    min_run = 10
    n = len(array)
    sorting_idx = []
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))
        sorting_idx.append((i, min((i + min_run - 1), n - 1)))
    tmpsorting = []
    while (len(sorting_idx) != 1):
        start = sorting_idx[0][0]
        end = sorting_idx[1][1]
        midpoint = sorting_idx[0][1]
        merge(array, start, midpoint, end)
        sorting_idx.pop(0)
        sorting_idx.pop(0)
        tmpsorting.append((start, end))
        if(len(sorting_idx) == 1):
            tmpsorting.append(sorting_idx[0])
            sorting_idx = copy.deepcopy(tmpsorting)
            tmpsorting.clear()
        elif(len(sorting_idx) == 0):
            sorting_idx = copy.deepcopy(tmpsorting)
        


    return array

algorytm = "Tim"
t0 = time.perf_counter()
timsort(tablica)
delta_t = time.perf_counter() - t0
###############################################
###############################################
print(f"Sortowanie: {algorytm}")
print(f"Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica.pelne_kopie):.0f}.")
###############################################

# konfiguracja wyświetlania histogramu
plt.rcParams["font.size"] = 16
fig, ax = plt.subplots(figsize=(16, 8))
container = ax.bar(np.arange(0, len(tablica), 1), tablica.pelne_kopie[0], align="edge", width=0.8)
fig.suptitle(f"Sortowanie: {algorytm}")
ax.set(xlabel="Indeks", ylabel="Wartość")
ax.set_xlim([0, N])
txt = ax.text(0.01, 0.99, "", ha="left", va="top", transform=ax.transAxes)

# funkcja aktualizująca stan poszczególnych klatek do wyświetlenia
def update(frame):
    txt.set_text(f"Liczba operacji = {frame}")
    for rectangle, height in zip(container.patches, tablica.pelne_kopie[frame]):
        rectangle.set_height(height)
        rectangle.set_color("darkblue")

    idx, op = tablica.aktywnosc(frame)
    if op == "get":
        container.patches[idx].set_color("green")
    elif op == "set":
        container.patches[idx].set_color("red")

    return (txt, *container)

# tu akumulowana jest animacja, wyświetlna komendą show
ani = FuncAnimation(fig, update, frames=range(len(tablica.pelne_kopie)), blit=True, interval=1000./FPS, repeat=False)
plt.show()