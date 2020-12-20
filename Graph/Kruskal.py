#Kruskal.py
#2020 / 12 / 21

def find_parent(parent, x):
    if parent[x] != x:
        parent[x]  = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent , a ,b) :
    a = find_parent(parent ,a)
    b = find_parent(parent , b)
    if a > b : parent[a] = b
    else : parent[b] =a

def kruskal (parent ,edges):

    edges.sort()
    result = 0
    for edge in edges:
        cost , now , will = edge

        if find_parent(parent ,now) != find_parent(parent , will):
            union_parent(parent,now,will)
            result += cost
    return result








v ,e = map(int, input().split())

parent = [0] * (v+1)
for i in range(1,v+1): parent[i] = i

edges = []

for _ in range(e):
    now ,will ,cost = map(int , input().split())
    edges.append((cost , now ,will))


print(kruskal(parent,edges))