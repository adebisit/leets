def climbStairs(n: int) -> int:
    n1 = 1
    n2 = 2
    if n == 1:
        return n1
    for _ in range(n - 2):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2 

print(climbStairs(1))
print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(5))
print(climbStairs(6))