# fibo.py
#2020 / 12 / 19


#피보나치 수열

#DP Table
cache = [0] * 1000

#Top-down(Memoization)

def fibo(x):

    global cache

    if x == 1 or x == 2 :
        return 1

    if cache[x] != 0 :
        return cache[x]

    cache[x] = fibo( x - 1 ) + fibo( x - 2 )
    return cache[x]

#Botton-Up

def fibo2(x):

    cache[1] = 1
    cache[2] = 1

    for i in range( 3 , x + 1 ):
        cache[ i ] = cache[ i - 1 ] + cache[ i - 2 ]
    return cache[ x ]

