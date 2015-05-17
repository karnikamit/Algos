__author__ = 'karnikamit'

def quicksort(a):
    split = partition(a)
    a1 = a[:split]
    print('not sorted a1', a1)
    if a1:
        list1 = partition(a1)
        if list1 == 1:
            print(' sorted a1', a1)
    a2 = a[split+1:]
    print('not sorted a2', a2)
    if a2:
        list2 = partition(a2)
        print('list2', list2)
    print(list(list1, list2))

def partition(array):
    if len(array) > 1:

        low = 0
        high = len(array) - 1
        pivot = array[low]
        i = low+1
        j = len(array) - 1

        while array:
            while array[i] < pivot:         # inc i until u find a greter no than the pivot
                i += 1

            while array[j] > pivot:         # dec j until u find a smaller than the pivot
                j -= 1

            if i < j:
                array[i], array[j] = array[j], array[i]
            else:
                array[j], array[low] = array[low], array[j]
                print(array)
                return j
    else:
        return array
if __author__ == 'karnikamit':
    # Input a list
    # quicksort()
