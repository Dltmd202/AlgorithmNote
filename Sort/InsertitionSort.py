#InsertionSory.py
#2020 / 12 / 18


#self_made
def InsertionSort(array):

    for i in range( 1 , len( array ) ) :
        sorted_data = array[i]
        sorted_idx = i
        for j in range( i , -1 , -1 ) :
           if sorted_data < array[j]:
                array[sorted_idx] , array[j] = ( array[j] ,  array[sorted_idx] )
                sorted_idx = j


#open sorce

def InsertionSort2(array):

    for i in range( 1 , len( array ) ) :
        for j in range( i , 0 , -1 ) :
            if array[j - 1] > array [j] :
                array[j -1] , array [j] = (array[j] , array[j - 1])
            else: break





array = [7,5,9,0,3,1,6,2,4,8]

InsertionSort2(array)

print(array)

