#Countsort.py
#2020 / 12 / 18
#O( N + K )
# N = len( array) K = max( array )


def countSort( array ):
    count = [0] * len( array )

    for i in array : count[i] += 1

    for i in range( len ( count ) ) :
        for j in range( count[i] ) :
            print( i , end = ' ')

