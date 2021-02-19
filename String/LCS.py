#LCS
# 2021 / 02 / 19
# O(N * M)

def LCS(a, b):
    a = [' '] + list(a)
    b = [' '] + list(b)
    dp = [[''] * len(b) for _ in range(len(a))]

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[i]:
                dp[i][j] = dp[i - 1][j - 1] + a[i]
            else:
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
    return dp[len(a) - 1][len(b) - 1]