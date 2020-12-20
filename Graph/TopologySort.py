#TopologySort.py
#2020 / 12 / 21


from collections import deque

v, e = map( int , input().split())

graph = [ [] for _ in range( v + 1 ) ]
indgree = [ 0 ] * ( v + 1 )

for i in range( e ):
    a , b = map( int , input().split())
    graph[ a ].append( b )
    indgree[ b ] += 1

def topologySort():
    result = []
    q = deque()

    for i in range( 1 , v + 1 ):
        if indgree[i] == 0:
            deque.append( q , i )

    while q:
        now = deque.popleft( q )
        result.append( now )

        for will in graph[ now ]:
            indgree[ will ] -= 1
            if indgree[ will ] == 0 :
                deque.append( q , will)
    return result

res = topologySort()

for i in res:
    print(i ,end=' ')























