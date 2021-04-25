
import datetime
start_time = datetime.datetime.now()

def insertion_sort(temp):

    for i in range(1, len(temp)):
        key = temp[i]
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
    i = (low-1)
    pivot = arr[high]
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

    arr1 =  [12, 121, 1733, 4435, 62342, 234]
    arr2 =  [15, 225, 233, 9440, 155, 3446, 6, 9349, 10]
    arr3 =  [217, 329, 1334, 5440, 4557, 4462, 2349, 72334, 31, 54, 240, 100]
    arr4 =  [319, 124, 5330, 4436, 556, 9329, 1430, 1231, 103, 58, 98, 885, 52, 63, 214]
    arr5 =  [817, 522, 6333, 244, 2558, 13246, 5338, 637, 94, 31, 43, 50, 84, 99, 761, 23, 37, 100]
    arr6 =  [919, 120, 333, 4413, 5539, 1434, 504, 497, 2345, 2484, 60, 33, 88, 76, 101, 62, 591, 70, 1239, 29, 55]
    arr7 =  [919, 210, 3311, 1443, 3559, 23414, 52340, 47, 25, 562, 93, 33, 55, 76, 101, 62, 531, 70, 916, 29, 55, 142]
    arr8 =  [143, 120, 323, 4413, 5539, 1344, 52343, 4345, 25, 322, 20, 103, 88, 4164, 101, 62, 51, 70, 24, 29, 55, 234, 34, 94]
    arr9 =  [919, 102, 333, 1444, 5536, 12344, 52340, 42347, 2235, 2, 90, 33, 88, 76, 101, 62, 51, 70, 9123, 29, 66123, 33, 65, 16, 68]
    arr10 = [919, 120, 1331, 1443, 5539, 1234, 52340, 47, 1010,  25, 32, 90, 33, 88, 75, 101, 62, 51, 76, 319, 323, 55, 432, 965, 42, 73]

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
# experimenta('Qui?ck')

