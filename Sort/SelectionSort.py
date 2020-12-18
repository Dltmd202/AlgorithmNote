#SelectionSort.py
#2020 / 12 / 18
#O(N^2)

def selctionSort(array):

    for i in range(len(array)):
        min_idx = i
        for j in range(i,len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i] , array[min_idx] = (array[min_idx] , array[i])







