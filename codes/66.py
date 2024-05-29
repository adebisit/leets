from typing import List

def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        quotient = 0
        
        for i in range(n - 1, 0, -1):
            print(digits)
            digits[i] = digits[i] + 1 + quotient
            if (digits[i] > 9):
                digits[i] = 0
                quotient = 1
        if quotient != 0:
            return [0] + digits
        else:
            return digits
        