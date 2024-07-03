from typing import List

def printMatrix(m):
    for i in range(len(m)):
        row = []
        for j in range(len(m[0])):
            row.append(str(m[i][j]))
        print(", ".join(row))


# def rotate(matrix: List[List[int]]) -> None:
#     n = len(matrix)

#     increments = [
#         [0, n - 1],
#         [n - 1, 0],
#         [0, - (n - 1)],
#         [-(n - 1), 0]
#     ]

#     for j in range(n):
#         p = [0, j]
#         temp0 = matrix[p[0]][p[1]]
#         for j in range(4):
#             print(f"Before => {p[0]}, {p[1]}")
#             print(f"Temp0 = {temp0}")

#             p[0] += increments[j][0]
#             p[1] += increments[j][1]

#             print(f"After => {p[0]}, {p[1]}")
#             temp1 = matrix[p[0]][p[1]]
#             matrix[p[0]][p[1]] = temp0
#             temp0 = temp1
#             print(f"New Temp0 = {temp0}\n")

#         printMatrix(matrix)


def rotate(matrix: List[List[int]]) -> None:
    # printMatrix(matrix)
    n = len(matrix)
    level = 0
    # n = n - (level * 2)
    while n > 1:
        for x in range(n - 1):
            i = 0
            j = x
            # print(f'Former Pos = {i}, {j}')
            direction = [0, 1]
            temp = matrix[i + level][j + level]
            for y in range(3):
                for z in range(n - 1):
                    if i == 0 and j == n - 1:
                        direction[0] = 1
                        direction[1] = 0
                    elif i == n - 1 and j == n - 1:
                        direction[0] = 0
                        direction[1] = -1
                    elif i == n - 1 and j == 0:
                        direction[0] = -1
                        direction[1] = 0
                    
                    i += direction[0]
                    j += direction[1]
                # print(f'New = {i}, {j}')
                # input("\nNext")
                temp2 = matrix[i + level][j + level]
                # print(f"Before swap temp = {temp}")
                matrix[i + level][j + level] = temp
                temp = temp2
                # print(f"After swap temp = {temp}")
            matrix[level][x + level] = temp
        n -= 2
        level += 1


test0 = [
    [1]
]
rotate(test0)
# printMatrix(test0)


test1 = [
    [4, 8],
    [3, 6]
]
# rotate(test0)
# printMatrix(test0)

test2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# rotate(test1)
# printMatrix(test1)

test3 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
# rotate(test2)
# printMatrix(test2)

test4 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
# rotate(test3)
# printMatrix(test3)