from typing import List

def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0
    minNoLeft = [prices[0]]
    maxNoRight = [prices[-1]]
    for i in range(1, n):
        if prices[i] < minNoLeft[-1]:
            minNoLeft.append(prices[i])
        else:
            minNoLeft.append(minNoLeft[-1])
        
        if prices[n - i - 1] > maxNoRight[-1]:
            maxNoRight.append(prices[n - i - 1])
        else:
            maxNoRight.append(maxNoRight[-1])

    max_profit = maxNoRight[1] - minNoLeft[0]
    for i in range(1, n - 1):
        if maxNoRight[n - i - 1] - minNoLeft[i] > max_profit:
            max_profit = maxNoRight[n - i - 1] - minNoLeft[i]
    return max_profit if max_profit > 0 else 0

# print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([5]))
