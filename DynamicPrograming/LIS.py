#LIS.py
#2020 / 01 / 09


import math

data = list(map(int,input().split()))


def solution(data):
    data = [-math.inf] + data
    n = len(data)
    dp = [-1]*n

    def find(start):
        if dp[start] != -1:
            return dp[start]


        ret = 0
        for nxt in range(start + 1 ,n):
            if data[start] < data[nxt]:
                ret = max(ret , 1 + find(nxt))
        dp[start] = ret
        return ret




    return find(0)

print(solution(data))