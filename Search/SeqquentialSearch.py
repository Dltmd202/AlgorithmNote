#SeqquentialSearch.py
#2020 / 12 / 19


def sequential_search(n , target , array):

    for i in range ( n ) :
        if array[ i ] == target:
            return i + 1

