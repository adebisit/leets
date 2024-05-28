from typing import List

def searchInsert(self, nums: List[int], target: int) -> int:
    n = len(nums)
    if target <= nums[0]:
        return 0
    if target == nums[n - 1]:
        return n - 1
    if target > nums[n - 1]:
        return n
    
    for i in range(1, n):
        if target <= nums[i] and target > nums[i - 1]:
            return i