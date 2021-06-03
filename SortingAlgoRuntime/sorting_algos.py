#Sorting Algorithms

#Quicksort Algorithm

def quicksort(arr):

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)

#Bubble Sort

def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(len(arr) -1):
            if arr[i] > arr[i + 1]:
                swap_happened = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


#Selection Sort

def selection_sort(arr):

    marker = 0
    while marker < len(arr):
        for num in range(marker, len(arr)):
            if arr[num] < arr[marker]: 
                arr[marker], arr[num] = arr[num], arr[marker]
        marker += 1



#Merge Sort

def merge_sort_iter(arr1, arr2):

    sorted_arr = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def mergesort(arr):

    if len(arr) < 2:
        return arr[:]

    else:
        middle = len(arr) // 2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sort_iter(l1, l2)
