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

    print("Before Starting")
    printMatrix(matrix)
    input("Press Enter to continue:\n")

    for i in range(m):
        print(f"Considering row {i}")
        inverted_row = False
        for j in range(n):
            if matrix[i][j] == 0:
                for _j in range(n):
                    inverted_row = True
                    matrix[i][_j] = 0 if matrix[i][_j] != 0 else -1
                break

        if not inverted_row:
            print("No value '0' in row")
            input("Press Enter to continue:\n")
            continue

        print("Inverted matrix looks like")
        printMatrix(matrix)
        input("Press Enter to continue:\n")

        for j in range(n):
            if matrix[i][j] == -1:
                for _i in range(m):
                    matrix[_i][j] = 0
        
        print("Inverting columns as well")
        printMatrix(matrix)
        input("Press Enter to continue:\n")

test1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
setZeroes(test1)

test2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

test3 = [
    [1, 2, 3, 4, 0, 5, 6],
    [7, 0, 8, 9, 0, 1, 2],
    [4, 5, 8, 0, 2, 3, 4],
    [2, -1, 8, 0, 0, -1, 4],
    [0, -5, 0, 2, 0, 4, 3],
    [0, 0, -1, 2, 3, 4, 0],
    [1, 2, 3, 4, 5, 6, 7]
]