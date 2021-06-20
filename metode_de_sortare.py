
import datetime
import random
start_time = datetime.datetime.now()

def insertion_sort(temp):

    # Traverse through 1 to len(arr)
    for i in range(1, len(temp)):

        key = temp[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i- 1
        while j >= 0 and key < temp[j]:
            temp[j + 1] = temp[j]
            j -= 1
        temp[j + 1] = key
    print(temp)
#####################

def selection_sort(L):
    for i in range(len(L) - 1):
        min_index = i
        for j in range(i + 1, len(L) - 1):

            if L[j] < L[min_index]:
                min_index = j

        L[i], L[min_index] = L[min_index], L[i]
    print(L)

#####################
# def selectionSort(array):
#     n = len(array)
#     for i in range(n):
#         # Initially, assume the first element of the unsorted part as the minimum.
#         minimum = i
#
#         for j in range(i + 1, n):
#             if (array[j] < array[minimum]):
#                 # Update position of minimum element if a smaller element is found.
#                 minimum = j
#
#         # Swap the minimum element with the first element of the unsorted part.
#         temp = array[i]
#         array[i] = array[minimum]
#         array[minimum] = temp
#
#     return array

#####################

def bubble_sort(list1):
    count=len(list1)
    for i in range(count):
        for j in range(count-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    print (list1)

def merge_sort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1

def partition(arr, low, high):
    i = (low-1)      # index of smaller element
    pivot = arr[high]    # pivot
    for j in range(low, high):


        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def calculateTime(start_time):
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds()
    return execution_time

def experimenta (aux):


    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    arr5 = []
    arr6 =[]
    arr7 = []
    arr8 = []
    arr9 = []
    arr10 = []
    print("number of array elements:")
    x = input()
    x = int(x)
    for i in range(x):
        n = random.randint(1000000, 10000000)
        # arry.append(n)
        arr1.append(n)
        arr2.append(n)
        arr3.append(n)
        arr4.append(n)
        arr5.append(n)
        arr6.append(n)
        arr7.append(n)
        arr8.append(n)
        arr9.append(n)
        arr10.append(n)

    if aux == 'Insertion':
        print("Insertion sort algorithm:\n")
        insertion_sort(arr1)
        insertion_sort(arr2)
        insertion_sort(arr3)
        insertion_sort(arr4)
        insertion_sort(arr5)
        insertion_sort(arr6)
        insertion_sort(arr7)
        insertion_sort(arr8)
        insertion_sort(arr9)
        insertion_sort(arr10)
        execution_time = calculateTime(start_time)
        print("--- %s seconds ---" % execution_time)

    elif  aux == 'Selection':
        print("Selection sort algorithm:\n")
        selection_sort(arr1)
        selection_sort(arr2)
        selection_sort(arr3)
        selection_sort(arr4)
        selection_sort(arr5)
        selection_sort(arr6)
        selection_sort(arr7)
        selection_sort(arr8)
        selection_sort(arr9)
        selection_sort(arr10)
        execution_time = calculateTime(start_time)
        print("--- %s seconds ---" % execution_time)

    elif  aux == 'Bubble':
        print("Bubble sort algorithm:\n")
        bubble_sort(arr1)
        bubble_sort(arr2)
        bubble_sort(arr3)
        bubble_sort(arr4)
        bubble_sort(arr5)
        bubble_sort(arr6)
        bubble_sort(arr7)
        bubble_sort(arr8)
        bubble_sort(arr9)
        bubble_sort(arr10)
        execution_time = calculateTime(start_time)
        print("--- %s seconds ---" % execution_time)

    elif  aux == 'Merge':
        print("Merge sort algorithm:")
        merge_sort(arr1)
        merge_sort(arr2)
        merge_sort(arr3)
        merge_sort(arr4)
        merge_sort(arr5)
        merge_sort(arr6)
        merge_sort(arr7)
        merge_sort(arr8)
        merge_sort(arr9)
        merge_sort(arr10)
        print('\n', arr1, '\n', arr2, '\n', arr3,
              '\n', arr4, '\n', arr5, '\n', arr6,
              '\n', arr7, '\n', arr8, '\n', arr9,
              '\n', arr10)

        execution_time = calculateTime(start_time)
        print("--- %s seconds ---" % execution_time)


    elif  aux == 'Quick':
        print("Quick sort algorithm:")
        quick_sort(arr1, 0, len(arr1) - 1)
        quick_sort(arr2, 0, len(arr2) - 1)
        quick_sort(arr3, 0, len(arr3) - 1)
        quick_sort(arr4, 0, len(arr4) - 1)
        quick_sort(arr5, 0, len(arr5) - 1)
        quick_sort(arr6, 0, len(arr6) - 1)
        quick_sort(arr7, 0, len(arr7) - 1)
        quick_sort(arr8, 0, len(arr8) - 1)
        quick_sort(arr9, 0, len(arr9) - 1)
        quick_sort(arr10, 0, len(arr10) - 1)

        print('\n', arr1, '\n', arr2, '\n', arr3,
              '\n', arr4, '\n', arr5, '\n', arr6,
              '\n', arr7, '\n', arr8, '\n', arr9,
              '\n', arr10)

        execution_time = calculateTime(start_time)
        print("--- %s seconds ---" % execution_time)




experimenta('Insertion')
# experimenta('Selection')
# experimenta('Bubble')
# experimenta('Merge')
# experi15menta('Qui?ck')


