#LIS.py
#2020 / 01 / 09
#UPDATE
#2020 / 01 / 11


import math

data = list(map(int,input().split()))


def LIS(data):
    #O(N^2)
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


def LIS2(data):
    #O(N^2)
    #Recursion RuntimeErr를 피하기 위한 BottomUp LIS
    n = len(data)
    data.reverse()
    dp = [1] * n

    data.reverse()

    for i in range(1, n):
        for j in range(i):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j] + 1)



print(LIS(data))