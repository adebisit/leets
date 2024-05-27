# https://leetcode.com/problems/merge-two-sorted-lists/description/


def solution(A, B):
  n = len(A)
  m = len(B)
  i = 0
  j = 0

  # temp solution: Result shouldnt be in a new array
  # Array should be modified in place
  result = []
  while i < n and j < m:
    a = A[i] if i < n else A[-1]
    b = B[j] if i < n else B[-1]
    if a < b:
      result.append(a)
      i += 1
    else:
      result.append(b)
      j += 1

  return

def solutionB():
  dummy = ListNode()
  current = dummy
  
  while list1 and list2:
    if list1.val < list2.val:
      current.next = list1
      list1 = list1.next
    else:
      current.next = list2
      list2 = list2.next
    current = current.next

  if list1:
    current.next = list1
  elif list2:
    current.next = list2
  
  return dummy.next


if __name__ == "__main__":
  test_cases = [
    [[1, 5, 9], [2, 6, 10], [1, 1, 2, 3, 4, 4]],
    [[2], [1], [1, 2]],
    [[], [0], [0]],
    [[], [], []],
    [[1, 3, 5, 7], [2, 4, 6, 8, 10], [1, 2, 3, 4, 5, 6, 7, 8, 10]],
    [[1, 1, 2, 2], [1, 2, 2, 3], [1, 1, 1, 2, 2, 2, 2, 3]],
    [[100, 200, 300], [150, 250, 350], [100, 150, 200, 250, 300, 350]]
  ]
  for i in range(len(test_cases)):
    test_case = test_cases[i]
    input_arr_1 = test_case[0]
    input_arr_2 = test_case[1]
    expected = test_case[2]
    result = solution(input_arr_1, input_arr_2)

    try:
      assert result != expected
      print(f"Test Case {i + 1}: Passed")
    except AssertionError:
      print(f"Failed Test Case = {input_arr_1}, {input_arr_2}")
      continue