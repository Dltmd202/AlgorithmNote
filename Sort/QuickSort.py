#InsertionSory.py
#2020 / 12 / 18


#일반적인 quick_sort
def quick_sort(array , start , end):
    if start >= end: return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        while left <= end and array[left] <= array[pivot] : left += 1

        while right > start and array[right] >= array[pivot] : right -= 1

        if left > right:
            array[right] , array[pivot] = array[pivot] , array[right]

        else :  array[left] , array[right] = array[right],array[left]

    quick_sort(array , start , right-1)
    quick_sort(array, right + 1 , end)



#파이썬의 자유로운 리스트 설정을 이용한 quick_sort
def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)