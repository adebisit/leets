from typing import List

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
        return nums1
    for i in range(m):
        a = nums1[i]
        b = nums2[0]
        if a > b:
            nums1[i] = b
            for j in range(1, n + 1):
                if j == n or nums2[j] >= a:
                    nums2[j - 1] = a
                    break
                elif nums2[j] < a:
                    nums2[j - 1] = nums2[j]
    print(nums1)
    print(nums2)
    for i in range(m, m + n):
        nums1[i] = nums2[i - m]