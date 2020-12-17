#RotateMatrix90Deree.py
# 2020 / 12 /17

# 2차원 행렬을 시계방향으로 90도 회전하는 메서드

def rotatate_a_matrix_by_90_degree(a):

    row_length = len(a)
    column_lenght = len(a[0])

    res = [[0] * row_length for _ in range(column_lenght)]

    for r in range(row_length):
        for c in range(column_lenght):
            res[c][(row_length - 1) - r] = a[r][c]

    return res


# 사용 예시

def printList(list):
    for c in list:
        for r in c:
            print("%4d"%r , end=' ')
        print(' ')

def Example_rotatate_a_matrix_by_90_degree():

    a = [
        [ 1 , 2 , 3 , 4 ],
        [ 5 , 6 , 7 , 8 ],
        [ 9 , 10, 11, 12],
    ]

    res = rotatate_a_matrix_by_90_degree(a)

    print("\ninput = \n")
    printList(a)

    print("\nres = \n")
    printList(res)


