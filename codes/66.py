from typing import List

def plusOne(self, digits: List[int]) -> List[int]:
    n = len(digits)
    last_sum = 10
    i = n - 1
    while i >= 0:
        last_sum = digits[i] + (last_sum // 10)
        digits[i] = last_sum % 10
        i -= 1
        if last_sum < 10:
            return digits
    if last_sum == 10:
        return [1] + digits