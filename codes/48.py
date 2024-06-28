from typing import List

def printMatrix(m):
    for i in range(len(m)):
        row = []
        for j in range(len(m[0])):
            row.append(str(m[i][j]))
        print(", ".join(row))


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)

    increments = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]

    p = [0, 0]
    curr = 0 
    temp0 = matrix[p[0]][p[1]]
    for i in range(n * 2):
        print(f"Before => {p[0]}, {p[1]}")
        print(f"Temp0 = {temp0}")
        p[0] += increments[curr][0]
        p[1] += increments[curr][1]
        if p[0] == 0 or p[0] == (n - 1) or p[1] == 0 or p[1] == (n - 1):
            curr += 1
        print(f"After => {p[0]}, {p[1]}\n")
        temp1 = matrix[p[0]][p[1]]
        print(f"Temp1 = {temp1}")
        matrix[p[0]][p[1]] = temp0
        temp0 = temp1
        print(f"Temp0 = {temp0}")



test0 = [
    [4, 8],
    [3, 6]
]
# rotate(test0)
# printMatrix(test0)

test1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# rotate(test1)
# printMatrix(test1)

test2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
rotate(test2)
printMatrix(test2)