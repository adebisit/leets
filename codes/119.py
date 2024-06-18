from typing import List

def getRow(self, rowIndex: int) -> List[int]:
    factorials = [1]
    for i in range(1, rowIndex + 1):
        factorials.append(i * factorials[i - 1])
    
    row = []
    for r in range(rowIndex + 1):
        row.append(int(factorials[rowIndex] / (factorials[rowIndex - r] * factorials[r])))
    return row