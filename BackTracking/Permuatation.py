import copy

n , m = map(int,input().split())

data = range(1,n+1)
visit = [False]*(n+1)
answer = []


def solution(select : list , m):
    if m == 0:
        global answer
        d = copy.deepcopy(select)
        print(d)
        answer.append(d)
        return

    for i in range(1,len(data)+1):
        if visit[i] == False :
            visit[i] = True
            select.append(i)
            solution(select,m-1)
            select.remove(i)
            visit[i] = False


solution([],m)

print(answer)