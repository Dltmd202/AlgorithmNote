#Dijkstra.py
#2020 / 12 / 20

#import
import sys
import heapq


input = sys.stdin.readline
INF = int(1e9)

n , m = map( int , input().split())
start = int(input())

graph = [ [] for i in range(n + 1)]

visited = [False] * ( n + 1)

distance = [INF] * ( n + 1 )

#삽입
for _ in range(m):
    a ,b ,c = map(int , input().split())
    graph[a].append(b,c)


#O(V^2) 다익스트라
def get_smallest_node():
    min_value = 0
    index = 0
    for i in range( 1 , n + 1 ):
        if distance[ i ] < min_value and not visited[ i ] :
            min_value = distance[ i ]
            index = i
    return index

def dijkstra( start ):
    distance[ start ] = 0
    visited[ start ]  = True

    for j in graph[ start ]:
        distance[ j[ 0 ] ] = j[ 1 ]

    for i in range( n - 1 ) :
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now] :
            cost = distance[ now ] + j[ 1 ]

            if cost < distance[ j[ 0 ] ]:
                distance[ j[ 0 ] ] = cost

#O(ElogV) 다익스트라
def dijkstra2(start):
    q = []
    heapq.heappush(q , ( 0 , start))
    distance[start] = 0

    while q :
        dist , now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for will in graph[now] :
            cost = dist + will[1]

            if cost < distance[will[0]] :
                distance[will[0]] = cost
                heapq.heappush( q , ( cost , will[0]))