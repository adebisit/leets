from typing import List

def printMatrix(m):
    for i in range(len(m)):
        row = []
        for j in range(len(m[0])):
            row.append(str(m[i][j]))
        print(", ".join(row))
    
def setZeroes(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])

    first_column_zero = matrix[0][0] == 0
    first_row_zero = matrix[0][0] == 0
    for i in range(m):
        if matrix[i][0] == 0:
            first_column_zero = True
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                break
    
    for j in range(1, n):
        if matrix[0][j] == 0:
            first_row_zero = True
        for i in range(m):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                break

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
 
    if first_column_zero:
        for i in range(m):
            matrix[i][0] = 0
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

if __name__ == "__main__":
    test1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    setZeroes(test1)
    printMatrix(test1)
    print("\n")

    test2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    setZeroes(test2)
    printMatrix(test2)
    print("\n")

    test3 = [
        [1, 2, 3, 4, 0, 5, 6],
        [7, 0, 8, 9, 0, 1, 2],
        [4, 5, 8, 0, 2, 3, 4],
        [2, -1, 8, 0, 0, -1, 4],
        [0, -5, 0, 2, 0, 4, 3],
        [0, 0, -1, 2, 3, 4, 0],
        [1, 2, 3, 4, 5, 6, 7]
    ]
    setZeroes(test3)
    printMatrix(test3)
    print("\n")

    test4 = [
        [0,2,5,2,2],
        [2,2,5,8,9],
        [3,2,9,5,8],
        [8,6,9,8,9],
        [2147483647,5,1,6,1]
    ]
    setZeroes(test4)
    printMatrix(test4)