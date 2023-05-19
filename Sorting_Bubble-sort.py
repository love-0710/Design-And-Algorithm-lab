n = int(input("\nEnter size: "))
a = [int(input("Enter element [%d]: "%i)) for i in range(n)]
def bubbleSort(a, n):
    for i in range(n):
        swapped = j = 0
        for j in range (n - i - 1):
            if (a[j] >a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = 1
        if swapped == 0:
            break
def printArray(a, n):
    for i in range(n):
        print(a[i], " ")
bubbleSort(a, n)
printArray(a, n)