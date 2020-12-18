#BinarySearch.py
#2020 / 12 / 19

#재귀함수를 이용한 이진탐색
def binarySearch( array , target , start , end):
    if start > end: return

    mid = (start + end) // 2

    if array[ mid ] == target :
        return mid

    elif array[ mid ] > target :
        return binarySearch( array , target , start , mid - 1 )

    elif array[ mid ] < target :
        return  binarySearch( array , target , mid + 1 , end )

#반복문을 이용한 이진탐색
def binarySearch2( array , target , start , end) :

    while start <= end :
        mid = (start + end ) // 2

        if array[ mid ] == target :
            return mid

        elif array[ mid ] > target :
            end = mid - 1

        elif array[ mid ] < target :
            start = mid + 1

    return