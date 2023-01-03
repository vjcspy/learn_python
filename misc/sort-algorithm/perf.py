import cProfile
from numpy import random

NUM_OF_ARRAY = 100
NUM_OF_ELEM = 5000

# ____________________________________________________________________________________________________


def mergeSort(arr):
    if (len(arr) > 1):
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # sắp sếp lại các phần tử của L và R và gán chúng vào array
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Chèn các phần tử còn lại của L hoặc R vào array
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# ____________________________________________________________________________________________________


def partition(arr, start, end):
    # print('swap from', start, 'to', end, 'with array', arr)
    # Từ 0 -> i sẽ là những phần tử nhỏ hơn pivot
    i = start - 1

    # sử dụng cách chọn phần tử cuối cùng làm pivot
    pivot = arr[end]

    for j in range(start, end+1):
        # chỗ này để bằng rất hợp lý, để nó có thể swap phần tử cuối cùng
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    return i


def quick_sort(array, start, end):
    if start < end:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot_index = partition(array, start, end)
        # print('after swap', array, 'with pivot index', pivot_index)
        # Recursive call on the left of pivot
        quick_sort(array, start, pivot_index - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pivot_index + 1, end)

# ____________________________________________________________________________________________________


def generate_array():
    list_to_sort = []
    for _ in range(NUM_OF_ARRAY):
        list_to_sort.append(random.randint(10000, size=(NUM_OF_ELEM)))

    return list_to_sort

# ____________________________________________________________________________________________________


x = generate_array()


def pefMegeSort():
    for i in x.copy():
        mergeSort(i)


def pefQuickSort():
    for i in x.copy():
        quick_sort(i, 0, NUM_OF_ELEM-1)


cProfile.run('pefQuickSort()')
cProfile.run('pefMegeSort()')
