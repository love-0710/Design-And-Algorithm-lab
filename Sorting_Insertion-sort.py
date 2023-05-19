def insertionSort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


arr = [2, 4, 7, 1, 3, 19, 8]
insertionSort(arr)
print(arr)