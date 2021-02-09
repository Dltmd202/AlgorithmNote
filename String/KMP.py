#KMP
# 2021 / 02 / 09


def fail(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


def kmp(parent, pattern):
    table = fail(pattern)
    parent_len = len(parent)
    pattern_len = len(pattern)
    j = 0
    cnt = 0
    answer = []
    for i in range(parent_len):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if pattern_len - 1 == j:
                cnt += 1
                answer.append(i - pattern_len)
                j = table[j]
            else:
                j += 1
    return cnt, answer
