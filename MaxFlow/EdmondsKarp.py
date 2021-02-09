from collections import deque
MAX = 53
INF = int(1e9)

graph = [[] for _ in range(MAX)]
capacity = [[0] * MAX for _ in range(MAX)]
flow = [[0] * MAX for _ in range(MAX)]
distance = [-1] * MAX


def c_to_i(ch: chr):
    if ch.isupper():
        return ord(ch) - ord('A')
    else:
        return ord(ch) - ord('a') + 26


def max_flow(start, end):
    result = 0
    while True:
        for i in range(MAX):
            distance[i] = -1
        q = deque()
        q.append(start)
        while q and distance[end] == -1:
            now = q.popleft()
            for will in graph[now]:
                if capacity[now][will] - flow[now][will] > 0:
                    q.append(will)
                    distance[will] = now
                    if will == end:
                        break
        if distance[end] == -1:
            break

        min_flow = INF
        target = end
        while target != start:
            min_flow = min(min_flow, capacity[distance[target]][target] - flow[distance[target]][target])
            target = distance[target]

        target = end
        while target != start:
            flow[distance[target]][target] += min_flow
            flow[target][distance[target]] -= min_flow
            target = distance[target]
        result += min_flow

    return result


n = int(input())
for i in range(n):
    now, will, cap = input().split()
    now = c_to_i(now)
    will = c_to_i(will)
    graph[now].append(will)
    graph[will].append(now)
    capacity[now][will] += int(cap)
    capacity[will][now] += int(cap)
print(max_flow(c_to_i('A'), c_to_i('Z')))
