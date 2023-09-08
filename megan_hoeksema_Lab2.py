import random
from time import time
from tabulate import tabulate

def mergeSort(L):
    list_length = len(L)
    if list_length == 1:
        return L
    mid_point = list_length // 2
    left_partition = mergeSort(L[:mid_point])
    right_partition = mergeSort(L[mid_point:])
    return merge(left_partition, right_partition)


def merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output

def insertionSort(L):
    for i in range(1, n):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j = j - 1
        L[j + 1] = key

def bubbleSort(L):
    n = len(L)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]

table = {}
for n in range(100,5001,100):
    L = [i for i in range(n)]
    random.shuffle(L)

    t1 = time()

    b = mergeSort(L)
    t2 = time()
    mTime = (t2-t1)*1000

    c = insertionSort(L)
    t3 = time()
    iTime = (t3 - t1) * 1000

    d = bubbleSort(L)
    t4 = time()
    bTime = (t4 - t1) * 1000


    table[n] = round(mTime,1), round(iTime,1), round(bTime,1)


headers = ['n', 'Merge', 'Insert', 'Bubble']
print(tabulate([(k,) + v for k,v in table.items()], headers=headers))

