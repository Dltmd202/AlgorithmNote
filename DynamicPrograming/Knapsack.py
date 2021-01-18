#Knapsack.py
#2021 / 01 / 19
#O(N * W )

import sys

input = sys.stdin.readline
n, w = map(int, input().split())
data = [tuple(map(int,input().split())) for _ in range(n)]


knap = [0 for _ in range(w+1)]

for i in range(n):
    for j in range(w, 1, -1):
        if data[i][0] <= j:
            knap[j] = max(knap[j], knap[j-data[i][0]] + data[i][1])
print(knap[-1])